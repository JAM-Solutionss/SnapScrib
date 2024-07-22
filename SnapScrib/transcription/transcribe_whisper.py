from datetime import timedelta
import os
import whisper
import json

def transcribe_audio(path, filename):
    model = whisper.load_model("base") # Change this to your desired model
    print("Whisper model loaded.")
    transcribe = model.transcribe(audio=path)
    segments = transcribe['segments']


    json_output = []
    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

        srtFilename = os.path.join("SrtFiles", f"{filename}.srt")
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
    print("Writing JSON file to OS...")
    file_path = "json_files/transcription.json"
    with open(file_path, "w") as file:
        json.dump(input, file, indent=2)
    
  



if __name__ == "__main__":
    transcribe_audio("audio.ogg")