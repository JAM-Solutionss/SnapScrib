import yt_dlp
import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))
from logger_config import LOGGER


# yt-dlp --split-chapters -x --audio-format 'mp3'  'https://www.youtube.com/watch?v=6lSLyERSuh4&pp=ygULbXA0IGNoYXB0ZXI%3D'
def download_youtube_video_as_audio_chapter(url):
    try:        
        snapscrib_directory = os.getcwd()
        os.chdir('out')
        # output_path = "out"
        # # the postprocessor (probably can't use output_path, therefore it will just be dumped into the new working directory
        # Set up yt-dlp options
        ydl_opts = {
            'format': 'bestaudio',
            'overwrite': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },{
                'key': 'FFmpegSplitChapters',
                'force_keyframes': True,
            }],
            # 'outtmpl': os.path.join(output_path, '%()s.%(ext)s'), TODO fix titles
        }
        
        # Download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
            LOGGER.info(f"Audio file downloaded to: {snapscrib_directory}/out")
        os.chdir(snapscrib_directory)
        print(os.getcwd())
        
    except Exception as e:
        LOGGER.error(f"An error occurred: {e}")
        if snapscrib_directory != os.getcwd(): # could change anyways TODO find out which is faster
            os.chdir(snapscrib_directory)
            print(os.getcwd())
            LOGGER.info(f"Changed directory back to: {snapscrib_directory}")

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


if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=6lSLyERSuh4&pp=ygULbXA0IGNoYXB0ZXI%3D'
    start = time.time()
    download_youtube_video_as_audio_chapter(url)
    self_made = time.time() - start
    print(self_made)