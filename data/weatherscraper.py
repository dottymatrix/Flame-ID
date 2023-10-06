import requests
import json
import csv
import datetime
import pandas as pd

# define the base URL of the API
base_url = 'https://wildfiresituation-api.nrs.gov.bc.ca/publicPublishedIncident?pageNumber=1&pageRowCount=20&stageOfControlList=OUT_CNTRL&stageOfControlList=HOLDING&stageOfControlList=UNDR_CNTRL&newFires=false&orderBy=lastUpdatedTimestamp%20DESC'
# define the number of rows per page
size = 20
# set the new fires flag to True or False depending on your preference
new_fires = False
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

# read the JSON data from a file
df = pd.read_json('wildfire_data.json')
# select the columns that contain the key wildfire information
df = df[['incidentNumberLabel', 'incidentLocation', 'incidentSizeEstimatedHa', 'stageOfControlCode', 'lastUpdatedTimestamp', 'incidentNumberLabel', 'incidentName', 'incidentSizeDetail', 'incidentCauseDetail']]
# write the dataframe to a CSV file
df.to_csv('wildfire_data.csv', index=False)

# open the JSON file in read mode
with open('wildfire_data.json', 'r') as f:
    # load the JSON data as a Python object
    data = json.load(f)

# open the csv file in write mode
with open('wildfire_data.csv', 'w', newline='') as f:
    # create a writer object
    writer = csv.writer(f)
    # write the header row
    writer.writerow(['lastUpdatedTimestamp', 'incidentLocation', 'fireCentreName', 'incidentSizeEstimatedHa', 'stageOfControlCode', 'incidentNumberLabel', 'incidentName', 'incidentSizeDetail', 'incidentCauseDetail'])
    # iterate through each wildfire in the data
    for wildfire in data:
        # get the milliseconds from the 'lastUpdatedTimestamp'
        milliseconds = wildfire['lastUpdatedTimestamp']
        # check if milliseconds is not None
        if milliseconds is not None:
            # divide the milliseconds by 1000 to get the seconds
            seconds = milliseconds / 1000
            # create a datetime object from the seconds
            dt = datetime.datetime.fromtimestamp(seconds)
            # format the datetime object as hh:mm:ss
            time = dt.strftime('%H:%M:%S, %b %d %Y')
            print(time)
            # replace the 'lastUpdatedTimestamp' with the time
            wildfire['lastUpdatedTimestamp'] = time
        # write the wildfire data as a row to the csv file with the converted timestamp column
        writer.writerow([wildfire['lastUpdatedTimestamp'], wildfire['incidentLocation'], wildfire['fireCentreName'], wildfire['incidentSizeEstimatedHa'], wildfire['stageOfControlCode'], wildfire['incidentNumberLabel'], wildfire['incidentName'], wildfire['incidentSizeDetail'], wildfire['incidentCauseDetail']])

# read the csv file as a dataframe
df = pd.read_csv('wildfire_data.csv')
# create a dictionary to map the codes to the phrases
code_to_phrase = {
    'OUT_CNTRL': 'Out Of Control',
    'HOLDING': 'Being Held',
    'UNDR_CNTRL': 'Under Control'
}
# replace the values in the stageOfControlCode column with the phrases
df['stageOfControlCode'] = df['stageOfControlCode'].replace(code_to_phrase)
# write the dataframe to a new csv file
df.to_csv('wildfire_data_cleaned.csv', index=False)


#maybe convert lastUpdatedTimestamp to hh:mm:ss