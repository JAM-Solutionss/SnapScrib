import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

class Summarizer():
    def summarize(transcription):
        sys_msg = (
            "You are an AI tasked with summarizing a scripted video. Your goal is to extract and highlight "
            "the most critical points while maintaining the original order of information. The summary "
            "should be about one quarter to one third of the length of the original text. "
            "Write in complete sentences, omit any dialogue, and focus only on the informational content. "
            "Do not add any commentary, and do not indicate that the text is a summary."
        )

        message = [
            {'role': 'system', 'content': sys_msg},
            {'role': 'user', 'content': transcription},
        ]

        try:
            response = Groq(api_key=GROQ_API_KEY).chat.completions.create(
                messages=message, model='llama-3.1-70b-versatile'
            )
            
            if hasattr(response, 'choices') and len(response.choices) > 0:
                return response.choices[0].message.content

            return 'No summary available.'

        except Exception as e:
            print(f"Error during API request: {e}")
            return None