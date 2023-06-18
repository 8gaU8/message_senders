import json

import requests

from .base_sender import BaseSender


class DiscordSender(BaseSender):
    def _set_token(self):
        with open(self.config_file) as f:
            json_dict = json.load(f)
        self.webhook_url = json_dict["webhook_url"]

    def send(self, text: str):
        headers = {"Content-Type": "application/json"}
        data = {}
        data["content"] = text
        response = requests.post(self.webhook_url, json.dumps(data), headers=headers)
        return response
