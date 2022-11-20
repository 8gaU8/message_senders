import json

import requests

from .base_sender import BaseSender


class DiscordSender(BaseSender):
    def __init__(self, api_key):
        self.api_key = api_key

    def send(self, text: str):
        headers = {"Content-Type": "application/json"}
        data = {}
        data["content"] = text
        response = requests.post(self.api_key, json.dumps(data), headers=headers)
        return response
