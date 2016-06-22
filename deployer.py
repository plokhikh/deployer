import json
import colors
import os
from client import TargetProcessClient

token = os.environ.get('TARGET_PROCESS_TOKEN')

if token is None:
    print colors.error("Environment variable 'TARGET_PROCESS_TOKEN' missing")
    exit()

userStoriesIds = []
wishState = 'Verify on Int'
tp = TargetProcessClient(token)

response = tp.get('UserStories', {'id': userStoriesIds})

if response.status_code != 200:
    print colors.error("Cant get user stories")
    exit()

userStories = json.loads(response.text)

if 'Items' not in userStories:
    print colors.error('Bad response')
    exit()

for userStory in userStories['Items']:
    result = tp.post('UserStories', {
        'Id': userStory['Id'],
        'EntityState': {'Id': tp.getStateCode(wishState)}
    })

    if result.status_code == 200:
        print colors.success("User story {} moved \"{}\" -> \"{}\" success".format(
            userStory['Id'],
            userStory['EntityState']['Name'],
            wishState
        ))
    else:
        print colors.error("User story {} update failed".format(id))
