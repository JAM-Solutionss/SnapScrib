import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq()
filename = os.path.dirname(__file__) + "/audio.ogg"

with open(filename, "rb") as file:
     transcription = client.audio.transcriptions.create(
       file=(filename, file.read()),
       model="whisper-large-v3",
       prompt="Specify context or spelling",  # Optional
       response_format="json",  # Optional
       language="en",  # Optional
       temperature=0.0  # Optional
     )
     print(transcription)