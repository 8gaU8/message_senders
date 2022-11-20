from requests_oauthlib import OAuth1Session

from .base_sender import BaseSender


class TweetSender(BaseSender):
    api_root = "https://api.twitter.com/2"

    def __init__(
        self,
        consumer_key: str,
        consumer_key_secret: str,
        access_token: str,
        access_token_secret: str,
    ):
        super().__init__()
        self.session = OAuth1Session(
            consumer_key, consumer_key_secret, access_token, access_token_secret
        )
        self.api_url = f"{self.api_root}/tweets"

    def send(self, text: str):
        params = {"text": text}
        response = self.session.post(self.api_url, json=params)
        return response
