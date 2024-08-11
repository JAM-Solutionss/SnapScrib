from abc import ABC, abstractmethod
from typing import Type
from audio_data import Audio



class AudioExtractor(ABC):
    """Abstract interface class for AudioExtractor"""
    supported_audio_files = ['.mp3', '.wav', '.flac', '.ogg', '.m4a']

    @abstractmethod
    def extract(audio_source: str) -> Type[Audio]:
        """This method needs to be implemmented by the child class"""
        pass
    
