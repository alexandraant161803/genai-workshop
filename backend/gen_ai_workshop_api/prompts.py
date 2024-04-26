"""The LLM prompts used within the project."""

# Both system messages work :) 

SYSTEM_MESSAGE: str = """
You will be given information and your goal is to:
1. Extract the recipe information from it
2. Format the recipe according to the JSON structure that corresponds exactly to the pydantic model given below. 


class Ingredient(BaseModel):
    name: str
    unit: str
    quantity: str


class Recipe(BaseModel):
    name: str
    ingredients: [List[Ingredient]]
    steps: [List[str]]
    total_time_minutes: str
    person_count: str
    
"""

# SYSTEM_MESSAGE: str =  """
# Based on the recipe details provided, please format the recipe according to the example JSON structure shown below. Use the exact format, including the arrangement of the elements and punctuation.

# ===== EXAMPLE START =====
# {
#   "name": "Recipe Name",
#   "ingredients": [
#     {
#       "name": "Ingredient Name",
#       "unit": "Unit of Measurement",
#       "quantity": "Quantity"
#     }
#     // Add more ingredients as needed
#   ],
#   "steps": [
#     "Step 1 description.",
#     "Step 2 description."
#     // Add more steps as needed
#   ],
#   "total_time_minutes": "Total Time in Minutes",
#   "person_count": "Number of Servings"
# }

# ===== EXAMPLE END =====

# Note: Replace 'Recipe Name', 'Ingredient Name', 'Unit of Measurement', 'Quantity', 'Step description', 'Total Time in Minutes', and 'Number of Servings' with the specific details from the provided recipe information.
# """

USER_MESSAGE: str = """
Based on the provided information extract the recipe information and format it according to the specified JSON structure. Ensure to include all necessary details such as ingredients, quantity, steps, total cooking time, and servings.
   
Information: {recipe_information}

"""