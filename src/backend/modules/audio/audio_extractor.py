from abc import ABC, abstractmethod

class AudioExtractor(ABC):
    '''Abstract interface class for AudioExtractor'''
    @abstractmethod
    def extract(self, audio_source: str) -> str:
        '''This method needs to be implemmented by the child class'''
        pass