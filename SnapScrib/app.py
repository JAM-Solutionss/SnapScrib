from transcription.transcribe import check_os
from youtube_audio.extract_audio import download_youtube_video_as_audio




if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=iXIwm4mCpuc"
    output= "./youtube_audio/output/audio.mp3"
    filename= "transcription"
    # downloads the audio from the youtube video
    download_youtube_video_as_audio(url)
    # checks which operating system is used and runs the appropriate command
    # then it will trigger the transcription process
    check_os(output, filename)
    