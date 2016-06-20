import urllib
import requests
import json
from lxml import objectify

token = ''

body = urllib.urlopen(
    "https://mbt.tpondemand.com/api/v1/UserStories/22665?token=").read()

userStory = objectify.fromstring(body)

result = requests.post(
    "https://mbt.tpondemand.com/api/v1/UserStories?token=",
    data=json.dumps({'Id': userStory.attrib['Id'], 'EntityState': {'Id':246}}),
    headers={"Content-type": "application/json"}
)

print(result.status_code, result.reason)
