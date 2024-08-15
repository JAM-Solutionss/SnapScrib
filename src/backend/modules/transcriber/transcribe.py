import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from modules.transcriber.whisper_transcriber import Whisper_Transcriber as whisper
from utils.logger_config import LOGGER

from yt_transcriber import YT_Transcriber as youtube

if sys.platform == "darwin":
    from modules.transcriber.mlx_transcriber import MLX_Transcriber as mlx
    from modules.transcriber.lightning_mlx_transcriber import (
        Lightning_MLX_Transcriber as lightning,
    )


def get_transcription():
    system = sys.platform
    if system == "darwin":
        LOGGER.info("This system is running macOS.")
        LOGGER.debug("Choosing transcription method...")
        choose = input("Choose 1: mlx or 2: lightning mlx: 3: YT transcription")
        if choose == "1":
            return mlx
        elif choose == "2":
            return lightning
        else:
            return youtube

    elif system == "win32":
        LOGGER.info("This system is running Windows.")
        return whisper

    elif system == "linux":
        LOGGER.info("This system is running Linux.")
        return whisper

    else:
        LOGGER.error("Unknown operating system.")
