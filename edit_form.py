# 1VGR-5coWsaqm22o3d6F7ppvWqeBv_rJK-i_Lk00VQtQ
from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('token.json')
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
    creds = tools.run_flow(flow, store)

form_service = discovery.build('forms', 'v1', http=creds.authorize(
    Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

form = {
    "info": {
        "title": "Update metadata example for Forms API!",
    }
}

# Creates the initial Form
createResult = form_service.forms().create(body=form).execute()

# Request body to add description to a Form
update = {
    "requests": [{
        "updateItem": {
                        {
                          "item": {
                              {  "itemId": string,
                                  "title": string,
                                  "description": string,

                                  # Union field kind can be only one of the following:
                                  "questionItem": {
                                      {
                                          "question": {


                                          {
                                              "questionId": 1,
                                              "required": True,

                                          }
                                      }
                                  }

                              }
                          },
                          "location": {
                            object (Location)
                          },
                          "updateMask": string
                        }

        }
    }]
}

# Update the form with a description
question_setting = form_service.forms().batchUpdate(
    formId=createResult["formId"], body=update).execute()

# Print the result to see it now has a description
getresult = form_service.forms().get(formId=createResult["formId"]).execute()
print(getresult)