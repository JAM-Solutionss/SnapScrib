from email.mime import audio
import sys
import os

from numpy import source

from transcriber_factory import get_transcriber

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from modules.audio.audio_data import Audio
from utils.logger_config import LOGGER

if __name__ == "__main__":
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # print(f"current_dir: {current_dir}")
    # source_file = os.path.join(current_dir, "..", "..", "..", "..", "data", "audio.mp3")

    # url = "https://www.youtube.com/watch?v=-HV0B8pHjuA"

    # transcription = get_transcription().transcribe(
    #     audio_file=source_file, youtube_url=url
    # )
    # LOGGER.info(f"RETURN: {transcription}")

    ### --- Testing transcriber factory --- ###
    # transcriber = get_transcriber()
    # print(transcriber)

    # transcriber = get_transcriber("whisper")
    # print(transcriber)

    # transcriber = get_transcriber("lightning_mlx")
    # print(transcriber)

    # transcriber = get_transcriber("mlx")
    # print(transcriber)

    # transcriber = get_transcriber("youtube")
    # print(transcriber)

    # transcriber = get_transcriber("WhiSper")
    # print(transcriber)

    # transcriber = get_transcriber("lIghtning_mLx")
    # print(transcriber)

    # transcriber = get_transcriber("MLX")
    # print(transcriber)

    # transcriber = get_transcriber("YouTube")
    # print(transcriber)

    # transcriber = get_transcriber("irgendwas")
    # print(transcriber)

    ### Testing YoutubeTranscriber ###

    # yt_url = "https://www.youtube.com/watch?v=-HV0B8pHjuA"
    # transcriber_class = get_transcriber("youtube")
    # youtube_transcriber = transcriber_class()
    # audio_dummy = Audio(audio_file=None, source=yt_url)
    # target_language = "de"
    # transcription = youtube_transcriber.transcribe(
    #     audio=audio_dummy, language=target_language
    # )
    # LOGGER.debug(transcription.json_output)
    # LOGGER.debug(transcription.json_output_dict)
    # LOGGER.debug(transcription.text)
    
    ### Testing WhisperTranscriber ###
    current_dir = os.getcwd()
    audio_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))), r"youtube_audio\output\audio.mp3")
    print(audio_file)
    

    audio = Audio(audio_file=audio_file, source=audio_file)
    transcriber_class = get_transcriber("whisper")
    whisper_transcriber = transcriber_class()
    transcription = whisper_transcriber.transcribe(audio=audio)
