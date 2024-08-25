import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from audio.audio_data import Audio
from audio.audio_extractor_interface import AudioExtractor

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER


class FileExtractor(AudioExtractor):
    """
    A class for extracting audio from file sources.

    This class implements the AudioExtractor interface and provides
    functionality to extract audio data from file sources.

    Attributes:
        Inherits attributes from AudioExtractor.

    Methods:
        extract(audio_source: str) -> Audio:
            Extracts audio from a given file source.
    """

        
    def __init__(self):
        super().__init__()

    def extract(self, audio_source: str) -> Audio:
        """
        Extract audio from a file source.

        Args:
            file_source (str): The path to the audio file.

        Returns:
            str: A Audio instance representing the extracted audio.

        Raises:
            ValueError: If the provided file path is invalid.
        """
        if os.path.isfile(audio_source):
            # file_source is a valid file path

            LOGGER.info(f"Extracting audio from file source {audio_source}...")

            audio = Audio(audio_file=audio_source, source=audio_source)

            return audio
        else:
            # file_source is not a valid file path
            raise ValueError(f"Invalid file path: {audio_source}")
