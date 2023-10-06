import requests
import json

# define the URL of the API
url = 'https://wildfiresituation-api.nrs.gov.bc.ca/publicPublishedIncident?pageNumber=1&pageRowCount=20&stageOfControlList=OUT_CNTRL&stageOfControlList=HOLDING&stageOfControlList=UNDR_CNTRL&newFires=false&orderBy=lastUpdatedTimestamp%20DESC'

# make a GET request to the API
response = requests.get(url)

# parse the response as a JSON object
json_data = json.loads(response.text)

# print the JSON objects or keys for the url
print(json_data.keys())