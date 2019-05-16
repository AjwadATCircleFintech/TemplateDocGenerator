import json



class Config(object):

    def __init__(self, JSON):
        self.filename = JSON
        self.
        self.temporary = json.load(open(JSON))

    def AddNewKey(self):



    def UpdateConfig(self):

        with open(self.filename, 'w') as json_file:
            json.dump(self.dictonary, json_file)
        json_file.close()

    def ConfigReset(self):

    def ConfigValidate(self):

configobj = Config('config.json')
print(configobj.dictonary['credentials'])