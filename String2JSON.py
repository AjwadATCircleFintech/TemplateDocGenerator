import re

API_DOCSTRING = """
Title: Dist List
URL: /api/v2/beftn/route/bank/dist-name/list/
Method: GET
:param request: { "bank_name": "AGRANI BANK LTD." }
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

Return Status:
BEFTN_DIST_LIST_CODE = _("BEFTNDL2001")
BEFTN_KEY_ERROR_CODE = _("BEFTKE4001")


"""
Pattern = re.compile(":")

print(Pattern.search(API_DOCSTRING))
#print(API_DOCSTRING)