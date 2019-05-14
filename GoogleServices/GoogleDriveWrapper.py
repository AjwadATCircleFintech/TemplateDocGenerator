from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from GoogleServices import  ServiceParent

SCOPES = ['https://www.googleapis.com/auth/drive']

ServiceConfiguration = {
        'ServiceName': 'Drive',
        'SCOPES': SCOPES,
        'API_NAME': 'drive',
        'Version': 'v3'
    }

class GoogleDriveService(ServiceParent.ServiceParent):



    def __init__(self):
        super().__init__(ServiceName=ServiceConfiguration['ServiceName'],
                         SCOPES=ServiceConfiguration['SCOPES'],
                         API_NAME=ServiceConfiguration['API_NAME'],
                         Version=ServiceConfiguration['Version'])

    def ShowList(self):
        service = super().GenerateService()

        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))

