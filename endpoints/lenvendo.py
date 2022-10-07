import requests


class LenvendoAPI:
    def __init__(self, api):
        self.url = 'https://www.lenvendo.ru' + api

    def get(self, params):
        return requests.get(url=self.url, params=params)
