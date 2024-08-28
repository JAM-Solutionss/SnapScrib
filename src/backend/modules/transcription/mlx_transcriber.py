import os
import sys
from transcriber_interface import Transcriber
from transcription_data import Transcription

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from modules.audio.audio_data import Audio
from utils.logger_config import LOGGER

if sys.platform == "darwin":
    import mlx_whisper


class MlxTranscriber(Transcriber):
    """
    Provides a transcription service using the MLX Whisper model.

    The `MlxTranscriber` class is responsible for transcribing audio data using
    the MLX Whisper model. It takes an `Audio` object as input and returns a `Transcription`
    object containing the transcribed text and associated metadata.

    The class includes methods for converting the transcription results to a JSON format and
    for converting millisecond timestamps to a human-readable format.

    Raises:
        ImportError: If the MLX Whisper model is not available on the current operating system.
        Exception: If the transcription process fails or no text is returned.
    """

    def __init__(self) -> None:
        if MlxTranscriber is None:
            raise ImportError("LightningMlxTranscriber not available on this OS")

    def transcribe(self, audio: Audio) -> Transcription:
        """
        Transcribes the provided audio using the MLX Whisper model and returns the transcription
        as a Transcription object.

        Args:
            audio (Audio): The audio data to be transcribed.

        Returns:
            Transcription: The transcription of the audio data.

        Raises:
            Exception: If the transcription process fails or no text is returned.
        """

        LOGGER.info("Starting the transcription process...")

        try:
            result = mlx_whisper.transcribe(audio, word_timestamps=True)
            LOGGER.info("Transcription process finished.")
        except Exception as e:
            LOGGER.error(f"Transcription failed with error: {e}")
            raise
        text = " ".join(text for text in result["segments"])

        if text is None:
            raise Exception("Transcription failed, no text returned")

        json_result = self._create_json(
            result
        )  # _create_json_result needs to be implemented correctly to return the json result

        transcription = Transcription(json_output=json_result)
        return transcription

    def _convert_millis(self, millis):
        """
        Converts a millisecond timestamp to a human-readable string in the format "hh:mm:ss,ms".

        Args:
            millis (int): The timestamp in milliseconds.

        Returns:
            str: The timestamp in the format "hh:mm:ss,ms".
        """
        LOGGER.info("Converting milliseconds to hh:mm:ss,ms format...")
        seconds = (millis / 1000) % 60
        minutes = (millis / (1000 * 60)) % 60
        hours = (millis / (1000 * 60 * 60)) % 24
        millis = millis % 1000
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(millis):03}"

    def _create_json(self, transcription):
        """
        Creates a JSON representation of the transcription results.

        Args:
            transcription (list): A list of tuples containing the start time, end time,
            and text for each segment of the transcription.

        Returns:
            list: A list of dictionaries, where each dictionary represents a segment of the
            transcription with the following keys:
                - index (int): The index of the segment, starting from 1.
                - start_time (str): The start time of the segment in the format "hh:mm:ss,ms".
                - end_time (str): The end time of the segment in the format "hh:mm:ss,ms".
                - text (str): The text of the segment.
        """
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
