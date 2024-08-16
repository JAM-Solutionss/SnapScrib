import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from modules.audio.audio_data import Audio
from modules.transcription.transcription_data import Transcription
from src.backend.modules.transcription.transcriber_interface import Transcriber


class LightningMlxTranscriber(Transcriber):

    def transcribe(self, audio: Audio) -> Transcription:
        pass