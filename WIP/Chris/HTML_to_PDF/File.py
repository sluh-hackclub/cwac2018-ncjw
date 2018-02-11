import os
import pdfkit
import datetime
import time
# DYNAMIC SECTION
first_name = "JOHN"
last_name = "SHIT"
address_1 = "2 Shiter St."
address_2 = "Saint Louis, MO 63110"
DATES=["1/2/14","1/4/15","4/11/16","5/7/20","5/3/4"]
ITEMS=["Sweater","Boots","Shirts","Jacket","ITEM"]
PRICES=[6000,300,301400,4503,2345]
email_address ="iamacookiedude@gmail.com"

# END OF DYNAMIC SECTION
S = '<html><head><style>* {font-family: helvetica;}table {border-collapse: collapse;width: 100%;}td, th {border: 1px solid #dddddd;text-align: left;padding: 1px;}tr:nth-child(even) {background-color: #dddddd;}</style></head><body><h1>Tax Return</h1><p>'

S=S+datetime.date.today().strftime("%B")+' '+datetime.date.today().strftime("%d")+', '+datetime.date.today().strftime("%Y")+'</p><p>'+first_name+' '+last_name+'<br>'+address_1+'<br>'+address_2+'<br><br>Dear '+first_name+',<br>Thank you so much for supporting NCJW and The Resale Shop. Below is your receipt for the entire 2017 year.</p><table><tr><th>Date Recieved</th><th>Items</th><th>Values</th></tr>'
total =0

for i in range(0,len(DATES)):
    S=S+"<tr><th>"+DATES[i]+"</td><td>"+ITEMS[i]+"</td><td>$"+str(PRICES[i])+"</td></tr>"
    total=total+PRICES[i]
S=S+'<tr><td>Total Value</td><td>$'+str(total)+'</td></tr></table><p>NCJW STL is recognized by the IRS as a 501 (c) 3 organization.Donations to The Resale Shop are tax deductible to the fullest extent allowed by law.Please consult your tax advisor for further information.IRS regulations require "fair market value"--the price we can sell your items; since we do not sell soiled or damaged items they cannot be included in our valuations.Your donation summary represents average resale pricing at The Resale Shop of the items you donated.It is reported to you at your request and may be used as your receipt for income tax purposes; however, you are under no obligation to use this statement in completing your tax return.The money earned from your donations helps us support our mission of improving the lives of women, children and families in our region through community service, education, philanthropy and advocacy.Your support is critical to our success and we thank you! Best Regards,</p><br><br><input type="submit" value="Continue"></body></html>'

f =open('/Users/chrisj/Desktop/SLUH_Study/Hackathon/HTML_to_PDF/SAMPLE.html','w')
f.write(S)
f.close()

options = {
    'zoom': '3.00'
}

pdfkit.from_file('/Users/chrisj/Desktop/SLUH_Study/Hackathon/HTML_to_PDF/SAMPLE.html', '/Users/chrisj/Desktop/SLUH_Study/Hackathon/HTML_to_PDF/OUTPUT.pdf',options=options)
