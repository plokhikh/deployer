import json
import colors
import os
from client import TargetProcessClient


class TargetProcessConnector:
    def __init__(self):
        self.token = os.environ.get('TARGET_PROCESS_TOKEN')

        if self.token is None:
            print colors.error("Environment variable 'TARGET_PROCESS_TOKEN' missing")
            exit()
        else:
            self.tp = TargetProcessClient(self.token)

    def move_user_stories(self, userStoriesIds, toState):
        if not isinstance(userStoriesIds, list):
            print colors.error("User stories should be list instance")
            exit()

        response = self.tp.get('UserStories', {'id': userStoriesIds})

        if response.status_code != 200:
            print colors.error("Cant get user stories")
            exit()

        userStories = json.loads(response.text)

        if 'Items' not in userStories:
            print colors.error('Bad response')
            exit()

        for userStory in userStories['Items']:
            result = self.tp.post('UserStories', {
                'Id': userStory['Id'],
                'EntityState': {'Id': self.tp.getStateCode(toState)}
            })

            if result.status_code == 200:
                print colors.success("User story {} \"{}\" -> \"{}\"".format(
                    userStory['Id'],
                    userStory['EntityState']['Name'],
                    toState
                ))
            else:
                print colors.error("User story {} update failed".format(id))

