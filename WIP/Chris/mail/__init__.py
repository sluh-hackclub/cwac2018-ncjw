# SETUP PROCEDURES
# Update console commands:
# echo "export SENDGRID_API_KEY='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'" > sendgrid.env
# echo "sendgrid.env" >> .gitignore
# source ./sendgrid.env
# SendGrid Library (Github Site): https://github.com/sendgrid/sendgrid-python"""

import sendgrid
import os
from sendgrid.helpers.mail import *

# STATIC SECTION TRANSFERRED TO MAIL_MAIN.py
from MAIL_MAIN import *
# DYNAMIC SECTION

first_name = "John"
last_name = "Johnson"
address_1 = "2 Market St."
address_2 = "Saint Louis, MO 63110"
DATES=["1/2/14","1/4/15","4/11/16","5/7/20","5/3/4"]
ITEMS=["Sweater","Boots","Shirts","Jacket","Backpacks"]
PRICES=[60,30,30,45,34]
email_address ="test@test.com"

X = MAIL()
X.HTMLGen(first_name,last_name,address_1,address_2,DATES,ITEMS,PRICES)
X.PDFGen()
X.MAIL(email_address)
