import os
import sys
from transcription.transcriber_interface import Transcriber
from transcription.transcription_data import Transcription
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from modules.audio.audio_data import Audio
from utils.logger_config import LOGGER

if sys.platform == "darwin":
    import mlx_whisper


class MlxTranscriber(Transcriber):
    def __init__(self) -> None:
        if MlxTranscriber is None:
            raise ImportError("LightningMlxTranscriber not available on this OS")

    def transcribe(self, audio: Audio) -> Transcription:
        """
        Transcribes the provided audio using the MLX Whisper model and returns the transcription as a Transcription object.

        Args:
            audio (Audio): The audio data to be transcribed.

        Returns:
            Transcription: The transcription of the audio data.

        Raises:
            Exception: If the transcription process fails or no text is returned.
        """

        LOGGER.info("Starting the transcription process...")

        try:
            result = mlx_whisper.transcribe(audio.audio_file, word_timestamps=True)
            LOGGER.info("Transcription process finished.")
        except Exception as e:
            LOGGER.error(f"Transcription failed with error: {e}")
            raise
        print(result["text"])
        #text = " ".join(text for text in result["segments"])
        # Extract text from each segment
        segments = result["segments"]
        text = " ".join(segment["text"] for segment in segments)

        if text is None:
            raise Exception("Transcription failed, no text returned")

        #json_result = self._create_json_result(
        #    result
        #)  # _create_json_result needs to be implemented correctly to return the json result
        json_content = self._create_json([(segment['start'], segment['end'], segment['text']) for segment in segments])
        json_result = json.dumps(json_content)

        transcription = Transcription(json_output=json_result)
        return transcription

    def _convert_millis(self, millis):
        LOGGER.info("Converting milliseconds to hh:mm:ss,ms format...")
        seconds = (millis / 1000) % 60
        minutes = (millis / (1000 * 60)) % 60
        hours = (millis / (1000 * 60 * 60)) % 24
        millis = millis % 1000
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(millis):03}"

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
