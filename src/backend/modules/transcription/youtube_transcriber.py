import os
from re import T
import sys
from youtube_transcript_api import YouTubeTranscriptApi
from transcriber_interface import Transcriber
from transcription_data import Transcription

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER
from modules.audio.audio_data import Audio


class YoutubeTranscriber(Transcriber):
    
    language_priority_order = [
        "en"
    ]
    
    def transcribe(audio_file: str, youtube_url: str) -> None:
        return None
    
    # def transcribe(self, audio: Audio, language: str = "en") -> Transcription:
    #     if not audio.is_youtube_source:
    #         raise ValueError("Audio source is not a valid YouTube URL")

    #     video_id = self._get_youtube_video_id(audio.source)
    #     transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    #     LOGGER.debug(transcript_list)
        
        
        
    #     if language in transcript_list:
            
    #         try:
    #             transcript = transcript_list.find_generated_transcript(
    #                 language_codes=[language]
    #             )
    #         except:
    #             for transcript in transcript_list:
    #                 if (
    #                     transcript.is_generated
    #                     or transcript.language_code == language
    #                 ):
    #                     try:
    #                         full_transcript = " ".join(
    #                             [part["text"] for part in transcript.fetch()]
    #                         )
    #                         return Transcription(full_transcript)
    #                     except Exception as e:
    #                         LOGGER.debug(f"Error fetching transcript: {e}")
    #                         continue

    #             raise Exception("No suitable transcript found.")

    #         for transcript in transcript_list:
    #             if transcript.is_generated or transcript.language_code:
    #                 try:
    #                     full_transcript = " ".join(
    #                         [part["text"] for part in transcript.fetch()]
    #                     )
    #                     return Transcription(full_transcript)
    #                 except Exception as e:
    #                     LOGGER.debug(f"Error fetching transcript: {e}")
    #                     continue

    #         raise Exception("No suitable transcript found.")
    #     except Exception as e:
    #         LOGGER.error(f"Error during transcription: {e}")
        # return None

    def _get_youtube_video_id(self, url: str) -> str:
        """Extract video ID from YouTube URL."""
        video_id = url.split("v=")[-1]
        return video_id



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
    youtube_url = "https://www.youtube.com/watch?v=xxBya1pPDe0"
    yt_transcriber = YoutubeTranscriber()
    video_id = yt_transcriber._get_youtube_video_id(url=youtube_url)
    LOGGER.debug(video_id)
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    LOGGER.debug(transcript_list)
    LOGGER.debug(type(transcript_list))
    language = "de"
    
    language_codes = []
    for transcript in transcript_list:
        language_codes.append(transcript.language_code)

    if language in language_codes:
        selected_language = language
    elif "en" in language_codes:
        selected_language = "en"
    else:
        selected_language = language_codes[0]

    LOGGER.debug(f"Selected language: {selected_language}")        


# try:
#     transcript = YT_Transcriber().transcribe(youtube_url=youtube_url)
#     if transcript:
#         print(f"Transcript: {transcript}")
#     else:
#         LOGGER.debug("Failed to retrieve a transcript.")
# except Exception as e:
#     LOGGER.debug(f"An error occurred: {e}")
