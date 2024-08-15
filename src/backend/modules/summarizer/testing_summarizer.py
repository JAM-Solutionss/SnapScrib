from summarizer_factory import get_summarizer
from dummy_text import text
import os
import sys


sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)
from utils.logger_config import LOGGER


if __name__ == "__main__":
    summary = get_summarizer().summarize(text)
    LOGGER.info(f"SUMMARY: {summary}")
