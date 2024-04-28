"""
Your task is to write effective prompts that will be used to communicate with Azure's OpenAI API.
An effective prompt should be clear, concise, and provide enough context to the AI for generating a relevant response.

Below you will find template strings for SYSTEM_MESSAGE and USER_MESSAGE.
These templates serve as containers for the text that will be sent to the API.

You will only need to modify the content within the triple quotes (''' ''') of these variables.

Tips for writing good prompts:
1. Be specific about what you want the AI model to do.
2. Provide clear instructions or questions.
3. Include relevant context or information that will help the AI understand the task.
4. Keep the language simple and direct.
5. Test different versions to see which prompts give you better results.
"""

# TODO: Write a prompt for the system message. 
# This is what the AI will see as the setup for the interaction.
# Example: "You are a helpful assistant who can provide detailed recipe information."
# Tip: Explain the exact format you would like the output in (have a look at the Recipe class in models.py). It can be helpful to provide an example of an expected output.
SYSTEM_MESSAGE: str = """    
# Your system prompt here
"""

# TODO: Write a prompt for the user message. 
# This should include any information the API needs to generate a response to a user's request.
# The {recipe_information} placeholder will be replaced with actual content from the scraped recipe when the code runs.
USER_MESSAGE: str = """   
# Your user prompt here
Information: {recipe_information}
"""

# Remember to check the output and tweak your prompts as needed. This iterative process will help you create prompts that effectively communicate with the API and generate the best possible responses.