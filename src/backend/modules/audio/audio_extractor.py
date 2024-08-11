from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type
import mutagen
import mutagen.wave
from audio_data import Audio


class AudioExtractor(ABC):
    """Abstract interface class for AudioExtractor"""

    @abstractmethod
    def extract(self, audio_source: str) -> Type[Audio]:
        """This method needs to be implemmented by the child class"""
        pass