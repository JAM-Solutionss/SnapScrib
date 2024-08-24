from dataclasses import dataclass
import sys
import mutagen
import os
from urllib.parse import unquote

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER


@dataclass
class Audio:
    audio_file: str
    source: str

    @property
    def duration(self) -> float:
        """:return: duration of the audio file in seconds"""
        LOGGER.debug(f"Getting duration for audio file {self.audio_file}...")
        audio = mutagen.File(self.audio_file)
        if audio:
            return int(audio.info.length)
        else:
            raise ValueError(f"Invalid audio file: {self.audio_file}")

    @property
    def file_size(self) -> float:
        """:return: file size of the audio file in bytes"""
        return os.path.getsize(self.audio_file)

    @property
    def format(self) -> str:
        """:return: format of the audio file"""
        audio = mutagen.File(self.audio_file)
        if audio is not None:
            # Attempt to retrieve MIME type if available
            if hasattr(audio.info, "mime_type"):
                return audio.info.mime_type
            elif hasattr(audio, "mime"):
                return audio.mime[0].split("/")[-1] if audio.mime else None
            else:
                return self.audio_file.split(".")[-1]
        else:
            raise ValueError(f"Invalid audio file: {self.audio_file}")

    @property
    def is_youtube_source(self) -> bool:
        """:return: True if audio source is a YouTube URL"""
        return self.source.lower().startswith(
            (
                "http://www.youtube.com/watch?v=",
                "https://www.youtube.com/watch?v=",
                "http://youtu.be/",
                "https://youtu.be/",
                "www.youtube.com/watch?v=",
                "youtube.com/watch?v=",
                "youtu.be/",
            )
        )
        
    def _sanitize_path(self, path: str) -> str:
        # Decode URL-encoded characters
        path = unquote(path)
        # Replace problematic characters
        path = re.sub(r'[<>:"/\\|?*]', '_', path)
        return os.path.abspath(path)
