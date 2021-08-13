import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# go to this link, click allow
# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PuUVzFjSTPFtLtJLmNffhmtDZM7DMxGe_xhCCXTdOVf74ADjl2z8L-TVIkkcowztXfzK7IpWoT9uMPvIGSVGBsa5TcVg
#if error 534: https://accounts.google.com/DisplayUnlockCaptcha


def email_sender(recipients, message):
    #setup content
    host = "smtp.gmail.com"
    port = 587
    #fill here
    sender = "your email"
    password = "password"
    subject = 'email subject'

    #create a message
    msg = MIMEMultipart()
    #setup the parameters of each message
    msg['From'] = sender
    msg['To'] = (', ').join(recipients.split(','))
    msg['Subject'] = subject
    #add the body
    msg.attach(MIMEText(message, 'html'))

    #setup server
    server = smtplib.SMTP(host=host, port=port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    
    #send emails
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    #fill message and recipients
    message = """<html>
                <body>
                    <p>Hello, 
                    <br>How are you doing?<br>
                    <a href="https://www.youtube.com/">youtube</a> 
                    has great videos.
                    </p>
                </body>
                </html>
                """
    email_sender('onamispirit@gmail.com,ixoranguyen106@gmail.com', message)