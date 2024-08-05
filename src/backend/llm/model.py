import os
from groq import Groq
from dotenv import load_dotenv
from test_llm import test_text

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY2')

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
        {'role': 'system', 'content': sys_msg},
        {'role': 'user', 'content': text},
    ]

    try:
        response = Groq(api_key=GROQ_API_KEY).chat.completions.create(
            messages=message, model='llama-3.1-8b-instant'
        )
        
        if hasattr(response, 'choices') and len(response.choices) > 0:
            return response.choices[0].message.content

        return 'No summary available.'

    except Exception as e:
        print(f"Error during API request: {e}")
        return None

if __name__ == "__main__":
    with open('SnapScrib/transcription/SrtFiles/transcription.srt', 'r') as file:
        test = file.read()
    
    output = summarize(test)
    print(output)