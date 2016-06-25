import requests
import json

class TargetProcessClient:
    format = 'json'
    baseUrl = 'https://mbt.tpondemand.com/api/v1/'
    headers = {"Content-type": "application/json"}
    ENTITY_STATE_HASH_MAP = {
        'Open': 23,
        'Requirements': 246,
        'To develop': 40,
        'In progress': 41,
        'Review': 248,
        'Ready to test': 275,
        'Testing': 249,
        'Merge to Develop': 281,
        'Deploy to Int': 150,
        'Verify on Int': 151,
        'Deploy to Prod': 157,
        'Verification': 156,
        'Done': 24
    }

    def __init__(self, token):
        self.token = token

    def getStateCode(self, state):
        if state in self.ENTITY_STATE_HASH_MAP:
            return self.ENTITY_STATE_HASH_MAP[state]
        else:
            raise ValueError('State "' + state + '" not found')

    def get(self, entity, filter=None):
        params = {'token': self.token, 'format': self.format}
        conditions = []
        if filter is not None:
            for (key, value) in filter.items():
                if isinstance(value, list):
                    conditions.append("%s in (%s)" % (key, ",".join(str(x) for x in value)))
                else:
                    conditions.append("%s eq '%s'" % (key, value))

            params['where'] = ' and '.join(conditions)
        return requests.get(self.baseUrl + entity, params=params)

    def post(self, entity, data=None):
        params = {'token': self.token, 'format': self.format}
        if data is None:
            data = {}

        return requests.post(self.baseUrl + entity, params=params, data=json.dumps(data))