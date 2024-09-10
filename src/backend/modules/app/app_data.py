from dataclasses import dataclass
import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from audio.audio_data import Audio
from audio.audio_extractor_interface import AudioExtractor
from audio.file_extractor import FileExtractor
from transcription.transcriber_interface import Transcriber
from transcription.transcription_data import Transcription
from summary.summarizer_interface import Summarizer
from summary.summary_data import Summary

@dataclass
class AppData:
    audio_extractor: AudioExtractor = None
    audio: Audio = None
    transcriber: Transcriber = None
    transcription: Transcription = None
    summarizer: Summarizer = None
    summary: Summary = None
    
