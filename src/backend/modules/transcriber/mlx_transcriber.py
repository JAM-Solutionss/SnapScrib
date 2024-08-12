from datetime import timedelta
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from transcriber.transcriber_blueprint import Transcriber

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.logger_config import LOGGER

if sys.platform == 'darwin':
    import mlx_whisper

class MLX_Transcriber(Transcriber):
    def transcribe(audio_file: str):
        path_or_hf_repo = "mlx-community/whisper-large-v3-mlx"
        speech_file = audio_file
        result = mlx_whisper.transcribe(speech_file, word_timestamps=True)
        text = result["text"]
        segments = result['segments']

        output_list = []

        for segment in segments:
            startTime = str(0) + str(timedelta(seconds=int(segment['start']))) + ',000'
            endTime = str(0) + str(timedelta(seconds=int(segment['end']))) + ',000'
            text = segment['text']
            segmentId = segment['id'] + 1
            segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

            #srt_directory = os.path.join("transcription", "SrtFiles")
            #os.makedirs(srt_directory, exist_ok=True)
            #srtFilename = os.path.join(srt_directory, f"{audio_file}.srt")
            #with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            #    srtFile.write(segment)
            
            segment_dict = {
                "id": segmentId,
                "start_time": startTime,
                "end_time": endTime,
                "text": text[1:] if text[0] == ' ' else text
            }
            output_list.append(text)
            full_text = " ".join(output_list)
        #writefile(output_list)

        return full_text