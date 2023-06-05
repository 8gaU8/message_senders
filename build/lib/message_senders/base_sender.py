from abc import ABC, abstractmethod
from os.path import expanduser
from pathlib import Path

from humps import decamelize


class BaseSender(ABC):
    needs_config: bool = True

    def __init__(self, *args, **kwargs):
        self._check_config()
        self._set_token()

    def _check_config(self):
        if not self.needs_config:
            return

        home_dir = Path(expanduser("~"))
        config_dir = home_dir / ".config/message_senders"
        if not config_dir.exists():
            config_dir.mkdir(parents=True)

        class_name_snake_case = decamelize(self.__class__.__name__)
        class_prefix = "_".join(class_name_snake_case.split("_")[:-1])

        self.config_file = config_dir / (class_prefix + "_config.json")

        if not self.config_file.exists() and self.needs_config:
            raise FileNotFoundError(str(self.config_file))

    @abstractmethod
    def send(self, text: str):
        pass

    def _set_token(self):
        pass
