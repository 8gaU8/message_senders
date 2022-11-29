import json
from typing import Optional

import requests

from .base_sender import BaseSender


class SlackSender(BaseSender):
    def __init__(self, channel_url: str, user_info: Optional[dict] = None):
        self.channel_url = channel_url
        self.user_info = {"username": "slack_sender", "icon_emoji": ":strawberry:"}
        if user_info is not None:
            self.user_info = user_info

    def send(self, text: str):
        self.user_info["text"] = text
        response = requests.post(
            self.channel_url,
            json.dumps(self.user_info),
        )
        return response
