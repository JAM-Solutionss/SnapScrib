import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER
from modules.summary.summarizer_factory import get_summarizer
import modules.summary.dummy_text as dummy_text
from modules.transcription.transcription_data import Transcription

def testing_get_summarizer():
    summarizer = get_summarizer()
    LOGGER.info(f"SUMMARIZER: {summarizer}")


def testing_dummy_text():
    extracted_text = [entry["text"] for entry in dummy_text.text]
    text = "\n".join(extracted_text)


def testing_summarizer():
    #extracted_text = [entry["text"] for entry in dummy_text.text]
    #text = "\n".join(extracted_text)

    test_transcription = Transcription(dummy_text)
    summary = get_summarizer().summarize(transcription=test_transcription)
    LOGGER.info(f"SUMMARY: {summary}")


if __name__ == "__main__":
    testing_summarizer()
