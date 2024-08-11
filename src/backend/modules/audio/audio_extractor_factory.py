from audio_extractor import AudioExtractor
from file_extractor import FileExtractor
import sys, os
import re
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)
from utils.logger_config import LOGGER

def get_audio_extractor(source: str) -> AudioExtractor:
    """Factory method to get the appropriate AudioExtractor"""
    if is_youtube_link(source): # Needs to be implemented when youtube extractor is implemented
        LOGGER.warning("Youtube link not supported yet")
        return None
    elif is_supported_audio_file(source):
        LOGGER.debug("Selected FileExtractor")
        return FileExtractor
    else:
        raise ValueError("Invalid audio source")
    
def is_youtube_link(url: str) -> bool:
    youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    match = re.match(youtube_regex, url)
    return bool(match)

def is_supported_audio_file(source: str) -> bool:
    return any(source.lower().endswith(ext) for ext in AudioExtractor.supported_audio_files)
