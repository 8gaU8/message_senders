from pathlib import Path

import requests

from .base_sender import BaseSender


class LineSender(BaseSender):
    def __init__(self, token: str):
        self.header = {"Authorization": f"Bearer {token}"}
        self.url = "https://notify-api.line.me/api/notify"

    def send(self, text: str):
        return self._send_text(text)

    def send_img(self, text: str, image_path: Path):
        if not image_path.exists():
            return self._send_text(text + " (file not found)")
        return self._send_img(text, image_path)

    def _send_text(self, text: str):
        payload = {"message": text}
        return requests.post(self.url, headers=self.header, params=payload)

    def _send_img(self, text: str, image_path):
        payload = {"message": text}
        image_file = open(image_path, "rb")
        try:
            files = {"imageFile": image_file}
            return requests.post(
                self.url, headers=self.header, params=payload, files=files
            )
        finally:
            image_file.close()
            print("file closed.")
