from datetime import timedelta
import json
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

    def __init__(self, model: str = default_model) -> None:
        self.model = whisper.load_model(model).to(self.device)
        LOGGER.info(f"Loaded Whisper model: {self.model}")
        LOGGER.info(f"Transcriber is set to {self.device.upper()}-mode.")

    def transcribe(self, audio: Audio) -> Transcription:
        pass

    # class Whisper_Transcriber(Transcriber):
    def transcribe(self, audio: Audio) -> Transcription:

        transcript = self.model.transcribe(audio=audio.audio_file)
        segments = transcript["segments"]
        
        segments = self._add_duration_to_segments(segments)
        
        json_output = self._get_json_output(segments)
        
        return Transcription(json_output=json_output)
        
        
        # segments = transcript["segments"]

        # json_output = []
        # for segment in segments:
        #     startTime = str(0) + str(timedelta(seconds=int(segment["start"]))) + ",000"
        #     endTime = str(0) + str(timedelta(seconds=int(segment["end"]))) + ",000"
        #     text = segment["text"]
        #     segmentId = segment["id"] + 1
        #     segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

        #     segment_dict = {
        #         "id": segmentId,
        #         "start_time": startTime,
        #         "end_time": endTime,
        #         "text": text[1:] if text[0] == " " else text,
        #     }
        #     json_output.append(segment_dict)

        #     result = "".join(text)

        # return transcript

    def _add_duration_to_segments(self, segments: list) -> dict:
        for segment in segments:
            segment["duration"] = segment["end"] - segment["start"]
        return segments       
    
    def _get_json_output(self, segments: list) -> str:
        """Formatting segments to required JSON format of Transcription dataclass and returning the json string"""
        json_output = []
        
        for segment in segments:
            segment_dict = {
                "text": segment["text"],
                "start": segment["start"],
                "duration": segment["duration"],
                "end": segment["end"],
            }
            json_output.append(segment_dict)
        
        return json.dumps(json_output)
            

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
