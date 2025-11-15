from pathlib import Path
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("AZURE_ENDPOINT")
deployment_name = "gpt-4o-mini-tts"
api_key = os.getenv("AZURE_API_KEY")

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2025-03-01-preview"
)
speech_file_path = Path(__file__).parent / "speech_azure.mp3"

with client.audio.speech.with_streaming_response.create(
    model=deployment_name,
    voice="coral",
    input="Today is a wonderful day to build something people love!",
    instructions="Speak in a cheerful and positive tone.",
) as response:
    response.stream_to_file(speech_file_path)