from abc import ABC, abstractmethod


class BaseSender(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def send(self, text: str):
        pass
