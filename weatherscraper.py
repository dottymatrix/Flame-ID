import requests
import json
import csv
# define the base URL of the API
base_url = 'https://wildfiresituation-api.nrs.gov.bc.ca/publicPublishedIncident?pageNumber=1&pageRowCount=20&stageOfControlList=OUT_CNTRL&stageOfControlList=HOLDING&stageOfControlList=UNDR_CNTRL&newFires=false&orderBy=lastUpdatedTimestamp%20DESC'
# define the number of rows per page
size = 20
# set the new fires flag to True or False depending on your preference
new_fires = True
# create an empty list to store the data
data = []
# set the initial page number to 1
page = 1
# loop through all the possible pages
while True:
    # define the parameters for the GET request
    params = {
        'pageNumber': page,
        'pageRowCount': size,
        'stageOfControlList': ['OUT_CNTRL', 'HOLDING', 'UNDR_CNTRL'],
        'newFires': new_fires,
        'orderBy': 'lastUpdatedTimestamp DESC'
    }
    # make a GET request to the API with the parameters
    response = requests.get(base_url, params=params)
    # parse the response as a JSON object
    json_data = json.loads(response.text)
    # get the total number of rows and pages from the JSON object
    total_rows = json_data['totalRowCount']
    total_pages = json_data['totalPageCount']
    # get the content of the JSON object, which is a list of wildfires
    content = json_data['collection']
    # append the content to the data list
    data.extend(content)
    # check if there are more pages to fetch
    if page < total_pages:
        # increment the page number by 1
        page += 1
    else:
        # break the loop if there are no more pages to fetch
        break

# open a file in write mode
with open('wildfire_data.json', 'w') as f:
    # dump the data list as a JSON string into the file
    json.dump(data, f)
