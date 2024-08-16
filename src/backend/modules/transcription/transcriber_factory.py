import sys
from src.backend.modules.transcription.lightning_mlx_transcriber import (
    LightningMlxTranscriber,
)
from src.backend.modules.transcription.mlx_transcriber import MlxTranscriber
from src.backend.modules.transcription.trranscriber_interface import Transcriber
from src.backend.modules.transcription.whisper_transcriber import WhisperTranscriber
from src.backend.modules.transcription.youtube_transcriber import YoutubeTranscriber


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

    operating_system = sys.platform

    if transcriber_type.lower() is None:
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
