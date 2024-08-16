from abc import abstractmethod, ABC
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from modules.audio.audio_data import Audio
from modules.transcription.transcription_data import Transcription

class Transcriber(ABC):

    @abstractmethod
    def transcribe(self, audio: Audio) -> Transcription:
        pass