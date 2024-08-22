
from audio_data import Audio
from audio_extractor_interface import AudioExtractor


class YoutubeExtractor(AudioExtractor):

    def extract(self, url: str) -> Audio:
        pass
