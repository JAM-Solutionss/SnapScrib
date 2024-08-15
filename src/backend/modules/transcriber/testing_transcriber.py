from transcribe import get_transcription
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"current_dir: {current_dir}")
    source_file = os.path.join(current_dir, "..", "..", "..", "..", "data", "audio.mp3")

    url = "https://www.youtube.com/watch?v=-HV0B8pHjuA"

    transcription = get_transcription().transcribe(audio_file=source_file, youtube_url=url)
    LOGGER.info(f"RETURN: {transcription}")
