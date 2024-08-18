from modules.audio.audio_data import Audio
from utils.logger_config import LOGGER
import os
import sys
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter, TextFormatter
from transcriber_interface import Transcriber
from transcription_data import Transcription
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


class YoutubeTranscriber(Transcriber):

    fallback_languages = ["en", "de"]

    formatters = {"json": JSONFormatter(), "text": TextFormatter()}

    def transcribe(self, audio: Audio, language: str = fallback_languages[0]) -> None:

        if not audio.is_youtube_source:
            raise ValueError("Audio source is not a valid YouTube URL")

        video_id = self._get_youtube_video_id(audio.source)
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        LOGGER.debug(transcript_list)
        available_languages = self._get_available_language_codes(transcript_list)
        # LOGGER.debug(f"Available languages: {available_languages}")

        transcript = self._get_transcript(
            transcript_list=transcript_list,
            target_language=language,
            available_languages=available_languages,
        )

        transcript_output = transcript.fetch()

        formatted_transcript_outputs = self._get_formatted_transcripts(
            transcript_output=transcript_output
        )

        return Transcription(
            text=formatted_transcript_outputs["text"],
            json_output=self._formatted_json_output(
                formatted_transcript_outputs["json"]
            ),
        )

        # return transcript

    def _get_youtube_video_id(self, url: str) -> str:
        """Extract video ID from YouTube URL."""
        video_id = url.split("v=")[-1]
        return video_id

    def _get_available_language_codes(self, transcript_list):
        return [transcript.language_code for transcript in transcript_list]

    def _get_available_translation_language_codes(self, transcript):
        available_translation_codes = []

        for language in transcript.translation_languages:
            available_translation_codes.append(language["language_code"])

        return available_translation_codes

    def _get_transcript(self, transcript_list, target_language, available_languages):
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

    def _find_fallback_transcript(self, transcript_list, available_languages):

        for lang in self.fallback_languages:
            if lang in available_languages:
                fallback_transcript = transcript_list.find_transcript([lang])
                return fallback_transcript
        fallback_transcript = transcript_list.find_transcript(available_languages)
        return fallback_transcript

    def _translate_if_possible(self, transcript, target_language):

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

    def _get_formatted_transcripts(self, transcript_output) -> dict:

        formatted_transcripts = {}
        for formatter_name, formatter in self.formatters.items():
            LOGGER.debug(f"Formatting transcript to {formatter_name} format")
            LOGGER.debug(formatter)
            formatted_transcripts[formatter_name] = formatter.format_transcript(
                transcript_output
            )

        return formatted_transcripts

    def _formatted_json_output(self, transcript_json_output):
        transcript_json_output_dict = json.loads(transcript_json_output)

        for entry in transcript_json_output_dict:
            entry["end"] = entry["start"] + entry["duration"]
        return transcript_json_output_dict

    def _end_time(self, start: float, duration: float):
        return start + duration

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=MXrdD5cc6Ao"
    yt_transcriber = YoutubeTranscriber()
    audio_dummy = Audio(audio_file=None, source=youtube_url)
    language = "deas"
    transcript = yt_transcriber.transcribe(audio=audio_dummy, language=language)
    LOGGER.debug(transcript.json_output)
    LOGGER.debug(transcript.text)
