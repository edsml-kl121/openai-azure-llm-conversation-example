from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("AZURE_ENDPOINT")
deployment_name = "gpt-4o-transcribe"
api_key = os.getenv("AZURE_API_KEY")

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-10-01-preview"
)
audio_file = open("testvoice.mp3", "rb")

transcription = client.audio.transcriptions.create(
    model=deployment_name,
    file=audio_file,
)

print(transcription.text)