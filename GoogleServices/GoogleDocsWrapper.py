from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from  GoogleServices import ServiceParent

SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

ServiceConfiguration = {
        'ServiceName': 'Docs',
        'SCOPES': SCOPES,
        'API_NAME': 'docs',
        'Version': 'v1'
    }
Document_Id = '195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE'

class GoogleDocsWrapper(ServiceParent.ServiceParent):

    def __init__(self):
        super().__init__(ServiceName=ServiceConfiguration['ServiceName'],
                         SCOPES=ServiceConfiguration['SCOPES'],
                         API_NAME=ServiceConfiguration['API_NAME'],
                         Version=ServiceConfiguration['Version'])

    def ReadTitle(self,Document_Id):

        service = super().GenerateService()

        document = service.documents().get(documentId=Document_Id).execute()

        print('The title of the document is: {}'.format(document.get('title')))

DocService = GoogleDocsWrapper()

DocService.ReadTitle(Document_Id)