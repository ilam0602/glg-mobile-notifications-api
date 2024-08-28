import base64
import csv
from io import StringIO
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, messaging, firestore
from dotenv import load_dotenv
import os
import json

app = Flask(__name__)
load_dotenv()

firebase_service_account_key = json.loads(os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY"))
cred = credentials.Certificate(firebase_service_account_key)
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Function to send FCM notification
def send_fcm_notification(title, body, contact_id):
    print('in send fcm')
    try:

        # Get the document from Firestore where 'contact_id' matches the given contact_id
        users_ref = db.collection('users_test')
        query = users_ref.where('contact_id', '==', contact_id).limit(1).get()

        if not query:
            return None, f"No document found with contact_id: {contact_id}"
        
        user_doc = query[0]
        user_doc = user_doc.to_dict()
        apns_tokens = user_doc.get('apns-token')

        if not apns_tokens:
            return None, f"No APNS tokens found for contact_id: {contact_id}"

        responses = []
        print('apns_tokens:', apns_tokens)
        for token in apns_tokens:
            message = messaging.Message(
                token=token,
                apns=messaging.APNSConfig(
                    payload=messaging.APNSPayload(
                        aps=messaging.Aps(
                            alert=messaging.ApsAlert(title=title, body=body),
                            content_available=True,
                            badge=0,
                            sound='default',
                        ),
                    ),
                    headers={
                        'apns-priority': '10',  # Set the priority to 10 (immediate delivery)
                    },
                ),
                data={
                    'custom_key': 'custom_value',
                },
            )
            response = messaging.send(message)
            responses.append(response)

        return responses, None
    except Exception as e:
        print(e)
        return None, str(e)

@app.route('/send', methods=['POST'])
def send_notification():
    try:
        # Parse the incoming JSON request
        data = request.json
        title = data.get('title')
        body = data.get('body')
        contact_id = data.get('contact_id')
        
        # Validate input
        if not title or not body or not contact_id:
            return jsonify({'error': 'Title, body, and contact_id are required fields'}), 400
        
        # Call the function to send the notification
        responses, error = send_fcm_notification(title, body, contact_id)
        
        if error:
            return jsonify({'error': error}), 500
        
        # Return success response
        return jsonify({'success': True, 'message_ids': responses}), 200
    except Exception as e:
        # Handle any exceptions that occur
        return jsonify({'error': str(e)}), 500
@app.route('/send_csv', methods=['POST'])
def send_notifications_from_csv():
    data = request.json

    if 'content' not in data:
        return jsonify({'error': 'No content provided'}), 400

    encoded_content = data['content']
    
    try:
        # Decode the base64 encoded string
        decoded_content = base64.b64decode(encoded_content).decode('utf-8')

        # Read the CSV content from the decoded string
        stream = StringIO(decoded_content)
        csv_input = csv.DictReader(stream)
        
        results = []
        for row in csv_input:
            title = row.get('title')
            body = row.get('body')
            contact_id = row.get('contact_id')
            
            if not title or not body or not contact_id:
                continue  # Skip rows with missing data
            
            responses, error = send_fcm_notification(title, body, contact_id)
            if error:
                results.append({'contact_id': contact_id, 'error': error})
            else:
                results.append({'contact_id': contact_id, 'message_ids': responses})
        
        return jsonify({'results': results}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to process CSV'}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)