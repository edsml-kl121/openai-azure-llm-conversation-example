from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

print("OPENAI FILE: ")
deployment_name = "gpt-4o"
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
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