from email.mime import audio
import os
from re import T
import sys
from typing import Any
from youtube_transcript_api import YouTubeTranscriptApi
from transcriber_interface import Transcriber
from transcription_data import Transcription

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER
from modules.audio.audio_data import Audio


class YoutubeTranscriber(Transcriber):

    fallback_languages = ["en", "de"]

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

        return transcript

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
            transcript_list, available_languages
        )
        LOGGER.warning(
            f"Target language '{target_language}' not available. Using language '{fallback_transcript.language_code}' and trying to translate it to '{target_language}'"
        )
        return self._translate_if_possible(fallback_transcript, target_language)

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
                self._get_available_translation_language_codes(transcript)
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

    def _translate_transcript(self, transcript, translate_language):
        if translate_language:
            transcript_translated = transcript.translate()
        else:
            return transcript
    # def _get_transcription(self, transcript_list, language, transcript_language_codes):
    #     if language in transcript_language_codes:
    #         transcript = transcript_list.find_generated_transcript(
    #             language_codes=[language]
    #         )
    #     elif Any(self.fallback_languages) in transcript_language_codes:
    #         transcript_fallback = transcript_list.find_generated_transcript(
    #             language_codes=self.fallback_languages
    #         )
    #         if transcript_fallback.is_translatable:
    #             transcript = self._translate_transcript(
    #                 transcript=transcript_fallback,
    #                 translate_language=language
    #             )
    #         else:
    #             LOGGER.warning(
    #                 f"Fallback language transcript is not translatable to desired language, using untranslated fallback transcript."
    #             )
    #             transcript = transcript_fallback
    #     else:
    #         raise Exception(
    #             f"No suitable transcript found for desired language {language} and fallback languages {self.fallback_languages}."
    #         )
    #     return transcript



# class YT_Transcriber(Transcriber):

#     def transcribe(audio_file, youtube_url):
#         try:
#             video_id = youtube_url.split("v=")[-1]
#             transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

#             for transcript in transcript_list:
#                 if transcript.is_generated or transcript.language_code:
#                     try:
#                         full_transcript = " ".join(
#                             [part["text"] for part in transcript.fetch()]
#                         )
#                         return full_transcript
#                     except Exception as e:
#                         LOGGER.debug(f"Error fetching transcript: {e}")
#                         continue

#             raise Exception("No suitable transcript found.")
#         except Exception as e:
#             LOGGER.debug(f"Error during transcription: {e}")
#             return None


if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=MXrdD5cc6Ao"
    yt_transcriber = YoutubeTranscriber()
    audio_dummy = Audio(audio_file=None, source=youtube_url)
    language = "deas"
    transcript = yt_transcriber.transcribe(audio=audio_dummy, language=language)
    LOGGER.debug(transcript.translation_languages)


# try:
#     transcript = YT_Transcriber().transcribe(youtube_url=youtube_url)
#     if transcript:
#         print(f"Transcript: {transcript}")
#     else:
#         LOGGER.debug("Failed to retrieve a transcript.")
# except Exception as e:
#     LOGGER.debug(f"An error occurred: {e}")
