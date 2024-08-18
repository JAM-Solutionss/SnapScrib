from dataclasses import dataclass
import json

@dataclass
class Transcription:
    """
    Transcription dataclass, that holds the transcription data.
    
    Attributes:
        json_output: dict - JSON output from transcription model in the format of (timestamps in seconds): 
        [{"text": "Hey there", "start": 7.58, "duration": 1.29, "end": 8.87}, ...]
    """
    json_output: dict
    
    @property
    def json_output_dict(self):
        """Returns the json_output as a dict for easy access"""
        return json.loads(self.json_output)
    
    @property
    def text_output(self):
        """Returns the transcription text extracted from json_output"""

        text = ""
        for segment in self.json_output_dict:
            text += segment["text"]

        return text
