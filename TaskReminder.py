#####################################################################
# Sending SMS through Textbelt

# import requests
# def send_text(numstring, message):
#     message = {"number": numstring, "message": message}
#     r = requests.post("https://textbelt.com/text", data=message)
#     return r.status_code, r.text
#
# status=send_text('6666666666', 'How are you')
#
# print(status)
################################################################
# Sending SMS through Textbelt using the open source code available on Github

# from pytextbelt import Textbelt#
# Recipient = Textbelt.Recipient("6666666666", "us")
# reponse = Recipient.send("Hello World!")
# reponse = Recipient.send("Its me, The Bot.")

###################################################################
# Sending SMS through Twilio
# First install Twilio using : pip install twilio (windows)

# Method 1: by setting up environment variables.

# import os
# from twilio.rest import Client
# client = Client(os.environ.get('TWILIO_ACCOUNT_SID'),
#                 os.environ.get('TWILIO_AUTH_TOKEN'))
#
# client.messages.create(from_=os.environ.get('TWILIO_PHONE_NUMBER'),
#                        to=os.environ.get('CELL_PHONE_NUMBER'),
#                        body='You got a message from Python using Twilio!')

# Method 2:

import os
from twilio.rest import Client

accountSid = "jjjjjjjjjjjjjjjjj"
authToken = "kkkkkkkkkkkkkkkkk"

client = Client(accountSid, authToken)
myTwilioNumber = "+1888888"
destCellPhone = "+17777777"
myMessage = client.messages.create(body = "You got message from Python using Twilio",
                                   from_=myTwilioNumber,
                                   to=destCellPhone)

