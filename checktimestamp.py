import json
import datetime
import csv

# open the JSON file in read mode
with open('wildfire_data.json', 'r') as f:
    # load the JSON data as a Python object
    data = json.load(f)

# iterate through each wildfire in the data
for wildfire in data:
    # get the milliseconds from the 'lastUpdatedTimestamp'
    milliseconds = wildfire['lastUpdatedTimestamp']
    # print the value of milliseconds
    print(milliseconds)
if TypeError:
    print(f"TypeError: unsupported operand type(s) for /: '{milliseconds}' and 'int'")

try:
    # get the milliseconds from the 'lastUpdatedTimestamp'
    milliseconds = wildfire['lastUpdatedTimestamp']
    # divide the milliseconds by 1000 to get the seconds
    seconds = milliseconds / 1000
    # create a datetime object from the seconds
    dt = datetime.datetime.fromtimestamp(seconds)
    # format the datetime object as hh:mm:ss
    time = dt.strftime('%H:%M:%S')
    # replace the 'lastUpdatedTimestamp' with the time
    wildfire['lastUpdatedTimestamp'] = time
except TypeError:
    print(f"TypeError: unsupported operand type(s) for /: '{milliseconds}' and 'int'")