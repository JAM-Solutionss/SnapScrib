from abc import ABC, abstractmethod


class Summarizer(ABC):
    @abstractmethod
    def summarize(text):
        pass
