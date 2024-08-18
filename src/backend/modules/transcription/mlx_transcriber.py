from datetime import timedelta
import os
import sys
from transcriber_interface import Transcriber
from transcription_data import Transcription

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from modules.audio.audio_data import Audio
from utils.logger_config import LOGGER

if sys.platform == "darwin":
    import mlx_whisper


class MlxTranscriber:
    def transcribe(self, audio: Audio) -> Transcription:
        result = mlx_whisper.transcribe(audio, word_timestamps=True)
        return " ".join(text for text in result["segments"])


# class MLX_Transcriber(Transcriber):
#     def transcribe(audio_file: str, youtube_url: str) -> str:
#         path_or_hf_repo = "mlx-community/whisper-large-v3-mlx"
#         speech_file = audio_file
#         result = mlx_whisper.transcribe(speech_file, word_timestamps=True)
#         text = result["text"]
#         segments = result["segments"]

#         output_list = []

#         for segment in segments:
#             text = segment["text"]

#             output_list.append(text)
#             full_text = " ".join(output_list)

#         return full_text
