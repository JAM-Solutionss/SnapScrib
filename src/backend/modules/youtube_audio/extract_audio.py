import yt_dlp
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))
from logger_config import LOGGER

def download_youtube_video_as_audio(url):
    try:
        # Set up yt-dlp options
        output_path = "out"
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, 'audio.%(ext)s'),
        }

        # Download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        LOGGER.info(f"Audio file downloaded to: {output_path}")
    except Exception as e:
        LOGGER.error(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    #output_path = input("Enter the output path (e.g., './downloads'): ")
    download_youtube_video_as_audio(url)

