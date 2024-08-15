from datetime import timedelta
import os
import whisper
import torch
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from transcriber.transcriber_interface import Transcriber

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER


class Whisper_Transcriber(Transcriber):
    def transcribe(audio_file: str, youtube_url: str) -> str:
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