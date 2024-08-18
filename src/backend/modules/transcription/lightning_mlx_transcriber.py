import json
from logging import Logger
import os
import sys

from requests import get

from transcriber_interface import Transcriber
from transcription_data import Transcription

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER
from modules.audio.audio_data import Audio

operating_system = sys.platform
if operating_system == "darwin":
    from lightning_whisper_mlx import LightningWhisperMLX, Whisper
else:
    LightningWhisperMLX = None
    Whisper = None


class LightningMlxTranscriber(Transcriber):
    def __init__(self) -> None:
        if LightningMlxTranscriber is None:
            raise ImportError("LightningMlxTranscriber not available on this OS")

    supported_models = [
        "tiny",
        "small",
        "distil-small.en",
        "base",
        "medium",
        "distil-medium.en",
        "large",
        "large-v2",
        "distil-large-v2",
        "large-v3",
        "distil-large-v3",
    ]

    def _get_whisper_class(
        self, model: str, batch_size: int = None, quant: bool = None
    ) -> LightningWhisperMLX:
        if model in self.supported_models:
            whisper = LightningWhisperMLX(
                model=model, batch_size=batch_size, quant=quant
            )
            return whisper
        else:
            raise ValueError(
                f"Model {model} not supported. Supported models are {self.supported_models}."
            )

    def transcribe(
        self,
        audio: Audio,
        model: str = "distil-large-v3",
        batch_size: int = 12,
        quant: bool = None,
    ) -> Transcription:

        whisper = self._get_whisper_class(
            model=model, batch_size=batch_size, quant=quant
        )
        LOGGER.info(f"Model {model} loaded successfully.")

        LOGGER.info("Starting the transcription process...")
        try:
            result = whisper.transcribe(audio.audio_file)
            LOGGER.info("Transcription process finished.")
        except Exception as e:
            LOGGER.error(f"Transcription failed with error: {e}")
            raise

        text = result["text"]
        
        if text is None:
            raise Exception("Transcription failed, no text returned")
        
        LOGGER.info("Transcription result obtained.")
        
        json_result = self._create_json_result(
            result
        )  # _create_json_result needs to be implemented correctly to return the json result
        
        transcription = Transcription(json_output=json_result)
        return transcription


# class Lightning_MLX_Transcriber(Transcriber):
#     def transcribe(audio_file: str, youtube_url: str) -> str:
#         LOGGER.info(f"Starting transcription for file: {audio_file}")

#         try:
#             whisper = LightningWhisperMLX(
#                 model="distil-large-v3", batch_size=12, quant=None
#             )
#             LOGGER.info("Model loaded successfully.")

#             LOGGER.info("Starting the transcription process...")
#             result = whisper.transcribe(audio_file)
#             LOGGER.info("Transcription process finished.")

#             text = result.get("text", "")
#             if text:
#                 LOGGER.info("Transcription result obtained.")
#             else:
#                 LOGGER.warning("Transcription result is empty.")

#             print(text)
#             return text

#         except Exception as e:
#             LOGGER.error(f"An error occurred during transcription: {str(e)}")
#             return ""

    def _convert_millis(self, millis):
        LOGGER.info("Converting milliseconds to hh:mm:ss,ms format...")
        seconds = (millis / 1000) % 60
        minutes = (millis / (1000 * 60)) % 60
        hours = (millis / (1000 * 60 * 60)) % 24
        millis = millis % 1000
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(millis):03}"

    # This needs to be implemnted correctly to return the json_result
    def _create_json(self, transcription):
        LOGGER.info("Creating JSON file content...")
        json_content = []
        for idx, (start, end, text) in enumerate(transcription, start=1):
            segment = {
                "index": idx,
                "start_time": self._convert_millis(start),
                "end_time": self._convert_millis(end),
                "text": text,
            }
            json_content.append(segment)

        return json_content

    def _create_srt(self, transcription):
        LOGGER.info("Creating SRT file content...")
        srt_content = []
        for idx, (start, end, text) in enumerate(transcription, start=1):
            start_time = self.convert_millis(start)
            end_time = self.convert_millis(end)
            srt_content.append(f"{idx}\n{start_time} --> {end_time}\n{text}\n")

        return "\n".join(srt_content)
