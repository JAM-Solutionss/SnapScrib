from youtube_transcript_api import YouTubeTranscriptApi
import time

def get_transcript(youtube_url):
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



if __name__ == "__main__":

    start_time = time.time()

    youtube_url = "https://www.youtube.com/watch?v=iXIwm4mCpuc"
    try:
        transcript, language_code = get_transcript(youtube_url)
        print(f"Transcript: {transcript}")
        print(f"Detected language: {language_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

    end_time = time.time()
    print(f"Execution time: {round(end_time - start_time, 3)} seconds")