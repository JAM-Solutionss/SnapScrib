from src.backend.modules.audio.audio_data import Audio
from src.backend.modules.transcriber.transcriber_interface import Transcriber
from src.backend.modules.transcription.transcription_data import Transcription


class YoutubeTranscriber(Transcriber):
    
    def transcribe(audio: Audio) -> Transcription:
        pass