from openai import AsyncAzureOpenAI
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

async def ask_chatgpt(system_message,user_message) -> str:
    client = AsyncAzureOpenAI(
        api_key=os.getenv('API_KEY'),
        api_version="2023-12-01-preview",
        azure_endpoint="https://oai-codepub.openai.azure.com/",
        azure_deployment= "gpt-4"
    )

    response = await client.chat.completions.create(
        temperature=0.5,
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": system_message,
            },
            {
                "role": "user",
                "content": user_message,
            },
        ],
    )

    return response.choices[0].message.content
