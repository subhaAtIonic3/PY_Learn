import imaplib
import getpass
import email

M = imaplib.IMAP4_SSL("imap.gmail.com")

email = getpass.getpass("Please enter your email => ")
app_password = getpass.getpass("Please provide your app password => ")

M.login(email, app_password)
print(M.list())

M.select("inbox")

typ, data = M.search(None, 'SUBJECT "Python workout"')
print(typ)
print(data)

email_id = data[0]
res, email_data = M.fetch(email_id, "(RFC822)")

raw_email = email_data[0][1]
raw_email_string = raw_email.decode("utf-8")

print(raw_email_string)

# email_body = email.message_from_string(raw_email_string)

# for part in email_body.walk():
#     if part.get_content_type == "text/html":
#         actual_email_msg = part.get_payload(decode=True)
#         print(actual_email_msg)
