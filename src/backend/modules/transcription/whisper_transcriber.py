from datetime import timedelta
import os
import whisper
import torch
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from modules.audio.audio_data import Audio
from transcription_data import Transcription
from transcriber_interface import Transcriber


class WhisperTranscriber(Transcriber):
    
    default_model = "base"
    available_models = ["tiny", "base", "small", "medium", "large"]
    has_cuda = torch.cuda.is_available()
    device = "cuda" if has_cuda else "cpu"
    
    def __init__(self, model: str=default_model) -> None:
        self.model = whisper.load_model("base")

    def transcribe(self, audio: Audio) -> Transcription:
        pass


# class Whisper_Transcriber(Transcriber):
    def transcribe(self, audio: Audio) -> Transcription:
      
        torch.cuda.init()
        device = "cuda"

        model = whisper.load_model("base").to(device=device)
        LOGGER.info("Whisper model loaded.")
        with torch.cuda.device(device):
            transcribe = model.transcribe(audio=audio_file)
        segments = transcribe["segments"]

        json_output = []
        for segment in segments:
            startTime = str(0) + str(timedelta(seconds=int(segment["start"]))) + ",000"
            endTime = str(0) + str(timedelta(seconds=int(segment["end"]))) + ",000"
            text = segment["text"]
            segmentId = segment["id"] + 1
            segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

            segment_dict = {
                "id": segmentId,
                "start_time": startTime,
                "end_time": endTime,
                "text": text[1:] if text[0] == " " else text,
            }
            json_output.append(segment_dict)

            result = "".join(text)

        return str(result)
    
    
    # def transcribe(audio_file: str, youtube_url: str) -> str:
    #     torch.cuda.init()
    #     device = "cuda"

    #     model = whisper.load_model("base").to(device=device)
    #     LOGGER.info("Whisper model loaded.")
    #     with torch.cuda.device(device):
    #         transcribe = model.transcribe(audio=audio_file)
    #     segments = transcribe["segments"]

    #     json_output = []
    #     for segment in segments:
    #         startTime = str(0) + str(timedelta(seconds=int(segment["start"]))) + ",000"
    #         endTime = str(0) + str(timedelta(seconds=int(segment["end"]))) + ",000"
    #         text = segment["text"]
    #         segmentId = segment["id"] + 1
    #         segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

    #         segment_dict = {
    #             "id": segmentId,
    #             "start_time": startTime,
    #             "end_time": endTime,
    #             "text": text[1:] if text[0] == " " else text,
    #         }
    #         json_output.append(segment_dict)

    #         result = "".join(text)

    #     return str(result)