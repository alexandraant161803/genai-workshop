from openai import AsyncAzureOpenAI

async def ask_chatgpt(system_message,user_message) -> str:
    client = AsyncAzureOpenAI(
        api_key="b54994dc983a426eb0447d065fb84f1a",
        api_version="2023-12-01-preview",
        azure_endpoint="https://oai-codepub.openai.azure.com/",
        azure_deployment= "gpt-35-turbo"
    )

    response = await client.chat.completions.create(
        temperature=0.5, #TODO: play around with this parameter. Can be a number between 0.0-1.0. 
        model="gpt-3.5-turbo",
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
