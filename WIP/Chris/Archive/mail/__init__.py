# Update console commands:
# echo "export SENDGRID_API_KEY='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'" > sendgrid.env
# echo "sendgrid.env" >> .gitignore
# source ./sendgrid.env
# SendGrid Library (Github Site): https://github.com/sendgrid/sendgrid-python"""

import base64
import sendgrid
import os
from sendgrid.helpers.mail import *
#
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
#
from_email = Email("iamacookiedude@gmail.com")
subject = "AAAA"
to_email = Email("iamacookiedude@gmail.com")
content = Content("text/html", "THIS IS AN ATTACHMENT")
#
file_path = "/Users/chrisj/Desktop/SLUH_Study/Hackathon/deeplearning.pdf"
with open(file_path,'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()
#
attachment = Attachment()
attachment.content = encoded
attachment.type = "application/pdf"
attachment.filename = "test.pdf"
attachment.disposition = "attachment"
attachment.content_id = "ID"
#
mail = Mail(from_email, subject, to_email, content)
mail.add_attachment(attachment)
try:
    response = sg.client.mail.send.post(request_body=mail.get())
except urllib.HTTPError as e:
    print(e.read())
    exit()
#
print(response.status_code)
print(response.body)
print(response.headers)

