from datetime import timedelta
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from transcriber.transcriber_interface import Transcriber

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER

if sys.platform == "darwin":
    import mlx_whisper


class MLX_Transcriber(Transcriber):
    def transcribe(audio_file: str, youtube_url: str) -> str:
        path_or_hf_repo = "mlx-community/whisper-large-v3-mlx"
        speech_file = audio_file
        result = mlx_whisper.transcribe(speech_file, word_timestamps=True)
        text = result["text"]
        segments = result["segments"]

        output_list = []

        for segment in segments:
            text = segment["text"]

            output_list.append(text)
            full_text = " ".join(output_list)

        return full_text
