from jinja2 import Environment, FileSystemLoader,PackageLoader, select_autoescape
from PDFConverter import convertHtmlToPdf
import json
from GoogleDriveWrapper import BuildService
from googleapiclient.discovery import MediaFileUpload


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
Template_JSON =[{
        "API_Title": "Credit Card Search By Connect Id",
        "URL_STRING": "/api/v1/jbl/credit-card/account/list/<connect_id>/",
        "HTTP_VERB": "GET",
        "RESPONSE_BODY": {
            "credit_card": [
                {
                    "credit_card_number": "4661054614652927",
                    "utility_name": "credit_card_bill_pay",
                    "last_used_at": "2019-04-08T10:32:46.437401Z",
                    "is_deleted": "false",
                    "is_active": "true"
                }
            ],
            "success_code": "JBLADF2003"
        }

    } , {

    "API_Title": "Bank List",
    "URL_STRING": "/api/v2/beftn/route/bank/list/",
    "HTTP_VERB": "GET",
    "RESPONSE_BODY": {
           "data": [
               {
                   "bank_name": "AGRANI BANK LTD."
               },
               {
                   "bank_name": "STANDARD CHARTERED BANK"
               },
           ],
           "success_code": "BEFTNBL2001"
       }


}, {

    "API_Title": "Route List All",
    "URL_STRING": "/api/v2/beftn/route/list/",
    "HTTP_VERB": "GET",
    "RESPONSE_BODY": {
        "data": [
            {
                "branch_name": "BAKTARPUR",
                "routing_number": "010330207"
            }
            ],
                "success_code": "BEFTNBRL2001"
        }


}, {

    "API_Title": "Route List",
    "URL_STRING": "/api/v2/beftn/route/list/",
    "HTTP_VERB": "POST",
    "RESPONSE_BODY":  {
        "data": [
            {
                 "branch_name": "BAKTARPUR",
                 "routing_number": "010330207"
            }
        ],
        "success_code": "BEFTNBRL2002"
    }


},{

    "API_Title": "Member List",
    "URL_STRING": "/api/v2/beftn/member/",
    "HTTP_VERB": "GET",
    "RESPONSE_BODY": {
   "data": [
       {
           "id": 3,
           "alias": "Mr. YEXX",
           "receiver_name": "Mr. YEXX",
           "receiver_bank_account": "0006-123456788",
           "routing_number": "null"
       },
       {
           "id": 2,
           "alias": "Mr. YEX",
           "receiver_name": "Mr. YEX",
           "receiver_bank_account": "0006-123456779",
           "routing_number": "130272324"
       }
   ],
   "success_code": "BEFTNBL2001"
}


}]
template = env.get_template('Basic_Template.html')

print(json.dumps(Template_JSON[0]["RESPONSE_BODY"],indent=4, sort_keys=True))

api_endpoints = [{
    "name": Template_JSON[0]["API_Title"],
    "url":Template_JSON[0]["URL_STRING"],
    "verb":Template_JSON[0]["HTTP_VERB"],
    "codeblock":json.dumps(Template_JSON[0]["RESPONSE_BODY"],indent=4, sort_keys=True)
}, {
    "name": Template_JSON[1]["API_Title"],
    "url": Template_JSON[1]["URL_STRING"],
    "verb":Template_JSON[1]["HTTP_VERB"],
    "codeblock":json.dumps(Template_JSON[1]["RESPONSE_BODY"],indent=4, sort_keys=True)
}, {
    "name": Template_JSON[2]["API_Title"],
    "url": Template_JSON[2]["URL_STRING"],
    "verb":Template_JSON[2]["HTTP_VERB"],
    "codeblock":json.dumps(Template_JSON[2]["RESPONSE_BODY"],indent=4, sort_keys=True)
}, {
    "name":Template_JSON[3]["API_Title"],
    "url":Template_JSON[3]["URL_STRING"],
    "verb":Template_JSON[3]["HTTP_VERB"],
    "codeblock":json.dumps(Template_JSON[3]["RESPONSE_BODY"],indent=4, sort_keys=True)

}, {
    "name":Template_JSON[4]["API_Title"],
    "url":Template_JSON[4]["URL_STRING"],
    "verb":Template_JSON[4]["HTTP_VERB"],
    "codeblock":json.dumps(Template_JSON[4]["RESPONSE_BODY"],indent=4, sort_keys=True)

}]


rendered_template = template.render(Doc={'title': 'Generated Documentation Example'}, endpointlist=api_endpoints)
print(rendered_template)
with open("some_new_file4.html", "w") as f:
    f.write(rendered_template)
f.close()

body = {'name': 'GeneratedDocumentation', 'mimeType': 'application/vnd.google-apps.document'}
DriveService = BuildService()

media = MediaFileUpload("some_new_file4.html", mimetype='text/html')
DocService = DriveService.files().create(body=body,media_body=media,fields='id').execute()

# media = MediaFileUpload("C:\\Users\\Circle\\Desktop\\Test_Template_doc.docx", mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
# DocService = DriveService.files().create(body=body,media_body=media,fields='id').execute()

print(DocService)