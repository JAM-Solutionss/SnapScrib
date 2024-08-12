from logging import Logger
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.logger_config import LOGGER

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from modules.transcription.transcribe_whisper import transcribe_audio as whisper

if sys.platform == 'darwin':
    from transcription.transcribe_mlx import transcribe as mlx
    from transcription.transcribe_with_lightning_mlx import transcribe as lightning


def check_os(path, filename):
    system = sys.platform
    if system == "darwin":
        LOGGER.info("This system is running macOS.")
        Logger.debug("Choosing transcription method...")
        choose = input("Choose 1: mlx or 2: lightning mlx: ")
        if choose == "1":
            mlx(path, filename)
        else:
            lightning(path, filename)

            
    elif system == "win32":
        LOGGER.info("This system is running Windows.")
        whisper(path, filename)

    elif system == "linux":
        LOGGER.info("This system is running Linux.")
        whisper(path, filename)

    else:
        LOGGER.error("Unknown operating system.")



if __name__ == "__main__":
    check_os()