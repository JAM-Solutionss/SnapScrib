from email.mime import audio
import sys
import os
from transcriber_factory import get_transcriber

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from modules.audio.audio_data import Audio
from utils.logger_config import LOGGER


def test_YoutubeTranscriber() -> None:
    yt_url = "https://www.youtube.com/watch?v=-HV0B8pHjuA"
    transcriber_class = get_transcriber("youtube")
    youtube_transcriber = transcriber_class()
    audio_dummy = Audio(audio_file=None, source=yt_url)
    target_language = "de"
    transcription = youtube_transcriber.transcribe(
        audio=audio_dummy, language=target_language
    )
    LOGGER.debug(transcription.json_output)
    LOGGER.debug(transcription.json_output_dict)
    LOGGER.debug(transcription.text_output)


def test_WhisperTranscriber() -> None:
    current_dir = os.getcwd()
    audio_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))),
        r"youtube_audio\output\audio.mp3",
    )
    print(audio_file)

    audio = Audio(audio_file=audio_file, source=audio_file)
    transcriber_class = get_transcriber("whisper")
    whisper_transcriber = transcriber_class()
    transcription = whisper_transcriber.transcribe(audio=audio)
    LOGGER.debug(transcription.json_output)
    LOGGER.debug(transcription.json_output_dict)
    LOGGER.debug(transcription.text_output)


if __name__ == "__main__":
    # test_YoutubeTranscriber()
    test_WhisperTranscriber()
