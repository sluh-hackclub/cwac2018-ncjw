# Update console commands:
# echo "export SENDGRID_API_KEY='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'" > sendgrid.env
# echo "sendgrid.env" >> .gitignore
# source ./sendgrid.env
# SendGrid Library (Github Site): https://github.com/sendgrid/sendgrid-python"""

import os
import base64
import csv
from io import StringIO
import simplejson

from mail.sendgrid import sendgrid
from mail.sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
# SENDGRID API Key must be PURCHASED from Sendgrid and INSTALLED onto the server !!!

from_email = Email("iamacookiedude@gmail.com")
to_email = Email("iamacookiedude@gmail.com")

subject = "AAAA"
content = Content("text/plain", "HI")

mail = Mail(from_email, subject, to_email, content)


with open('/Users/chrisj/Desktop/SLUH_Study/Hackathon/deeplearning.pdf','rb') as f:
    data = f.read()
    f.close()

encoded = base64.b64encode(data)

attachment = Attachment()
attachment.content(encoded)
attachment.type("application/pdf")
attachment.filename("deeplearning.pdf")
attachment.disposition("attachment")
attachment.content_id("NO.1")

mail2 = Mail(from_email, subject, to_email, content)
mail2.add_attachment(attachment)

response = sg.client.mail.send.post(request_body=mail.get())
response2 = sg.client.mail.send.post(request_body=mail2.get())

print(response.status_code)
print(response.body)
print(response.headers)

print(response2.status_code)
print(response2.body)
print(response2.headers)


