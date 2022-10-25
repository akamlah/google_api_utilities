# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Gmail API - send emails
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# module in this utility kit responsible for establishing connection to google api
import oauth_client

# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode

# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type

def build_message(sender, to, subject, body, attachments = []):
    if not attachments: # no attachments given
        message = MIMEText(body)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
    else:
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        message.attach(MIMEText(body))
        for filename in attachments:
            add_attachment(message, filename)
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(gmail_client, sender, to, subject, body, attachments = []) :
    return gmail_client.users().messages().send(
        userId = "me",
        body=build_message(sender, to, subject, body, attachments)
    ).execute()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# test

from dotenv import dotenv_values

if __name__ == "__main__":

    config = dotenv_values(".env.secret")
    test_user_address = config.get('TEST_USER_ADDRESS')
    test_sending_address = config.get('DEVELOPER_EMAIL_ADDRESS')

    send_message(
        oauth_client.authenticate_oauth_gmail(),
        test_sending_address,
        test_user_address,
        "my msg",
        "hi there 4"
    )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
