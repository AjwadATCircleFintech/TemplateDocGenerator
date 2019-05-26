import re

BASIC_DOCSTRING = ""
API_DOCSTRING = """
:Title: Dist List
:URL: /api/v2/beftn/route/bank/dist-name/list/
:Method: GET
:param_request: { "bank_name": "AGRANI BANK LTD." }
:return: {
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
TEST_APISTRING = """

:Title: Dist List
:URL: /api/v2/beftn/route/bank/dist-name/list/
:Method: GET
:param_request: { "bank_name": "Dist BANK LTD." }
:return: {
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

:Title: Another List
:URL: /api/v2/beftn/route/bank/dist-name/Anotherlist/
:Method: GET
:param_request: { "bank_name": "Another BANK LTD." }
:return: {
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
:param_request: { "bank_name": "BEFTN BANK LTD." }
:return: {
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

:Title: Cred List
:URL: /api/v2/beftn/route/bank/dist-name/Credlist/
:Method: GET
:param_request: { "bank_name": "CRED BANK LTD." }
:return: {
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

TEST_APISTRING = TEST_APISTRING.replace("\n","")

API_DOCSTRING = API_DOCSTRING.replace("\n","")
bracketpattern = re.compile("(:Title:(.*?):URL:)")
Pattern = re.compile(":\w+:")
stringz = Pattern.findall(TEST_APISTRING)
print(stringz)
#TODO figure out the loop and we should more or less get every data of interest
for i in range(len(stringz)):
    if i+1<len(stringz):
        pattern = re.compile(stringz[i]+"(.*?)"+stringz[i+1])
        for elements in pattern.findall(TEST_APISTRING):
            print(elements)
    else:
        pattern = re.compile(stringz[i]+"(.*?)[)]$")
        for elements in pattern.findall(TEST_APISTRING):
            print(elements)
# for elements in stringz:
#     subpattern = re.compile(elements+"(.*?)\n")
#     Foundstring = subpattern.findall(API_DOCSTRING)
#     print(Foundstring)
    # Pattern = re.compile(elements)
    # print(Pattern.findall(API_DOCSTRING))
# API_DOCSTRING = API_DOCSTRING.replace('\n','')
# Pattern = re.compile(":\w+:")
# stringz = Pattern.findall(API_DOCSTRING)
# split = re.split(":\w+:",API_DOCSTRING)
# print(len(stringz))
# print(len(split))
# print(split)



# keydictionary=dict(zip(Pattern.findall(API_DOCSTRING), re.split("(:\w+:)",API_DOCSTRING)))
# print(keydictionary)