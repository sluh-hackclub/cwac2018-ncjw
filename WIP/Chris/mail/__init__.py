# SETUP PROCEDURES
# Update console commands:
# echo "export SENDGRID_API_KEY='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'" > sendgrid.env
# echo "sendgrid.env" >> .gitignore
# source ./sendgrid.env
# SendGrid Library (Github Site): https://github.com/sendgrid/sendgrid-python"""

import base64
import sendgrid
import os
from sendgrid.helpers.mail import *
import urllib2
import os
import pdfkit
import datetime
import time

# STATIC SECTION
def HTMLGen(first_name,last_name,address_1,address_2,DATES,ITEMS,PRICES):
    S = '<html><head><style>* {font-family: helvetica;}table {border-collapse: collapse;width: 100%;}td, th {border: 1px solid #dddddd;text-align: left;padding: 1px;}tr:nth-child(even) {background-color: #dddddd;}</style></head><body><h1>Tax Return</h1><p>'
    S=S+datetime.date.today().strftime("%B")+' '+datetime.date.today().strftime("%d")+', '+datetime.date.today().strftime("%Y")+'</p><p>'+first_name+' '+last_name+'<br>'+address_1+'<br>'+address_2+'<br><br>Dear '+first_name+',<br>Thank you so much for supporting NCJW and The Resale Shop. Below is your receipt for the entire 2017 year.</p><table><tr><th>Date Recieved</th><th>Items</th><th>Values</th></tr>'
    total =0
    for i in range(0,len(DATES)):
        S=S+"<tr><th>"+DATES[i]+"</td><td>"+ITEMS[i]+"</td><td>$"+str(PRICES[i])+"</td></tr>"
        total=total+PRICES[i]
    S=S+'<tr><td>Total Value</td><td>$'+str(total)+'</td></tr></table><p>NCJW STL is recognized by the IRS as a 501 (c) 3 organization.Donations to The Resale Shop are tax deductible to the fullest extent allowed by law.Please consult your tax advisor for further information.IRS regulations require "fair market value"--the price we can sell your items; since we do not sell soiled or damaged items they cannot be included in our valuations.Your donation summary represents average resale pricing at The Resale Shop of the items you donated.It is reported to you at your request and may be used as your receipt for income tax purposes; however, you are under no obligation to use this statement in completing your tax return.The money earned from your donations helps us support our mission of improving the lives of women, children and families in our region through community service, education, philanthropy and advocacy.Your support is critical to our success and we thank you! Best Regards,</p><br><br><input type="submit" value="Continue"></body></html>'

    f =open('/Users/chrisj/Desktop/SLUH_Study/Hackathon/mail/SAMPLE.html','w')
    f.write(S)
    f.close()

def PDFGen():
    options = {
        'zoom': '3.00'
    }
    pdfkit.from_file('/Users/chrisj/Desktop/SLUH_Study/Hackathon/mail/SAMPLE.html', '/Users/chrisj/Desktop/SLUH_Study/Hackathon/mail/OUTPUT.pdf',options=options)

def MAIL(email_address):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

    from_email = Email("test@test.com")
    subject = "The Resale Shop : Tax Return Receipt"
    to_email = Email(email_address)
    content = Content("text/html", "Thank you so much for supporting NCJW and The Resale Shop. Below is your receipt for the entire 2017 year.")

    file_path = "/Users/chrisj/Desktop/SLUH_Study/Hackathon/mail/OUTPUT.pdf"
    with open(file_path,'rb') as f:
        data = f.read()
        f.close()
    encoded = base64.b64encode(data).decode()

    attachment = Attachment()
    attachment.content = encoded
    attachment.type = "application/pdf"
    attachment.filename = "Tax Return Receipt.pdf"
    attachment.disposition = "attachment"
    attachment.content_id = "ID"

    mail = Mail(from_email, subject, to_email, content)
    mail.add_attachment(attachment)
    try:
        response = sg.client.mail.send.post(request_body=mail.get())
    except urllib2.HTTPError as e:
        print(e.read())
        exit()
    print(response.status_code)
    print(response.body)
    print(response.headers)

# DYNAMIC SECTION
first_name = "John"
last_name = "Johnson"
address_1 = "2 Market St."
address_2 = "Saint Louis, MO 63110"
DATES=["1/2/14","1/4/15","4/11/16","5/7/20","5/3/4"]
ITEMS=["Sweater","Boots","Shirts","Jacket","Backpacks"]
PRICES=[60,30,30,45,34]
email_address ="test@test.com"

HTMLGen(first_name,last_name,address_1,address_2,DATES,ITEMS,PRICES);
PDFGen();
MAIL(email_address);
