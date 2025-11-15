from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

print("AZURE FILE: ")
endpoint = os.getenv("AZURE_ENDPOINT")
deployment_name = "gpt-4o"
api_key = os.getenv("AZURE_API_KEY")

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-10-01-preview"
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "List top 10 programming languages in 2024",
        }
    ],
)

print(completion.choices[0].message)