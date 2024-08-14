from abc import ABC, abstractmethod
from typing import Type
from transcription import Transcription

class Summarizer(ABC):
    @abstractmethod
    def summarize(transcription: Type[Transcription]) -> str:
        pass
