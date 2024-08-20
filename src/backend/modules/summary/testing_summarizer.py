from summarizer_factory import get_summarizer
from dummy_text import text
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER

if __name__ == "__main__":
    extracted_text = [entry["text"] for entry in text]
    text = "\n".join(extracted_text)
    summary = get_summarizer().summarize(transcription=text)
    LOGGER.info(f"SUMMARY: {summary}")
