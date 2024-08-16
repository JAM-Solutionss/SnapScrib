from src.backend.modules.audio.audio_data import Audio
from src.backend.modules.transcription.transcription_data import Transcription
from src.backend.modules.transcription.trranscriber_interface import Transcriber


class LightningMlxTranscriber(Transcriber):

    def transcribe(self, audio: Audio) -> Transcription:
        pass