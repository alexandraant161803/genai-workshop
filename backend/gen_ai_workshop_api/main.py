import uvicorn
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gen_ai_workshop_api.chatgpt import ask_chatgpt
from gen_ai_workshop_api.utils import fetch_and_transform_content
from gen_ai_workshop_api.prompts import SYSTEM_MESSAGE, USER_MESSAGE
from gen_ai_workshop_api.models import Recipe


app = FastAPI(title="GenAI PoC Workshop API", description="You got the API running, congratulations 💜")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173','http://localhost:4173'],
    allow_credentials=True,
    allow_methods=["*"],  # Or restrict to ['GET', 'POST', etc.]
    allow_headers=["*"],
)

@app.get("/recipe")
async def get_recipe(recipe_url: str) -> str | Recipe:
    """
    Creates a recipe from a recipe URL
    :param recipe_url: URL of the recipe
    :return: Recipe object with ingredients, instructions etc.
    """

    recipe_information = await fetch_and_transform_content(recipe_url)
    print("Successfully fetched recipe information")

    user_message = USER_MESSAGE.format(
            recipe_information=recipe_information
        )

    response = await ask_chatgpt(system_message=SYSTEM_MESSAGE, user_message=user_message)

    try:
        print(f"Here is the response from the chatbot: {response}")
        # Parse JSON string to a dictionary
        parsed_json = json.loads(response)
        # Convert dictionary to Pydantic model instance
        recipe = Recipe.model_validate(parsed_json)
        return recipe
    except:
        return response
    

@app.get("/healthz")
@app.get("/")
async def health_check():
    """
    Simply returns a 200 if the service is healthy
    """
    return {"ok": True}

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)


