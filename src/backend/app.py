from transcription.transcribe import check_os
from youtube_audio.extract_audio import download_youtube_video_as_audio
from src.backend.utils.logger_config import LOGGER




if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=iXIwm4mCpuc"
    output= "./youtube_audio/output/audio.mp3"
    filename= "transcription"
    # downloads the audio from the youtube video
    LOGGER.info("Downloading audio from YouTube video...")
    download_youtube_video_as_audio(url)
    # checks which operating system is used and runs the appropriate command
    # then it will trigger the transcription process
    LOGGER.info("Transcribing audio...")
    check_os(output, filename)
    