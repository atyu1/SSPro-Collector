import json
from requests import post

class JsonSender:
    """
    Class used to send send data via JSON to API server
    """

    def __init__(self, url, data, user="", password="", secure=False):
        """ Basic initiator """
        self.ipaddr = ipaddr
	self.port = port
        self.user = user
        self.password = password

        self.data = self._fix_data(data)

    def _fix_data(self, data):
	""" Review the collected data and check if all fields are present"""
	# Todo: Add data pre-checks

	return data

    def push(self):
        """ Push data to server """

        r = requests.post(self.url, data=self.data)
