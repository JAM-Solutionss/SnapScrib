from datetime import timedelta
import json
import os
import sys
from src.backend.utils.logger_config import LOGGER  # Korrigierter Import

if sys.platform == 'darwin':
    from lightning_whisper_mlx import LightningWhisperMLX

def transcribe(path, filename):
    LOGGER.info("transcribing....")
    whisper = LightningWhisperMLX(model="distil-large-v3", batch_size=12, quant=None)
    result = whisper.transcribe(path)
    srt_content = create_srt(result["segments"])
    srt_directory = os.path.join("transcription", "SrtFiles")
    os.makedirs(srt_directory, exist_ok=True)
    srtFilename = os.path.join(srt_directory, f"{filename}.srt")
    with open(srtFilename, 'a', encoding='utf-8') as srtFile:
        srtFile.write(srt_content)
    
    writefile_json(create_json(result["segments"]))

def convert_millis(millis):
    """Convert milliseconds to hh:mm:ss,ms format."""
    LOGGER.info("Converting milliseconds to hh:mm:ss,ms format...")
    seconds = (millis / 1000) % 60
    minutes = (millis / (1000 * 60)) % 60
    hours = (millis / (1000 * 60 * 60)) % 24
    millis = millis % 1000
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(millis):03}"

def create_json(transcription):
    """Create JSON file content from transcription data."""
    LOGGER.info("Creating JSON file content...")
    json_content = []
    for idx, (start, end, text) in enumerate(transcription, start=1):
        segment = {
            "index": idx,
            "start_time": convert_millis(start),
            "end_time": convert_millis(end),
            "text": text
        }
        json_content.append(segment)
        
    return json_content

def create_srt(transcription):
    """Create SRT file content from transcription data."""
    LOGGER.info("Creating SRT file content...")
    srt_content = []
    for idx, (start, end, text) in enumerate(transcription, start=1):
        start_time = convert_millis(start)
        end_time = convert_millis(end)
        srt_content.append(f"{idx}\n{start_time} --> {end_time}\n{text}\n")
       
    return "\n".join(srt_content)

def writefile_json(input):
    LOGGER.info("Writing JSON file to OS...")

    json_directory = os.path.join("transcription", "json_files")
    os.makedirs(json_directory, exist_ok=True)
    jsonFilename = os.path.join(json_directory, f"transcription.json")
    with open(jsonFilename, "w") as file:
        json.dump(input, file, indent=2)

if __name__ == "__main__":
    test_path = "out/audiofile.wav"
    test_filename = "test_output"
    transcribe(test_path, test_filename)