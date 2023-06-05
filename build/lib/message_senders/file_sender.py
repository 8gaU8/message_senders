from pathlib import Path

from .base_sender import BaseSender


class FileSender(BaseSender):
    def __init__(self, path: Path):
        self.path = path

    def send(self, text: str):
        with open(self.path, "a") as f:
            f.write(text + "\n")
