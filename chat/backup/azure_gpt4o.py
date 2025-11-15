from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

print("AZURE FILE: ")
endpoint = f"{os.getenv('AZURE_ENDPOINT')}/openai/v1/"
deployment_name = "gpt-4o"
api_key = os.getenv("AZURE_API_KEY")

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
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