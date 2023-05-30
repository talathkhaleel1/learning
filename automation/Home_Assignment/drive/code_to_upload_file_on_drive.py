from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from googleapiclient.http import MediaFileUpload
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API     # it is from this part that we need to change and run the code
    # and use the Google Drive API and do multiple things
    # This is the part which interacts with Google Drive
    # results = service.files().list(
    #     pageSize=10, fields="nextPageToken, files(id, name)").execute()#service.files() creates an object which is able to read and write files on Google
    # items = results.get('files', [])# need to edit page size to the required number as per project, here 100
    #
    # if not items:
    #     print('No files found.')
    # else:
    #     print('Files:')
    #     for item in items:
    #         print(item)
    file_metadata = {"name": "highest_rated_authors.csv"}
    media = MediaFileUpload("highest_rated_authors.csv", mimetype="text/csv")
    service.files().create(body=file_metadata,
                           media_body=media).execute()

if __name__ == '__main__':
    main()
