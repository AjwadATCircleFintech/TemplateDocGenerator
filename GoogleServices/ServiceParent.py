from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def loadConfig():

    with open('config.json') as config:
        VariableName = json.load(config)
    config.close()
    return VariableName
 
def UpdateConfig(dictionary):

    with open('config.json', 'w') as json_file:
        json.dump(dictionary, json_file)
    json_file.close()

class BuildCredential(object):

    def __init__(self, ServiceName, Scopes):
        self.ServiceName = ServiceName
        self.SCOPES = Scopes

    def CheckServiceName(self):

        APPLICATION_VARIABLES = loadConfig()
        if self.ServiceName in APPLICATION_VARIABLES.keys():
            return True
        else:
            return False

    def GeneratePickleFile(self):

        APPLICATION_VARIABLES = loadConfig()
        APPLICATION_VARIABLES[self.ServiceName] = self.ServiceName + ".pickle"
        UpdateConfig(APPLICATION_VARIABLES)

    def FindPickleFile(self):

        APPLICATION_VARIABLES = loadConfig()

        return APPLICATION_VARIABLES[self.ServiceName]

    def GenerateCred(self):

        creds = None
        APPLICATION_VARIABLES = loadConfig()
        Credentials = APPLICATION_VARIABLES['credentials']

        if not self.CheckServiceName():
            self.GeneratePickleFile()

        picklefile = self.FindPickleFile()

        if os.path.exists(picklefile):
            with open(picklefile, 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    Credentials, self.SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open(picklefile, 'wb') as token:
                pickle.dump(creds, token)

        return creds

class ServiceParent(BuildCredential):

    def __init__(self, SCOPES, ServiceName, API_NAME, Version ):
        super().__init__(ServiceName,SCOPES)
        self.API_NAME = API_NAME
        self.Version = Version

    def GenerateService(self):

        Credentials = super().GenerateCred()
        return build(self.API_NAME, self.Version, credentials=Credentials)






# def BuildService():
#     """Shows basic usage of the Drive v3 API.
#     Prints the names and ids of the first 10 files the user has access to.
#     """
#     creds = None
#     # The file token.pickle stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server()
#         # Save the credentials for the next run
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#
#     service = build('drive', 'v3', credentials=creds)
#
#     return service

