from docxtpl import DocxTemplate
import json
from googleapiclient.discovery import build,MediaFileUpload
from GoogleDriveWrapper import BuildService

doc = DocxTemplate("C:\\Users\\Circle\\PycharmProjects\\TemplateDocsGenerator\\templates\\template.docx")
Template_JSON ={
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

    }
context = {"endpointlist": [{

    "name": "Test Endpoint 1",
    "url": "/app/test/endpoint1",
    "verb": "GET",
    "codeblock": "{"
                 "  'error_code':'beftn4009'"
                 "}"
},
    {

        "name": "Test Endpoint 2",
        "url": "/app/test/endpoint2",
        "verb": "GET",
        "codeblock": "Test Outside <pre><h1>Test</h1></pre>"
        # "codeblock": json.dumps(Template_JSON, indent=4, sort_keys=True))
},
    {
        "name": "Test Endpoint 3",
        "url": "/app/test/endpoint3",
        "verb": "POST",
        "codeblock": "{"
                     "  'error_code':'beftn5009'"
                     "  'error_code':'beftn5009'"
                     "  'error_code':'beftn5009'"
                     "  'error_code':'beftn5009'"
                     "  'error_code':'beftn5009'"
                     "  'error_code':'beftn5009'"
                     "  'error_code':'beftn5009'"
                     "  'error_code':'beftn5009'"
                     "  'error_code':'beftn5009'"
                     "  'error_code':'beftn5009'"
                     "  'error_code':'beftn5009'"
                     "  'error_code':'beftn5009'"
                     "}"
}
]}
doc.render(context)
doc.save("generated_doc.docx")

body = {'name': 'TestDocX', 'mimeType': 'application/vnd.google-apps.document'}
DriveService = BuildService()

media = MediaFileUpload("generated_doc.docx", mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
DocService = DriveService.files().create(body=body,media_body=media,fields='id').execute()