import os
import sys
import time
from youtube_transcript_api import YouTubeTranscriptApi

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from audio.audio_extractor_factory import get_audio_extractor

class Transcription:

    def transcribe(self, source):
        temp, yt = get_audio_extractor(source)

        if yt:
            return self.transcribe_yt(temp)
        else:
            raise ValueError("Non-YouTube sources are not supported yet.")

    def transcribe_yt(self, youtube_url):
        try:
            video_id = youtube_url.split("v=")[-1]
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

            for transcript in transcript_list:
                if transcript.is_generated or transcript.language_code:
                    try:
                        full_transcript = " ".join([part['text'] for part in transcript.fetch()])
                        return full_transcript, transcript.language_code
                    except Exception as e:
                        print(f"Error fetching transcript: {e}")
                        continue

            raise Exception("No suitable transcript found.")
        except Exception as e:
            print(f"Error during transcription: {e}")
            return None, None

if __name__ == '__main__':
    start_time = time.time()

    youtube_url = "https://www.youtube.com/watch?v=iXIwm4mCpuc"
    try:
        transcript, language_code = Transcription().transcribe(youtube_url)
        if transcript:
            print(f"Transcript: {transcript}")
            print(f"Detected language: {language_code}")
        else:
            print("Failed to retrieve a transcript.")
    except Exception as e:
        print(f"An error occurred: {e}")

    end_time = time.time()
    print(f"Execution time: {round(end_time - start_time, 3)} seconds")