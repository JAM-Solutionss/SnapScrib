import os
import sys
from groq import Groq
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER
from modules.summarizer.summarizer_interface import Summarizer

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


class Llama_Summarizer(Summarizer):

    default_style = "professional"
    available_styles = ["professional", "friendly", "funny"]

    def summarize(self, summary: str, style: str):
        """
        Summarizes the given text using the Llama language model.

        Args:
            summary (str): The text to be summarized.
            style (str): The style of the system message, can be "professional", "friendly", or "funny".

        Returns:
            str: The summarized text, or "No summary available." if an error occurs.
        """
        sys_msg = self._get_sys_msg(style)
        LOGGER.info("Using style: " + style)

        message = [
            {"role": "system", "content": sys_msg},
            {"role": "user", "content": summary},
        ]

        try:
            response = Groq(api_key=GROQ_API_KEY).chat.completions.create(
                messages=message, model="llama-3.1-70b-versatile"
            )

            if hasattr(response, "choices") and len(response.choices) > 0:
                LOGGER.info("Summary successful")
                return response.choices[0].message.content

            LOGGER.debug("No summary available.")
            return None

        except Exception as e:
            LOGGER.debug(f"Error during API request: {e}")
            return None

    def _get_sys_msg(self, style):
        """
        Retrieves the system message for the Llama summarizer based on the specified style.

        Args:
            style (str): The style of the system message, can be "professional", "friendly", or "funny".

        Returns:
            str: The system message for the specified style.
        """
        styles = {
            "professional": "You are an AI that gets a scripted video. You should then summarize this and "
            "lift the most important points. Keep the order when summarizing. Do not add "
            "anything and do not deviate. Please write this in sentences and without *. "
            "Leave out the speech and just summarize the information. The summary should "
            "be about a quarter to a third of the length of the original text. do not indicate "
            "that this is the summary.",
            "friendly": "You are an AI that gets a scripted video. You should then summarize this and lift "
            "the most important points. Keep the order when summarizing. Do not add anything and "
            "do not deviate. Please write this in sentences and without *. Leave out the speech "
            "and just summarize the information. The summary should be about a quarter to a third "
            "of the length of the original text. do not indicate that this is the summary.",
            "funny": "You are an AI that gets a scripted video. You should then summarize this and lift the "
            "most important points. Keep the order when summarizing. Do not add anything and do not "
            "deviate. Please write this in sentences and without *. Leave out the speech and just "
            "summarize the information. The summary should be about a quarter to a third of the "
            "length of the original text. do not indicate that this is the summary.",
        }

        if style in styles:
            return styles[style]
        else:
            return self.default_style
