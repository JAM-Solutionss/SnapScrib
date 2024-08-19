import yt_dlp
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.logger_config import LOGGER

def download_youtube_video_as_audio(url, output_dir="out"):
    try:
        # Ensure the output directory exists
        os.makedirs(output_path, exist_ok=True)

        # Set up yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, 'audio'),
        }

        # Download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        LOGGER.info(f"Audio file downloaded to: {os.path.join(os.path.abspath(output_path), 'audio.mp3')}")
    except Exception as e:
        LOGGER.error(f"An error occurred: {e}")


if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ").strip()
    
    if url:
        output_path = "data"
        download_youtube_video_as_audio(url, output_path)
    else:
        LOGGER.error("No URL provided.")
        print("Please provide a valid YouTube video URL.")