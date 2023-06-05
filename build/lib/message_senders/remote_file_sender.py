import subprocess

from .base_sender import BaseSender


class RemoteFileSender(BaseSender):
    needs_config = False
    def __init__(self, host: str, remote_file_path: str):
        self.host = host
        self.path = remote_file_path

    def send(self, text: str):
        cmd = self._build_command(text)
        subprocess.run(cmd)

    def _build_command(self, text: str):
        text = text.replace("\n", r"\n")
        base_cmd = f"ssh {self.host} 'echo -e \"{text.strip()}\" >> {self.path}'"
        cmd = ["sh", "-c", base_cmd]
        return cmd
