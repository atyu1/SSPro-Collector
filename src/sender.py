import json
from requests import post

class JsonSender:
    """
    Class used to send send data via JSON to API server
    """

    def __init__(self, url, user="", password="", secure=False):
        """ Basic initiator """
        self.url = url
        self.user = user
        self.password = password

    def _validate_datapoints(self, data):
        """ Review the collected data and check if all fields are present"""
        # Todo: Add data pre-checks

        return data

    def push(self, data):
        """ Push datapoints to server """
        safe_data = _validate_datapoints(data)
        r = requests.post(self.url+"/datapoints", data=self.data)

    def get_token(self, token_user, token_pass):
        """ Get new token for data processing """
        r = requests.post(self.url+"/login", json={"email":token_user, "password":token_pass})
        print(r)
