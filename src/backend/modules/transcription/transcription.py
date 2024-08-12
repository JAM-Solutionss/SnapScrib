import os
import sys
import time
from youtube_transcript_api import YouTubeTranscriptApi

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from audio.audio_extractor_factory import get_audio_extractor

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.logger_config import LOGGER
from modules.transcription.transcribe_whisper import transcribe_audio as whisper

if sys.platform == 'darwin':
    from modules.transcription.transcribe_mlx import transcribe as mlx
    from modules.transcription.transcribe_with_lightning_mlx import transcribe as lightning

class Transcription:

    def transcribe(self, source, method=2):
        """ transcription methods 
        1 -- yt subtitle 
        2 -- mlx/whisper
        """

        self.source, yt = get_audio_extractor(source)

        if yt:
            if method == 1: 
                return self.transcribe_yt_subtitle(self.source)
            elif method == 2:
                return self.transcribe_yt_audio(self.source)
            
        else:
            raise ValueError("Non-YouTube sources are not supported yet.")

    def transcribe_yt_subtitle(self, youtube_url):
        
        try:
            video_id = youtube_url.split("v=")[-1]
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

            for transcript in transcript_list:
                if transcript.is_generated or transcript.language_code:
                    try:
                        full_transcript = " ".join([part['text'] for part in transcript.fetch()])
                        return full_transcript, transcript.language_code
                    except Exception as e:
                        LOGGER.debug(f"Error fetching transcript: {e}")
                        continue

            raise Exception("No suitable transcript found.")
        except Exception as e:
            LOGGER.debug(f"Error during transcription: {e}")
            return None, None

    def transcribe_yt_audio(self, file):
        self.check_os(file)

    def check_os(self, filename, path='data'):
        system = sys.platform
        if system == "darwin":
            LOGGER.info("This system is running macOS.")
            LOGGER.debug("Choosing transcription method...")
            # choose = input("Choose 1: mlx or 2: lightning mlx: ")
            choose = 2

            if choose == "1":
                mlx(path, filename)
            else:
                lightning(path, filename)

                
        elif system == "win32":
            LOGGER.info("This system is running Windows.")
            whisper(path, filename)

        elif system == "linux":
            LOGGER.info("This system is running Linux.")
            whisper(path, filename)

        else:
            LOGGER.error("Unknown operating system.")


if __name__ == '__main__':
    youtube_url = "https://www.youtube.com/watch?v=iXIwm4mCpuc"
    try:
        transcript, language_code = Transcription().transcribe(youtube_url)
        if transcript:
            print(f"Transcript: {transcript}")
            print(f"Detected language: {language_code}")
        else:
            LOGGER.debug("Failed to retrieve a transcript.")
    except Exception as e:
        LOGGER.debug(f"An error occurred: {e}")