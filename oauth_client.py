# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Gmail API - authentication module
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

import os # Miscellaneous operating system interfaces
from dotenv import dotenv_values # to read .env file for private data
import pickle # Python object serialization

# Gmail API utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Request all access (permission to read/send/receive emails, manage the inbox, and more)
SCOPES = ['https://mail.google.com/']

config = dotenv_values(".env.secret")
test_sending_address = config.get('DEVELOPER_EMAIL_ADDRESS')
test_user_address = config.get('TEST_USER_ADDRESS')

def authenticate_oauth_gmail() :
    creds = None
    try :
        if os.path.exists("token.pickle") :
            # open for binary reading. This file is created at first run.
            with open("token.pickle", "rb") as token :
                creds = pickle.load(token)
    except OSError as e:
        print(e.message)
    except pickle.PickleError as e:
        print(e.message)
    try :
        if not creds or not creds.valid:
            # make a new request if the credentials are expired, invalid or not present
            if creds and creds.expired and creds.refresh_token :
                creds.refresh(Request())
            else :
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                # run_local_server uses a default host of localhost for the redirect_uri,
                # which is fine when you run the project locally but won't work once your project is deployed.
                # ref: https://developers.google.com/identity/protocols/oauth2/web-server#python_1
                # from: https://github.com/googleapis/google-api-python-client/issues/755
                creds = flow.run_local_server(port=0)
            with open("token.pickle", "wb") as token :
                pickle.dump(creds, token)
    except :
        print("Something went wrong when fetching credentials")
    return build('gmail', 'v1', credentials=creds)

# get the Gmail API service
# gmail_client = authenticate_oauth_gmail()