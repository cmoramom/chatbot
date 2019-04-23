import requests

# this class consume and return the raw data form the API


class Consume(object):
    url = None
    api_token = None

    def __init__(self, url=None, api_toke=None):
        self.url = url
        self.api_token = api_toke
        self.headers = {'Content-Type': 'application/text/csv',
                        'Authorization': 'Bearer {0}'.format(self.api_token)}

    def consume_api(self):
        response = requests.get(self.url, headers=self.headers)

        if response.status_code == 200:
            return response.content.decode('utf-8')
        else:
            return None
