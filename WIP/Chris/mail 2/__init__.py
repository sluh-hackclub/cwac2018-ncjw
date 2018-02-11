# Update console commands:
# echo "export SENDGRID_API_KEY='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'" > sendgrid.env
# echo "sendgrid.env" >> .gitignore
# source ./sendgrid.env
# SendGrid Library (Github Site): https://github.com/sendgrid/sendgrid-python"""


import os

from mail.sendgrid import sendgrid
from mail.sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
# SENDGRID API Key must be PURCHASED from Sendgrid and INSTALLED onto the server !!!

from_email = Email("test@test.com")
to_email = Email("test@test.com")

subject = "AAAA"
content = Content("text/plain", "AAAA BBB CC D")

mail = Mail(from_email, subject, to_email, content)

response = sg.client.mail.send.post(request_body=mail.get())

print(response.status_code)
print(response.body)
print(response.headers)
