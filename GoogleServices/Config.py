import json
import os, sys
Google_KEY_VALUE = "GoogleCredentials"
#TODO added tests and exceptions, here we want to make sure we arent accidentally changing anything important in the env
#TODO once core logic is done next  is thinking about errors and shit. While we are adding tests as an after thought tdd
#TODO might have said us a lot of time


default_config = {

    "credentials": ""

}
#First we need the process to check for a config file, In case it Can't find one we make one, using the same format as
#default, question is where the hell do we store it? maybe objects arent the best solution or approach here? Maybe we
#can make like bunch of static methods and avoid the other issues
#The fundamental issue we have is the chicken and egg problem. Do we have users predefine a config,json at a specific path
#or do we store them somewhere, cause our biggest question is okay where? I mean we can't store it at env we would need to
#set it every time, we are using config.json but then we have to know where the file is or all of this falls apart
#One idea is create bunch of method for creating and maintaining

def loadConfig():

    with open('config.json') as config:
        VariableName = json.load(config)
    config.close()
    return VariableName

def UpdateConfig(dictionary):

    with open('config.json', 'w') as json_file:
        json.dump(dictionary, json_file)
    json_file.close()

def GenerateConfig(dictionary):


    return 0


class Configs(object):

    def __init__(self,KEY_VALUE):
        self.KEY_VALUE = KEY_VALUE

    def ReturnKey(self):
        return self.KEY_VALUE

    def CheckKey(self):

        if self.KEY_VALUE in os.environ:
            return True
        else:
            return False

    def CheckValue(self):

        if os.environ[self.KEY_VALUE] is None:
            return False
        else:
            return True

    def SetKeyValue(self,value):

        os.putenv(self.KEY_VALUE,value)

    def ReturnKeyValue(self):

        return os.environ[self.KEY_VALUE]
        # if self.CheckKey():
        #     return os.environ[self.KEY_VALUE]
        # else:
        #     return None


class Credentials(Config):
#todo we can start using the classes to deal with case specific errors
#todo in case of credentials make sure that the
        def __init__(self):
            super().__init__(KEY_VALUE=Google_KEY_VALUE)

        def CheckPathValue(self):
            return 0 # We will use this later to check for correct path format etc

CredentialsObj = Credentials()
CredentialsObj.SetKeyValue("C:\\Users\\Circle\\PycharmProjects\\TemplateDocsGenerator\\GoogleServices\\Credentials\\credentials.json")
print(CredentialsObj.ReturnKeyValue())


# class Error(Exception): pass
#
# def _find(path, matchFunc=os.path.isfile):
#     for dirname in sys.path:
#         candidate = os.path.join(dirname, path)
#         if matchFunc(candidate):
#             return candidate
#     raise Error("Can't find file %s" % path)
#
# def find(path):
#     return _find(path)
#
# def findDir(path):
#     return _find(path, matchFunc=os.path.isdir)