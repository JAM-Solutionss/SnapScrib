import os
import sys
from src.backend.modules.transcriber.transcriber_factory import check_os
from modules.youtube_audio.extract_audio import download_youtube_video_as_audio

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from logger_config import LOGGER

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=iXIwm4mCpuc"
    output_dir = "./youtube_audio/output"
    output = os.path.join(output_dir, "audio.mp3")
    filename = "transcription"
    
    os.makedirs(output_dir, exist_ok=True)
    
    LOGGER.info("Downloading audio from YouTube video...")
    download_youtube_video_as_audio(url, output_dir)
    
    if not os.path.exists(output):
        LOGGER.error(f"Audio file not found at {output}. Exiting.")
        sys.exit(1)
    
    LOGGER.info("Transcribing audio...")
    check_os(output, filename)