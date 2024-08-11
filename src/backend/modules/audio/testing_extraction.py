from file_extractor import FileExtractor
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)
from utils.logger_config import LOGGER

if __name__ == "__main__":

    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_path = os.path.abspath(
        os.path.join(
            current_dir, "..", "..", "..", "..", "data","audio.mp3"
        )
    )

    audio_extractor = FileExtractor()

    audio = audio_extractor.extract(test_path)

    LOGGER.debug(f"Audio Object: {audio}")
    LOGGER.debug(f"Audio duration: {audio.duration}")
    LOGGER.debug(f"Audio file size: {audio.file_size}")
    LOGGER.debug(f"Audio format: {audio.format}")