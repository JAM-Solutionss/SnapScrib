from audio_extractor import AudioExtractor, DummyAudio
from typing import Type
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))
from logger_config import LOGGER


class FileExtractor(AudioExtractor):
    def extract(self, file_source: str) -> Type[DummyAudio]:
        """
        Extract audio from a file source.

        Args:
            file_source (str): The path to the audio file.

        Returns:
            str: A Audio instance representing the extracted audio.

        Raises:
            ValueError: If the provided file path is invalid.
        """
        if os.path.isfile(file_source):
            # file_source is a valid file path
            
            LOGGER.info(f"Extracting audio from file source {file_source}...")
            
            audio = DummyAudio(audio_file=file_source)  # Instantiation needs to be adjusted later, when Adio dataclass is implemented
            
            return audio
        else:
            # file_source is not a valid file path
            raise ValueError(f"Invalid file path: {file_source}")
