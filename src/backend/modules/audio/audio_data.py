from dataclasses import dataclass, Field
import sys
import mutagen
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)
from utils.logger_config import LOGGER


@dataclass
class Audio:
    audio_file: str

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