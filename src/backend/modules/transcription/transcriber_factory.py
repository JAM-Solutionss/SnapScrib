import sys
import os
from lightning_mlx_transcriber import LightningMlxTranscriber
from mlx_transcriber import MlxTranscriber
from transcriber_interface import Transcriber
from whisper_transcriber import WhisperTranscriber
from youtube_transcriber import YoutubeTranscriber

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER

operating_system = sys.platform

# System-specific transcriber classes
transcribers = {
    "whisper": {
        "supported_operating_systems": ["win32", "linux"],
        "transcriber_class": WhisperTranscriber,
    },
    "mlx": {
        "supported_operating_systems": ["darwin"],
        "transcriber_class": MlxTranscriber,
    },
    "lightning_mlx": {
        "supported_operating_systems": ["darwin"],
        "transcriber_class": LightningMlxTranscriber,
    },
    "youtube": {
        "supported_operating_systems": ["win32", "linux", "darwin"],
        "transcriber_class": YoutubeTranscriber,
    },
}


def get_transcriber(transcriber_type: str = None) -> Transcriber:
    """
    Get the appropriate transcriber class based on the specified type and the current operating system.

    Args:
        transcriber_type (str, optional): The type of transcriber to get. If not provided, the first supported transcriber will be returned.
            Possible options:
            - "whisper": Whisper transcriber (supported on Windows and Linux)
            - "mlx": MLX transcriber (supported on macOS)
            - "lightning_mlx": Lightning MLX transcriber (supported on macOS)
            - "youtube": YouTube transcriber (supported on all OSes)

    Returns:
        Transcriber: The transcriber class.

    Raises:
        ValueError: If the specified transcriber type is not supported on the current operating system, or if none transcriber is supported on the current operating system.
    """

    if transcriber_type is None:
        for name, transcriber_info in transcribers.items():
            if operating_system in transcriber_info["supported_operating_systems"]:
                return transcriber_info["transcriber_class"]
        raise ValueError(
            f"No transcriber is supported on this operating system: {operating_system}"
        )
    else:
        if transcriber_type.lower() in transcribers:
            if operating_system in transcribers[transcriber_type]["supported_operating_systems"]:
                return transcribers[transcriber_type]["transcriber_class"]
            else:
                raise ValueError(
                    f"Transcriber '{transcriber_type}' is not supported on this operating system."
                )
        else:
            raise ValueError(f"Unknown transcriber type: {transcriber_type}")



# from yt_transcriber import YT_Transcriber

# if sys.platform == "darwin":
#     from modules.transcriber.mlx_transcriber import MLX_Transcriber
#     from modules.transcriber.lightning_mlx_transcriber import Lightning_MLX_Transcriber


# def get_transcriber() -> Type[Transcriber]:
#     system = sys.platform
#     if system == "darwin":
#         LOGGER.info("This system is running macOS.")
#         LOGGER.debug("Choosing transcription method...")
#         choose = input("Choose 1: mlx or 2: lightning mlx: 3: YT transcription")
#         if choose == "1":
#             return MLX_Transcriber
#         elif choose == "2":
#             return Lightning_MLX_Transcriber
#         else:
#             return YT_Transcriber

#     elif system == "win32":
#         LOGGER.info("This system is running Windows.")
#         return Whisper_Transcriber

#     elif system == "linux":
#         LOGGER.info("This system is running Linux.")
#         return Whisper_Transcriber

#     else:
#         LOGGER.error("Unknown operating system.")
#         return None


# if __name__ == "__main__":
    # transcriber = get_transcriber()
    # if transcriber:
    #     LOGGER.info(f"Using transcriber: {transcriber.__class__.__name__}")
    # else:
    #     LOGGER.error("Failed to choose a transcriber.")
