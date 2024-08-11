from audio_extractor import AudioExtractor, DummyAudio
from typing import Type
import os


class FileExtractor(AudioExtractor):
      def extract(self, file_source: str) -> Type[DummyAudio]:
          """
          Extract audio from a file source.

          Args:
              file_source (str): The path to the audio file.

          Returns:
              str: A Audio instance representing the extracted audio.

          Raises:
              ValueError: If the provided file path is invalid.
          """

          if os.path.isfile(file_source):
              # file_source is a valid file path
              return DummyAudio(audio_file=file_source) # Instantiation needs to be adjusted later, when Adio dataclass is implemented
          else:
              # file_source is not a valid file path
              raise ValueError(f"Invalid file path: {file_source}")
