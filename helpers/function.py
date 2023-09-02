import os
import smtplib
from email.mime.text import MIMEText
from email.utils import make_msgid, formatdate


def sendmail():
    # No usage found for this function
    try:
        # Create your SMTP session
        smtp = smtplib.SMTP('mail.game-energy.de', 587)

        # Use TLS to add security
        smtp.starttls()

        # User Authentication
        smtp.login("no-reply@max1021.de", os.getenv("MAIL_PASSWORD"))

        # Define the Message
        msg = MIMEText('Hallo ')
        msg['Subject'] = 'Game-Energy - Dein Server wurde gesperrt!'
        msg['From'] = 'no-reply@max1021.de'
        msg['To'] = 'Game-Energy@gmx.de'
        msg['Message-ID'] = make_msgid()
        msg['Date'] = formatdate(localtime=True)

        sender = 'no-reply@max1021.de'
        receivers = ['Game-Energy@gmx.de']

        # Sending the Email
        smtp.sendmail(sender, receivers, msg.as_string())

        # Terminating the session
        smtp.quit()
        print("Email sent successfully!")

    except Exception as ex:
        print("Something went wrong....", ex)


