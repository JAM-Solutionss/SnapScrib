import sys
from src.backend.modules.transcription.trranscriber_interface import Transcriber

transcribers = {
    "whisper": {
        'supported_operating_systems': []
    }
}

def get_transcriber(type: str= None) -> Transcriber:
    operating_system = sys.platform
    if operating_system == "darwin":
        LOGGER.info("This system is running macOS.")
        LOGGER.debug("Choosing transcription method...")
        choose = input("Choose 1: mlx or 2: lightning mlx: 3: YT transcription")
        if choose == "1":
            return MLX_Transcriber
        elif choose == "2":
            return Lightning_MLX_Transcriber
        else:
            return YT_Transcriber

    elif operating_system == "win32":
        LOGGER.info("This system is running Windows.")
        return Whisper_Transcriber

    elif operating_system == "linux":
        LOGGER.info("This system is running Linux.")
        return Whisper_Transcriber

    else:
        LOGGER.error("Unknown operating system.")
        return None    