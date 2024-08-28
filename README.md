/send
{
    "Headers": {
        "content-type": "application/json"
    },
    "Body": {
        "title" : "example title",
        "body" : "example body",
        "contact_id" : "822830678"
    }
}

/send_csv
{
    "Headers": {
        "content-type": "application/json"
    },
    "Body": {
        "content": "dGl0bGUsYm9keSxjb250YWN0X2lkCiJXZWxjb21lIiwiSGVsbG8gYW5kIHdlbGNvbWUgdG8gb3VyIHNlcnZpY2UhIiwiODIyODMwNjc4IgoiUmVtaW5kZXIiLCJEb24ndCBmb3JnZXQgYWJvdXQgeW91ciBhcHBvaW50bWVudCB0b21vcnJvdyEiLCI4MjI4MzA2NzgiCg=="
    }
}

content is generated using base 64 encoding of following csv file:

title,body,contact_id
"Welcome","Hello and welcome to our service!","822830678"
"Reminder","Don't forget about your appointment tomorrow!","822830678"


Example curl:

curl -s -X POST "http://35.247.39.169:8765/send_csv" \
-H "Content-Type: application/json" \
-d "{\"content\":\"dGl0bGUsYm9keSxjb250YWN0X2lkCiJXZWxjb21lIiwiSGVsbG8gYW5kIHdlbGNvbWUgdG8gb3VyIHNlcnZpY2UhIiwiODIyODMwNjc4IgoiUmVtaW5kZXIiLCJEb24ndCBmb3JnZXQgYWJvdXQgeW91ciBhcHBvaW50bWVudCB0b21vcnJvdyEiLCI4MjI4MzA2NzgiCg==\"}"





