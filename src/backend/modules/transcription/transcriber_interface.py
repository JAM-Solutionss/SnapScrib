from abc import ABC, abstractmethod
from typing import Type
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from transcription.transcription_data import Transcription
from audio.audio_data import Audio


class Transcriber(ABC):

    @abstractmethod
    def transcribe(audio: Audio) -> Transcription:
        pass
