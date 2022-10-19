import json
import subprocess
from pathlib import Path
from typing import Optional

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


class FileSender(BaseSender):
    def __init__(self, path: Path):
        self.path = path

    def send(self, text: str):
        with open(self.path, "a") as f:
            f.write(text + "\n")


class StdOutSender(BaseSender):
    def __init__(self, *args, **kwargs):
        pass

    def send(self, text: str):
        print(text)


class RemoteFileSender(BaseSender):
    def __init__(self, host: str, host_path: str):
        self.host = host
        self.path = host_path

    def send(self, text: str):
        cmd = self._build_command(text)
        subprocess.run(cmd)

    def _build_command(self, text: str):
        text = text.replace("\n", r"\n")
        base_cmd = f"ssh {self.host} 'echo -e \"{text.strip()}\" >> {self.path}'"
        cmd = ["sh", "-c", base_cmd]
        return cmd


class LineSender(BaseSender):
    def __init__(self, token: str):
        self.header = {"Authorization": f"Bearer {token}"}
        self.url = "https://notify-api.line.me/api/notify"

    def send(self, text: str, image_path: Optional[Path] = None):
        if image_path is None:
            return self._send_text(text)
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
