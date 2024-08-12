import os
import sys
from youtube_transcript_api import YouTubeTranscriptApi

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from transcriber.transcriber_blueprint import Transcriber

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.logger_config import LOGGER

class YT_Transcriber(Transcriber):

    def transcribe(self, audio_file, youtube_url):
        try:
            video_id = youtube_url.split("v=")[-1]
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

            for transcript in transcript_list:
                if transcript.is_generated or transcript.language_code:
                    try:
                        full_transcript = " ".join([part['text'] for part in transcript.fetch()])
                        return full_transcript
                    except Exception as e:
                        LOGGER.debug(f"Error fetching transcript: {e}")
                        continue

            raise Exception("No suitable transcript found.")
        except Exception as e:
            LOGGER.debug(f"Error during transcription: {e}")
            return None


if __name__ == '__main__':
    youtube_url = "https://www.youtube.com/watch?v=iXIwm4mCpuc"
    try:
        transcript = YT_Transcriber().transcribe('', youtube_url)
        if transcript:
            print(f"Transcript: {transcript}")
        else:
            LOGGER.debug("Failed to retrieve a transcript.")
    except Exception as e:
        LOGGER.debug(f"An error occurred: {e}")