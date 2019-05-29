import re
import json
from pprint import pprint

#TODO: We shall be fixing majority of the functions in this

RegexParams = [":Title:",":URL:",":Method:",":Param_Request:",":Return:",":Return_Status:"]
JSON_VERBS = ['API_TITLE', 'URL_STRING', 'HTTP_VERB', 'REQUEST_PARAMS', 'RETURN_DATA', 'RETURN_STATUS']

API_DOCSTRING = """
:Title: Dist List
:URL: /api/v2/beftn/route/bank/dist-name/list/
:Method: GET
:Param_request: { "bank_name": "AGRANI BANK LTD." }
:Return: {
   "data": [
       {
           "dist_name": "GAZIPUR"
       },
       {
           "dist_name": "NAWABGANJ"
       },
   ],
   "success_code": "BEFTNDL2001"
}

:Return_Status:
BEFTN_DIST_LIST_CODE = _("BEFTNDL2001")
BEFTN_KEY_ERROR_CODE = _("BEFTKE4001")


"""
TEST_DOCSTRING = """

:Title: Dist List
:URL: /api/v2/beftn/route/bank/dist-name/list/
:Method: GET
:Param_Request: { "bank_name": "Dist BANK LTD." }
:Return: {
   "data": [
       {
           "dist_name": "GAZIPUR"
       },
       {
           "dist_name": "NAWABGANJ"
       },
   ],
   "success_code": "BEFTNDL2001"
}

:Return_Status:
BEFTN_DIST_LIST_CODE = _("BEFTNDL2001")
BEFTN_KEY_ERROR_CODE = _("BEFTKE4001")
BEFTN_KEY_ERROR_CODE = _("BEFTKE1001")



:Title: Another List
:URL: /api/v2/beftn/route/bank/dist-name/Anotherlist/
:Method: GET
:Param_Request: { "bank_name": "Another BANK LTD." }
:Return: {
   "data": [
       {
           "dist_name": "Faridpur"
       },
       {
           "dist_name": "GANJ"
       },
   ],
   "success_code": "BEFTNDL3101"
}

:Return_Status:
BEFTN_DIST_LIST_CODE = _("BEFTNDL3101")
BEFTN_KEY_ERROR_CODE = _("BEFTKE5001")




:Title: BEFTN LIST
:URL: /api/v2/beftn/route/bank/dist-name/BEFTNlist/
:Method: GET
:Param_Request: { "bank_name": "BEFTN BANK LTD." }
:Return: {
   "data": [
       {
           "dist_name": "GAZIPUR"
       }
   ],
   "success_code": "BEFTNDL8001"
}

:Return_Status:
BEFTN_DIST_LIST_CODE = _("BEFTNDL6001")
BEFTN_KEY_ERROR_CODE = _("BEFTKE8001")
BEFTN_KEY_ERROR_CODE = _("BEFTKJ9001")





:Title: Cred List
:URL: /api/v2/beftn/route/bank/dist-name/Credlist/
:Method: GET
:Param_Request: { "bank_name": "CRED BANK LTD." }
:Return: {
   "data": [
       {
           "dist_name": "PURIPUR"
       },
       {
           "dist_name": "NAWABGANJ"
       },
   ],
   "success_code": "TLDR2001"
}

:Return_Status:
BEFTN_DIST_LIST_CODE = _("ABCTNDL3001")
BEFTN_KEY_ERROR_CODE = _("TKEDNF1001")




"""

def RemoveNewLine(String):

    return String.replace("\n","")

def GenerateUniqueList(ParameterList):

    return list(dict.fromkeys(ParameterList))

def FindParameters(String):

    #bracketpattern = re.compile("(:Title:(.*?):URL:)")
    Pattern = re.compile(":\w+:")
    stringz = Pattern.findall(String)

    return stringz

def FindPattern(String,Pattern):

    pattern = re.compile(Pattern)

    return pattern.findall(String)

def FindParamValues(DocString):

    Params = [":Title:",":URL:",":Method:",":Param_Request:",":Return:",":Return_Status:"]
    DocString = RemoveNewLine(DocString)
    ReturnDic = {}
    for i in range(len(Params)):
        if i + 1 < len(Params):
            pattern = re.compile(Params[i] + "(.*?)" + Params[i + 1])
            ReturnDic[Params[i]]= pattern.findall(DocString)
        else:
            pattern = re.compile(Params[i]+"(.*?)([)]\W|[)]$)")
            ReturnDic[Params[i]] = pattern.findall(DocString)


    return zip(ReturnDic[":Title:"],ReturnDic[":URL:"],ReturnDic[":Method:"],ReturnDic[":Param_Request:"],\
               ReturnDic[":Return:"],ReturnDic[":Return_Status:"])

def GenerateJSON(ParsedDic):

    JsonList = []

    for item in ParsedDic:
        Jsondic ={}
        for i in range(len(JSON_VERBS)):
            Jsondic[JSON_VERBS[i]] = item[i]
        JsonList.append(json.dumps(Jsondic))

    return JsonList

def Validate(String):

    return 0




pattern = re.compile(":\w+:")
print(pattern.findall(TEST_DOCSTRING))
# for elements in GenerateJSON(ValueList):
#  print(elements)
#  print("\n")















