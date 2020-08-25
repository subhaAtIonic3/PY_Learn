import smtplib
import getpass

smtp_object = smtplib.SMTP("smtp.gmail.com")
smtp_object.ehlo()
smtp_object.starttls()

email = getpass.getpass("Please enter your email => ")
app_password = getpass.getpass("Please provide your app password => ")

smtp_object.login(email, app_password)

from_address = email
to_address = email
subject = input("enter the subject => ")
body = input("enter the mail body => ")

msg = "Subject: "+subject+"\n"+body

smtp_object.sendmail(from_address, to_address, msg)
smtp_object.quit()
