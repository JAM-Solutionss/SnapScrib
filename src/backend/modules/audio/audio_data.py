from dataclasses import dataclass
import sys
import mutagen
import os
from urllib.parse import unquote

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER


@dataclass
class Audio:
    """
    A dataclass representing an audio file.

    Attributes:
        audio_file (str): The path to the audio file.
        source (str): The source of the audio file, which could be a local path or a URL.

    Properties:
        duration (float): The duration of the audio file in seconds.
        file_size (float): The size of the audio file in bytes.
        format (str): The format or MIME type of the audio file.
        is_youtube_source (bool): Indicates whether the audio source is a YouTube URL.

    Methods:
        duration(): Calculates and returns the duration of the audio file.
        file_size(): Returns the size of the audio file.
        format(): Determines and returns the format of the audio file.
        is_youtube_source(): Checks if the audio source is a YouTube URL.

    Raises:
        ValueError: If the audio file is invalid or cannot be processed.
    """
    
    audio_file: str
    source: str

    @property
    def duration(self) -> float:
        """:return: duration of the audio file in seconds"""
        audio = mutagen.File(self.audio_file)
        if audio:
            return int(audio.info.length)
        else:
            raise ValueError(f"Invalid audio file: {self.audio_file}")

    @property
    def file_size(self) -> float:
        """:return: file size of the audio file in megabytes"""
        return os.path.getsize(self.audio_file) / (1024 * 1024)

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
