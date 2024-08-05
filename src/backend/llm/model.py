import os
from groq import Groq
from dotenv import load_dotenv
from test_llm import test_text

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

def gpt(script):
    sys_msg = (
        "You are an AI that gets a scripted video. You should then summarize this "
        "and lift the most important points. Keep the order when summarizing. "
        "Do not add anything and do not deviate. Please write this in sentences and without *. "
        "Leave out the speech and just summarize the information. "
        "The summary should be about a quarter to a third of the length of the original text. "
        "do not indicate that this is the summary."
    )

    message = [
        {'role': 'system', 'content': sys_msg},
        {'role': 'user', 'content': script},
    ]

    try:
        response = Groq(api_key=GROQ_API_KEY).chat.completions.create(
            messages=message, model='llama3-70b-8192'
        )
        
        if hasattr(response, 'choices') and len(response.choices) > 0:
            return response.choices[0].message.content

        return 'No summary available.'

    except Exception as e:
        print(f"Error during API request: {e}")
        return None

if __name__ == "__main__":
    output = gpt(test_text)
    print(output)