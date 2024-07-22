from lightning_whisper_mlx import LightningWhisperMLX
from datetime import timedelta
import json
import os




def transcribe(path, filename):
    print("transcribing....")
    whisper = LightningWhisperMLX(model="distil-large-v3", batch_size=12, quant=None)
    result = whisper.transcribe(path)
    #print(result["segments"])
    srt_content = (create_srt(result["segments"]))
    srtFilename = os.path.join("transcription/SrtFiles", f"{filename}.srt")
    with open(srtFilename, 'a', encoding='utf-8') as srtFile:
        srtFile.write(srt_content)
    
    writefile_json(create_json(result["segments"]))

def convert_millis(millis):
    """Convert milliseconds to hh:mm:ss,ms format."""
    seconds = (millis / 1000) % 60
    minutes = (millis / (1000 * 60)) % 60
    hours = (millis / (1000 * 60 * 60)) % 24
    millis = millis % 1000
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(millis):03}"

def create_json(transcription):
    """Create JSON file content from transcription data."""
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
    srt_content = []
    for idx, (start, end, text) in enumerate(transcription, start=1):
        start_time = convert_millis(start)
        end_time = convert_millis(end)
        srt_content.append(f"{idx}\n{start_time} --> {end_time}\n{text}\n")
       
    return "\n".join(srt_content)


def writefile_json(input):
    print("Writing JSON file to OS...")
    file_path = "transcription/json_files/transcription.json"
    with open(file_path, "w") as file:
        json.dump(input, file, indent=2)
    
    


if __name__ == "__main__":
    transcribe()
    #print(save)