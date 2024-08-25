from abc import ABC, abstractmethod
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from audio.audio_data import Audio


class AudioExtractor(ABC):
    
    """
    Abstract base class for audio extraction.

    This class defines the interface for audio extractors. Subclasses should
    implement the `extract` method to provide specific extraction functionality.

    Attributes:
        supported_audio_files (list): A list of supported audio file extensions.
        _default_audio_file_save_path (str): The default path for saving extracted audio files.

    Methods:
        __init__(self, audio_file_path=None): Initialize the AudioExtractor.
        extract(self, audio_source: str) -> Audio: Abstract method for audio extraction.
    """

    supported_audio_files = [".mp3", ".wav", ".flac", ".ogg", ".m4a"]
    _default_audio_file_save_path = os.path.join(os.path.dirname(__file__), "download")


    def __init__(self, audio_file_path=None):
        self._audio_file_path = (
            audio_file_path if audio_file_path else self._default_audio_file_save_path
        )
        os.makedirs(self._audio_file_path, exist_ok=True)

    @abstractmethod
    def extract(self, audio_source: str) -> Audio:
        """This method needs to be implemmented by the child class"""
        pass