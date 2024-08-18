from abc import ABC, abstractmethod
from typing import Type
import sys
import os

from transcription_data import Transcription

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from audio.audio_data import Audio


class Transcriber(ABC):

    @abstractmethod
    def transcribe(audio: Audio) -> Transcription:
        pass
