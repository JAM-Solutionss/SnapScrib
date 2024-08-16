from src.backend.modules.audio.audio_data import Audio
from src.backend.modules.transcription.transcription_data import Transcription


class WhisperTranscriber:
    def transcribe(self, audio: Audio) -> Transcription:
        pass