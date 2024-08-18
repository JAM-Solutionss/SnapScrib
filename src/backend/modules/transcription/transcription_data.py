from dataclasses import dataclass

@dataclass
class Transcription:
    """
    Transcription dataclass, that holds the transcription data.
    
    Attributes:
        text: str - Transcription text
        json_output: dict - JSON output from transcription model in the format of (timestamps in seconds): [{"text": "Hey there", "start": 7.58, "end": 8.87, "duration": 1.29}, ...]
    """
    text: str
    json_output: dict
