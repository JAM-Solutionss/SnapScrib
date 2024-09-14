from youtube_transcript_api import YouTubeTranscriptApi

class Youtube():
    def transcribe(self, url):
        video_id = url.split("v=")[-1]
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