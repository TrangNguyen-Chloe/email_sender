import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# go to this link, click allow
# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PuUVzFjSTPFtLtJLmNffhmtDZM7DMxGe_xhCCXTdOVf74ADjl2z8L-TVIkkcowztXfzK7IpWoT9uMPvIGSVGBsa5TcVg
#if error 534: https://accounts.google.com/DisplayUnlockCaptcha


#function to read name and email addresses of receiver
def read_contacts(file):
    names = []
    emails = []
    with open(file, mode='r', encoding='utf-8') as contact_file:
        for contact in contact_file:
            names.append(contact.split()[0])
            emails.append(contact.split()[1])
    return names, emails

# #function to read content content file
def read_content(file):
    with open(file, mode='r', encoding='utf-8') as content_file:
        file_content = content_file.read()
    return Template(file_content)

# #setup server
host = "smtp.gmail.com"
port = 587
sender = input("input sender's adress:\n")
password = input("Enter your password:\n")
subject = 'test message'

server = smtplib.SMTP(host=host, port=port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(sender, password)

names, emails = read_contacts('contacts.txt')
message_template = read_content('message.txt')
# print(names)
# #send email to each contact
for name, email in zip(names, emails):
    #create a message
    msg = MIMEMultipart()
    #add the right name to the message template
    message = message_template.substitute(NAME=name.title())

    #setup the parameters of each message
    msg['From'] = sender
    msg['To'] = email
    msg['Subject'] = subject

    #add the body
    msg.attach(MIMEText(message, 'html'))

    #send emails
    server.send_message(msg)

    del msg

