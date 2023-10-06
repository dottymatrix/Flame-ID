import datetime
#testing time conversion script
# get the seconds from the lastUpdatedTimestamp
seconds = 1693110000
# create a datetime object from the seconds
dt = datetime.datetime.fromtimestamp(seconds)
# format the datetime object as hh:mm:ss
time = dt.strftime('%H:%M:%S, %b %d %Y')
# print the time
print(time)