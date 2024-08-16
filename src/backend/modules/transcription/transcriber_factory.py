import sys
from src.backend.modules.transcription.trranscriber_interface import Transcriber



def get_transcriber(type: str= None) -> Transcriber:
    operating_system = sys.platform
    pass