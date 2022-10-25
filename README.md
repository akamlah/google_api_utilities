# Google gmail API utilities
Utilities to send, recieve and mark emails with Google API

## Usage

### Dependencies

You can opt to create a virtual environment to download the dependencies into:
```python3 -m vevnv env```  

* python version 3 or above  
* google-api-python-client, google-auth-httplib2, google-auth-oauthlib:  
    ```pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```
* [python dotenv](https://pypi.org/project/python-dotenv/) for extracting data from a ```.env``` file:  
    ```pip3 install --upgrade python-dotenv```

### Required: Enable Gmail API.  

You need to enable Gmail API with your developer address, to create a client to use for the functionalities in this utility kit.

* Go to [Google API's Dashboard](https://console.cloud.google.com/apis/dashboard)
* Serch for Gmail API in the searchbar and enable it
* Hit the Create Credentialsbutton to create an OAuth 2.0 client ID and Select "User data" to create an OAuth Client
* Select Desktop Application as type.
* Download .json of the credentials

Note: If this is the first time you use Google APIs, you may need to simply create an OAuth Consent screen and add your email as a testing user.

Then create a ```.env.secret``` file at the root of the directory and write following line:  
```DEVELOPER_EMAIL_ADDRESS = <your address>```   
Add this file to your .gitignore and don't publish sensitive data.   