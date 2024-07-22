from datetime import timedelta
import os
import mlx_whisper
import json




def transcribe():
    path_or_hf_repo = "mlx-community/whisper-large-v3-mlx"
    speech_file = "audio.ogg"
    print("transcribing....")
    result = mlx_whisper.transcribe(speech_file ,word_timestamps=True)
    text = result["text"]
    print(text)
    segments = result['segments']


    json_output = []

    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

        srtFilename = os.path.join("SrtFiles", f"VIDEO_FILENAME.srt")
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
    file_path = "json_files/transcription_mlx.json"
    with open(file_path, "w") as file:
        json.dump(input, file, indent=2)
    
    print("Writing JSON file to OS...")


if __name__ == "__main__":
    transcribe()
    #print(save)