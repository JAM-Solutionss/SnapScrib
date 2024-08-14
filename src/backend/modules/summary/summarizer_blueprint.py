from abc import ABC, abstractmethod
from typing import Type
from transcription import Transcription

class Summarizer(ABC):
    @abstractmethod
    def summarize(self, transcription: str, style: str='neutral', length: float=0.3) -> str:
        pass
