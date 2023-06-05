from .base_sender import BaseSender


class StdOutSender(BaseSender):
    def __init__(self, *args, **kwargs):
        pass

    def send(self, text: str):
        print(text)
