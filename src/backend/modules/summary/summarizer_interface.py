from abc import ABC, abstractmethod


class Summarizer(ABC):
    @abstractmethod
    def summarize(
        self, transcription: str, style: str = "neutral", length: float = 0.3
    ) -> str:
        """
        Summarizes the given transcription text into a shorter version, with the specified style and length.

        Args:
            transcription (str): The full transcription text to be summarized.
            style (str, optional): The desired style of the summary, defaults to "neutral".
            length (float, optional): The desired length of the summary as a fraction of the original transcription, defaults to 0.3.

        Returns:
            str: The summarized text.
        """
        pass
