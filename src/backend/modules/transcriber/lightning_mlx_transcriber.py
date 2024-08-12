import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from transcriber.transcriber_blueprint import Transcriber

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.logger_config import LOGGER

if sys.platform == 'darwin':
    from lightning_whisper_mlx import LightningWhisperMLX

class Lightning_MLX_Transcriber(Transcriber):
    def transcribe(self, audio_file: str) -> str:
        LOGGER.info("transcribing....")
        whisper = LightningWhisperMLX(model="distil-large-v3", batch_size=12, quant=None)
        result = whisper.transcribe(audio_file)
        print(result)
        srt_content = self.create_srt(result["segments"])
        
        #srt_directory = os.path.join("transcription", "SrtFiles")
        #os.makedirs(srt_directory, exist_ok=True)
        #srtFilename = os.path.join(srt_directory, f"{filename}.srt")
        #with open(srtFilename, 'a', encoding='utf-8') as srtFile:
        #    srtFile.write(srt_content)
        
        # return self.create_json(result["segments"])
        return result["segments"]

    def convert_millis(self, millis):
        """Convert milliseconds to hh:mm:ss,ms format."""
        LOGGER.info("Converting milliseconds to hh:mm:ss,ms format...")
        seconds = (millis / 1000) % 60
        minutes = (millis / (1000 * 60)) % 60
        hours = (millis / (1000 * 60 * 60)) % 24
        millis = millis % 1000
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(millis):03}"

    def create_json(self, transcription):
        """Create JSON file content from transcription data."""
        LOGGER.info("Creating JSON file content...")
        json_content = []
        for idx, (start, end, text) in enumerate(transcription, start=1):
            segment = {
                "index": idx,
                "start_time": self.convert_millis(start),
                "end_time": self.convert_millis(end),
                "text": text
            }
            json_content.append(segment)
            
        return json_content

    def create_srt(self, transcription):
        """Create SRT file content from transcription data."""
        LOGGER.info("Creating SRT file content...")
        srt_content = []
        for idx, (start, end, text) in enumerate(transcription, start=1):
            start_time = self.convert_millis(start)
            end_time = self.convert_millis(end)
            srt_content.append(f"{idx}\n{start_time} --> {end_time}\n{text}\n")
        
        return "\n".join(srt_content)