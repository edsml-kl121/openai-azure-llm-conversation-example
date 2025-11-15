from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=api_key
)
audio_file = open("testvoice.mp3", "rb")

translation = client.audio.transcriptions.create(
    # model="whisper-1", 
    model="gpt-4o-transcribe", 
    file=audio_file,
)

print(translation.text)