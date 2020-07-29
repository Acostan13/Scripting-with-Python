from twilio.rest import Client

account_sid = 'ACcb0a7b9893ae8d3b44c89a6c1a431057'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+15614199653',
    body='Lets goooo',
    to='+15613965770'
)

print(message.sid)
