
import yt_dlp
from audio_data import Audio
from audio_extractor_interface import AudioExtractor
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER

class YoutubeExtractor(AudioExtractor):
    
    _default_format = 'bestvideo+bestaudio/best'
    _deflaut_postprocessors = [
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}
    ]
    _default_outtmpl = '%(title)s.%(ext)s'
    
    def __init__(self, format=None, postprocessors=None, outtmpl=None) -> None:
        super().__init__()
        self.format = format or self._default_format
        self.postprocessors = postprocessors or self._deflaut_postprocessors
        self.outtmpl = outtmpl or self._default_outtmpl

    def extract(self, audio_source: str) -> Audio:
        options = self._set_dl_opts()
        audio_file_path = self._get_audio_file_path(audio_source)
        self._donwload_audio(audio_source, options)
        audio = Audio(audio_file=audio_file_path, source=audio_source)
        return audio

    def _donwload_audio(self, url: str, options: dict) -> str:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
    
    def _set_dl_opts(self) -> dict:
        ydl_opts = {
            'format': self.format,
            'postprocessors': self.postprocessors,
            'outtmpl': os.path.join(self._default_audio_file_save_path,self.outtmpl)
        }
        return ydl_opts

    def _get_audio_file_path(self, url: str) -> str:
        with yt_dlp.YoutubeDL(self._set_dl_opts()) as ydl:
            info = ydl.extract_info(url, download=False)
            filename = ydl.prepare_filename(info)
            return os.path.splitext(filename)[0] + "." + self.postprocessors[0]['preferredcodec']
