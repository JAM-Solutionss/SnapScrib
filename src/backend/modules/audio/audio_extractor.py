from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type

@dataclass
class DummyAudio():
    '''Dummy Adio dataclass for testing and implementing AudioExtractors. Will be replaced by Audio dataclass later on.'''
    audio_file: str


class AudioExtractor(ABC):
    '''Abstract interface class for AudioExtractor'''
    
    @abstractmethod
    def extract(self, audio_source: str) -> Type[DummyAudio]:
        '''This method needs to be implemmented by the child class'''
        pass