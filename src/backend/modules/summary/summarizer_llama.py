import os
import sys
from groq import Groq
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.logger_config import LOGGER
from modules.summary.summarizer_interface import Summarizer
from modules.summary.summary_data import Summary
from modules.transcription.transcription_data import Transcription

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


class LlamaSummarizer(Summarizer):

    default_style = "neutral"
    available_styles = ["professional", "friendly", "funny", "neutral"]

    def summarize(
        self, transcription: Transcription, style: str = None, length: float = 0.5
    ) -> Summary:
        """
        Summarizes the given transcription text using the Llama language model.

        Args:
            transcription (str): The text to be summarized.
            style (str, optional): The style of the system message, can be "professional", "friendly", "funny", or "neutral". Defaults to "neutral".
            length (float, optional): The target length of the summary as a fraction of the original text length. Defaults to 0.5.

        Returns:
            str or None: The summarized text, or None if an error occurs during the API request.
        """

        sys_msg = self._get_sys_msg(style, length)
        LOGGER.info("Using style: " + str(style))

        message = [
            {"role": "system", "content": sys_msg},
            {"role": "user", "content": transcription.text_output},
        ]

        try:
            response = Groq(api_key=GROQ_API_KEY).chat.completions.create(
                messages=message, model="llama-3.1-70b-versatile"
            )

            if hasattr(response, "choices") and len(response.choices) > 0:
                LOGGER.info("Summary successful")
                LOGGER.info(f"Summary: {response.choices[0].message.content}")
                LOGGER.info(f"Original text: {len(transcription)}")
                LOGGER.info(
                    f"Words: {len(str(response.choices[0].message.content).split())}"
                )
                return response.choices[0].message.content

            LOGGER.debug("No summary available.")
            return None

        except Exception as e:
            LOGGER.debug(f"Error during API request: {e}")
            return None

    def _get_sys_msg(self, style: str, length: float) -> str:
        """
        Helper function to generate the system message for the Llama language model based on the specified style and target summary length.

        Args:
            style (str): The style of the system message, can be "professional", "friendly", "funny", or "neutral".
            length (float): The target length of the summary as a fraction of the original text length.

        Returns:
            str: The generated system message.
        """
        styles = {
            "professional": "You are an AI that gets a scripted video. You should then summarize this and "
            "lift the most important points. Keep the order when summarizing. Do not add "
            "anything and do not deviate. Please write this in sentences and without *. "
            "Leave out the speech and just summarize the information. The summary should "
            f"be about {length*100}% of the length of the original text, not shorter or longer. do not indicate "
            "that this is the summary.",
            "friendly": "You are an AI that gets a scripted video. You should then summarize this and lift "
            "the most important points. Keep the order when summarizing. Do not add anything and "
            "do not deviate. Please write this in sentences and without *. Leave out the speech "
            f"and just summarize the information. The summary should be about {length*100}% "
            "of the length of the original text, not shorter or longer. do not indicate that this is the summary.",
            "funny": "You are an AI that gets a scripted video. You should then summarize this and lift the "
            "most important points. Keep the order when summarizing. Do not add anything and do not "
            "deviate. Please write this in sentences and without *. Leave out the speech and just "
            f"summarize the information. The summary should be about {length*100}% of the "
            "length of the original text, not shorter or longer. do not indicate that this is the summary.",
            "neutral": "You are an AI that gets a scripted video. You should then summarize this and lift the "
            "most important points. Keep the order when summarizing. Do not add anything and do not "
            "deviate. Please write this in sentences and without *. Leave out the speech and just "
            f"summarize the information. The summary should be about {length*100}% of the "
            "length of the original text, not shorter or longer. do not indicate that this is the summary.",
        }

        if style in styles:
            LOGGER.info("SYS PROMPT: " + styles[style])
            return styles[style]
        else:
            LOGGER.info("SYS PROMPT: " + styles[self.default_style])
            return styles[self.default_style]
