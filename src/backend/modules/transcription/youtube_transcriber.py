import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from modules.audio.audio_data import Audio
from modules.transcriber.transcriber_interface import Transcriber
from modules.transcription.transcription_data import Transcription


class YoutubeTranscriber(Transcriber):

    def transcribe(audio: Audio) -> Transcription:
        pass
