from audio_extractor_factory import get_audio_extractor
import sys, os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER

if __name__ == "__main__":

    current_dir = os.path.dirname(os.path.abspath(__file__))
    source_file = os.path.join(
        current_dir, "..", "..", "..", "..", "youtube_audio", "output", "audio.mp3"
    )

    source_yt = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    # Automatically getting the correct AudioExtractor
    audio_extractor_file = get_audio_extractor(source_file)
    audio_extractor_yt = get_audio_extractor(
        source_yt
    )  # This will raise an NotImplementedError as this Extractor is not implemented yet

    # Extracting the audio from file
    audio_from_file = audio_extractor_file.extract(source_file)

    LOGGER.debug(f"Audio Object: {audio_from_file}")
    LOGGER.debug(f"Audio duration: {audio_from_file.duration}")
    LOGGER.debug(f"Audio file size: {audio_from_file.file_size}")
    LOGGER.debug(f"Audio format: {audio_from_file.format}")