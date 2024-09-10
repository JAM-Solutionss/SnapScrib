import os
import sys
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptList, Transcript
from youtube_transcript_api.formatters import JSONFormatter, TextFormatter
from transcriber_interface import Transcriber
from transcription_data import Transcription
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from modules.audio.audio_data import Audio
from utils.logger_config import LOGGER


class YoutubeTranscriber(Transcriber):
    """
    A class for transcribing YouTube videos.

    This class implements the Transcriber interface and provides functionality
    to transcribe YouTube videos using the YouTube Transcript API.

    Attributes:
        fallback_languages (list): A list of language codes to use as fallbacks
            if the requested language is not available.
        formatters (dict): A dictionary of formatter objects for different output formats.

    Methods:
        transcribe(audio: Audio, language: str) -> Transcription:
            Transcribes a YouTube video and returns a Transcription object.

    Note:
        This class requires the youtube_transcript_api library to function properly.
    """

    fallback_languages = ["en", "de"]

    formatters = {"json": JSONFormatter(), "text": TextFormatter()}

    def transcribe(
        self, audio: Audio, language: str = fallback_languages[0]
    ) -> Transcription:
        """
        Transcribe a YouTube video.

        This method takes an Audio object representing a YouTube video and transcribes it,
        returning a Transcription object containing the transcribed text and JSON output.

        Args:
            audio (Audio): An Audio object representing the YouTube video to be transcribed.
            language (str, optional): The target language for transcription. Defaults to the first language in fallback_languages.

        Returns:
            Transcription: A Transcription object containing the transcribed text and formatted JSON output.

        Raises:
            ValueError: If the audio source is not a valid YouTube URL.

        Note:
            This method attempts to fetch the transcript in the specified language. If unavailable,
            it falls back to other available languages or translations.
        """

        if not audio.is_youtube_source:
            raise ValueError("Audio source is not a valid YouTube URL")

        video_id = self._get_youtube_video_id(url=audio.source)
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id=video_id)
        LOGGER.debug(transcript_list)
        available_languages = self._get_available_language_codes(
            transcript_list=transcript_list
        )
        # LOGGER.debug(f"Available languages: {available_languages}")

        transcript = self._get_transcript(
            transcript_list=transcript_list,
            target_language=language,
            available_languages=available_languages,
        )

        transcript_output = transcript.fetch()

        json_output = self._get_json_output(transcript_output=transcript_output)

        json_output_formatted = self._formatted_json_output(json_output)

        return Transcription(
            json_output=json_output_formatted,
        )

    def _get_youtube_video_id(self, url: str) -> str:
        """Extract video ID from YouTube URL."""
        video_id = url.split("v=")[-1]
        return video_id

    def _get_available_language_codes(self, transcript_list: TranscriptList) -> list:
        """Return a list of available language codes for the transcript"""
        return [transcript.language_code for transcript in transcript_list]

    def _get_available_translation_language_codes(self, transcript: Transcript):
        """Return a list of available translation language codes for the transcript"""
        available_translation_codes = []

        for language in transcript.translation_languages:
            available_translation_codes.append(language["language_code"])

        return available_translation_codes

    def _get_transcript(
        self,
        transcript_list: TranscriptList,
        target_language: str,
        available_languages: list,
    ) -> Transcript:
        """Return a transcript object for the target language or a fallback"""
        if target_language in available_languages:
            return transcript_list.find_transcript([target_language])

        fallback_transcript = self._find_fallback_transcript(
            transcript_list=transcript_list, available_languages=available_languages
        )
        LOGGER.warning(
            f"Target language '{target_language}' not available. Using language '{fallback_transcript.language_code}' and trying to translate it to '{target_language}'"
        )
        return self._translate_if_possible(
            transcript=fallback_transcript, target_language=target_language
        )

    def _find_fallback_transcript(
        self, transcript_list: TranscriptList, available_languages: list
    ) -> Transcript:
        """Return a fallback transcript if the target language is unavailable"""
        for lang in self.fallback_languages:
            if lang in available_languages:
                fallback_transcript = transcript_list.find_transcript([lang])
                return fallback_transcript
        fallback_transcript = transcript_list.find_transcript(available_languages)
        return fallback_transcript

    def _translate_if_possible(
        self, transcript: Transcript, target_language: str
    ) -> Transcript:
        """Translate transcript if possible, otherwise return untranslated transcript"""
        if transcript.is_translatable:
            available_translation_language_codes = (
                self._get_available_translation_language_codes(transcript=transcript)
            )
            if target_language in available_translation_language_codes:

                return transcript.translate(target_language)

            else:
                LOGGER.warning(
                    f"Transcript cannot be translated to '{target_language}' from language '{transcript.language_code}'. Using untranslated language '{transcript.language_code}' transcript."
                )
                return transcript

        LOGGER.warning(
            f"Transcript is not translatable. Using untranslated fallback language '{transcript.language_code}' transcript."
        )
        return transcript

    def _get_json_output(self, transcript_output: str) -> str:
        """Return a dictionary of formatted transcript outputs"""

        json_output = self.formatters["json"].format_transcript(transcript_output)
        return json_output

    def _formatted_json_output(self, transcript_json_output: str) -> str:
        """Return a formatted JSON output with end times calculated"""
        transcript_json_output_dict = json.loads(transcript_json_output)

        for entry in transcript_json_output_dict:
            entry["end"] = entry["start"] + entry["duration"]
        return json.dumps(transcript_json_output_dict)

    def _end_time(self, start: float, duration: float) -> float:
        """Return end time calculated from start time and duration"""
        return start + duration


if __name__ == "__main__":
    audio = Audio(
        audio_file="C:\\Users\\janni\\Developer\\SnapScrib\\dummy.mp3",
        source="https://www.youtube.com/watch?v=JH4q65dZPvY",
    )
    y = YoutubeTranscriber()
    transcription = json.dumps(json.loads(y.transcribe(audio).json_output), indent=4)
    print(transcription)
