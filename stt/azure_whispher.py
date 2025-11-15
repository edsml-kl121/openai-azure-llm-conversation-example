from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("AZURE_ENDPOINT")
deployment_name = "whisper"
api_key = os.getenv("AZURE_API_KEY")

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-06-01"
)
audio_file = open("testvoice.mp3", "rb")

translation = client.audio.translations.create(
    model=deployment_name,
    file=audio_file,
)

print(translation.text)