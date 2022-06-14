from __future__ import print_function
#AIzaSyCz-ZaLelw6SzhwM5bWBZIz1da5UEweqTA
from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
# 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
SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('hip-girder-352015-3697566be8c0.json')
creds = None
#%%
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret_849078933505-m4ttob7o0tvh76mk0mberpjlsjo070mg.apps.googleusercontent.com.json', SCOPES)
    creds = tools.run_flow(flow, store)

form_service = discovery.build('forms', 'v1', http=creds.authorize(
    Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

# Request body for creating a form
NEW_FORM = {
    "info": {
        "title": "Quickstart form",
    }
}

# Request body to add a multiple-choice question
NEW_QUESTION = {
    "requests": [{
        "createItem": {
            "item": {
                "title": "Take a picture of the following image: ",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "1965"},
                            ],
                            "shuffle": True
                        }
                    }
                },
            },
            "location": {
                "index": 0
            }
        }
    }]
}

# Creates the initial form
result = form_service.forms().create(body=NEW_FORM).execute()

# Adds the question to the form
for _ in range(200):
    question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()

# Prints the result to show the question has been added
get_result = form_service.forms().get(formId=result["formId"]).execute()
print(get_result)