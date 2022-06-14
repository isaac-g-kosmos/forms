from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive']


def main():
    """Shows copy file example in Drive v3 API.
    Prints the name, id and other data of the copied file.
    """
    creds = None
    if os.path.exists('hip-girder-352015-3697566be8c0.json'):
        creds = Credentials.from_authorized_user_file('hip-girder-352015-3697566be8c0.json', SCOPES)
        print(creds.to_json())
        print('Valid credential')
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        # if False:
        if creds and creds.expired and creds.refresh_token:
            l=Request()
            print(l)
            creds.refresh(l)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_849078933505-m4ttob7o0tvh76mk0mberpjlsjo070mg.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('hip-girder-352015-3697566be8c0.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    origin_file_id = '1ox-6vHFeKpC6mon-tL5ygBC8zpbTnTp76JCZdIg80hA'  # example ID
    copied_file = {'title': 'my_copy'}
    results = service.files().copy(
        fileId=origin_file_id, body=copied_file).execute()
    print(results)


if __name__ == '__main__':
    main()