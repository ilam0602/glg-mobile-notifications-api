# Example JSON Payload for `/send` Endpoint

```json
{
    "Headers": {
        "content-type": "application/json"
    },
    "Body": {
        "title": "example title",
        "body": "example body",
        "contact_id": "123456789"
    }
}
```

# Example JSON Payload for `/send_csv` Endpoint

```json
{
    "Headers": {
        "content-type": "application/json"
    },
    "Body": {
        "content": "dGl0bGUsYm9keSxjb250YWN0X2lkCiJXZWxjb21lIiwiSGVsbG8gYW5kIHdlbGNvbWUgdG8gb3VyIHNlcnZpY2UhIiwiODIyODMwNjc4IgoiUmVtaW5kZXIiLCJEb24ndCBmb3JnZXQgYWJvdXQgeW91ciBhcHBvaW50bWVudCB0b21vcnJvdyEiLCI4MjI4MzA2NzgiCg=="
    }
}
```

# Base64 Encoded Content for `/send_csv`

The `content` field in the JSON payload is a Base64 encoded version of the following CSV data:

```csv
title,body,contact_id
"Welcome","Hello and welcome to our service!","123456789"
"Reminder","Don't forget about your appointment tomorrow!","123456789"
```

# Example cURL Command

To send the Base64 encoded CSV content using a POST request to the `/send_csv` endpoint, you can use the following cURL command:

```bash
curl -s -X POST "http://35.247.39.169:8765/send_csv" \
-H "Content-Type: application/json" \
-d "{\"content\":\"dGl0bGUsYm9keSxjb250YWN0X2lkCiJXZWxjb21lIiwiSGVsbG8gYW5kIHdlbGNvbWUgdG8gb3VyIHNlcnZpY2UhIiwiODIyODMwNjc4IgoiUmVtaW5kZXIiLCJEb24ndCBmb3JnZXQgYWJvdXQgeW91ciBhcHBvaW50bWVudCB0b21vcnJvdyEiLCI4MjI4MzA2NzgiCg==\"}"
```
