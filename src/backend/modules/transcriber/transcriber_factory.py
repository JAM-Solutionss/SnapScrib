import sys
import os
from typing import Type

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from modules.transcriber.transcriber_interface import Transcriber
from modules.transcriber.whisper_transcriber import Whisper_Transcriber
from utils.logger_config import LOGGER

from yt_transcriber import YT_Transcriber

if sys.platform == "darwin":
    from modules.transcriber.mlx_transcriber import MLX_Transcriber
    from modules.transcriber.lightning_mlx_transcriber import Lightning_MLX_Transcriber


def get_transcriber() -> Type[Transcriber]:
    system = sys.platform
    if system == "darwin":
        LOGGER.info("This system is running macOS.")
        LOGGER.debug("Choosing transcription method...")
        choose = input("Choose 1: mlx or 2: lightning mlx: 3: YT transcription")
        if choose == "1":
            return MLX_Transcriber
        elif choose == "2":
            return Lightning_MLX_Transcriber
        else:
            return YT_Transcriber

    elif system == "win32":
        LOGGER.info("This system is running Windows.")
        return Whisper_Transcriber

    elif system == "linux":
        LOGGER.info("This system is running Linux.")
        return Whisper_Transcriber

    else:
        LOGGER.error("Unknown operating system.")
        return None


if __name__ == "__main__":
    transcriber = get_transcriber()
    if transcriber:
        LOGGER.info(f"Using transcriber: {transcriber.__class__.__name__}")
    else:
        LOGGER.error("Failed to choose a transcriber.")
