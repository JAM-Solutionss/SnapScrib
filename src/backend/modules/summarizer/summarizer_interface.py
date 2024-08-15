from abc import ABC, abstractmethod


class Summarizer(ABC):
    @abstractmethod
    def summarize(
        self, transcription: str, style: str = "neutral", length: float = 0.3
    ) -> str:
        pass
