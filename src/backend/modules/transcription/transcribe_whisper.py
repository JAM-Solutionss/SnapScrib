from datetime import timedelta
import os
import whisper
import json
import torch
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))
from logger_config import LOGGER


def transcribe_audio(path, filename):
    torch.cuda.init()
    device = "cuda"

    model = whisper.load_model("base").to(device=device)  # Change this to your desired model
    LOGGER.info("Whisper model loaded.")
    with torch.cuda.device(device):
        transcribe = model.transcribe(audio=path)
    segments = transcribe['segments']

    json_output = []
    for segment in segments:
        startTime = str(0) + str(timedelta(seconds=int(segment['start']))) + ',000'
        endTime = str(0) + str(timedelta(seconds=int(segment['end']))) + ',000'
        text = segment['text']
        segmentId = segment['id'] + 1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

        srt_directory = os.path.join("transcription", "SrtFiles")
        os.makedirs(srt_directory, exist_ok=True)
        srtFilename = os.path.join(srt_directory, f"{filename}.srt")
        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)
        segment_dict = {
            "id": segmentId,
            "start_time": startTime,
            "end_time": endTime,
            "text": text[1:] if text[0] == ' ' else text
        }
        json_output.append(segment_dict)
    writefile(json_output)

    return srtFilename

def writefile(input):
    LOGGER.info("Writing JSON file to OS...")

    json_directory = os.path.join("transcription", "json_files")
    os.makedirs(json_directory, exist_ok=True)
    jsonFilename = os.path.join(json_directory, f"transcription.json")
    with open(jsonFilename, "w") as file:
        json.dump(input, file, indent=2)

if __name__ == "__main__":
    test_path = "out/audiofile.ogg"
    test_filename = "test_output"
    transcribe_audio(test_path, test_filename)