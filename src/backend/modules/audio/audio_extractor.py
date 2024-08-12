from abc import ABC, abstractmethod
from typing import Type
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from audio.audio_data import Audio



class AudioExtractor(ABC):
    """Abstract interface class for AudioExtractor"""
    supported_audio_files = ['.mp3', '.wav', '.flac', '.ogg', '.m4a']

    @abstractmethod
    def extract(self, audio_source: str) -> Type[Audio]:
        """This method needs to be implemmented by the child class"""
        pass
    
