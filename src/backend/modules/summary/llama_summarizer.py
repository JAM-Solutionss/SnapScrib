import os
from groq import Groq
from dotenv import load_dotenv
from summarizer_blueprint import Summarizer

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


class Llama_Summarizer(Summarizer):
    def summarize(text):
        sys_msg = (
            "You are an AI that gets a scripted video. You should then summarize this "
            "and lift the most important points. Keep the order when summarizing. "
            "Do not add anything and do not deviate. Please write this in sentences and without *. "
            "Leave out the speech and just summarize the information. "
            "The summary should be about a quarter to a third of the length of the original text. "
            "do not indicate that this is the summary."
        )

        message = [
            {"role": "system", "content": sys_msg},
            {"role": "user", "content": text},
        ]

        try:
            response = Groq(api_key=GROQ_API_KEY).chat.completions.create(
                messages=message, model="llama-3.1-70b-versatile"
            )

            if hasattr(response, "choices") and len(response.choices) > 0:
                return response.choices[0].message.content

            return "No summary available."

        except Exception as e:
            print(f"Error during API request: {e}")
            return None
