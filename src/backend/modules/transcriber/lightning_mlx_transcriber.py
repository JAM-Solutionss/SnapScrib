import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from transcriber.transcriber_blueprint import Transcriber

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER

if sys.platform == "darwin":
    from lightning_whisper_mlx import LightningWhisperMLX


class Lightning_MLX_Transcriber(Transcriber):
    def transcribe(audio_file: str, youtube_url: str) -> str:
        LOGGER.info(f"Starting transcription for file: {audio_file}")

        try:
            whisper = LightningWhisperMLX(
                model="distil-large-v3", batch_size=12, quant=None
            )
            LOGGER.info("Model loaded successfully.")

            LOGGER.info("Starting the transcription process...")
            result = whisper.transcribe(audio_file)
            LOGGER.info("Transcription process finished.")

            text = result.get("text", "")
            if text:
                LOGGER.info("Transcription result obtained.")
            else:
                LOGGER.warning("Transcription result is empty.")

            print(text)
            return text

        except Exception as e:
            LOGGER.error(f"An error occurred during transcription: {str(e)}")
            return ""

    def convert_millis(self, millis):
        LOGGER.info("Converting milliseconds to hh:mm:ss,ms format...")
        seconds = (millis / 1000) % 60
        minutes = (millis / (1000 * 60)) % 60
        hours = (millis / (1000 * 60 * 60)) % 24
        millis = millis % 1000
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(millis):03}"

    def create_json(self, transcription):
        LOGGER.info("Creating JSON file content...")
        json_content = []
        for idx, (start, end, text) in enumerate(transcription, start=1):
            segment = {
                "index": idx,
                "start_time": self.convert_millis(start),
                "end_time": self.convert_millis(end),
                "text": text,
            }
            json_content.append(segment)

        return json_content

    def create_srt(self, transcription):
        LOGGER.info("Creating SRT file content...")
        srt_content = []
        for idx, (start, end, text) in enumerate(transcription, start=1):
            start_time = self.convert_millis(start)
            end_time = self.convert_millis(end)
            srt_content.append(f"{idx}\n{start_time} --> {end_time}\n{text}\n")

        return "\n".join(srt_content)
