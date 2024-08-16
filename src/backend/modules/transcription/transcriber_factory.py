import sys
from src.backend.modules.transcription.lightning_mlx_transcriber import (
    LightningMlxTranscriber,
)
from src.backend.modules.transcription.mlx_transcriber import MlxTranscriber
from src.backend.modules.transcription.trranscriber_interface import Transcriber
from src.backend.modules.transcription.whisper_transcriber import WhisperTranscriber

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
}


def get_transcriber(type: str = None) -> Transcriber:
    """
    Get the appropriate transcriber instance based on the specified type and the current operating system.

    Args:
        type (str, optional): The type of transcriber to get. If not provided, the first supported transcriber will be returned.

    Returns:
        Transcriber: The transcriber class.

    Raises:
        ValueError: If the specified transcriber type is not supported on the current operating system, or if none transcriber is supported on the current operating system.
    """

    operating_system = sys.platform

    if type.lower() is None:
        for name, transcriber_info in transcribers.items():
            if operating_system in transcriber_info["supported_operating_systems"]:
                return transcriber_info["transcriber_class"]
        raise ValueError(
            f"No transcriber is supported on this operating system: {operating_system}"
        )
    else:
        if type.lower() in transcribers:
            if operating_system in transcribers[type]["supported_operating_systems"]:
                return transcribers[type]["transcriber_class"]
            else:
                raise ValueError(
                    f"Transcriber '{type}' is not supported on this operating system."
                )
        else:
            raise ValueError(f"Unknown transcriber type: {type}")
