# GenAI Workshop Setup Guide
Welcome to this GenAI Workshop! To get you up and running smoothly, we've prepared a step-by-step guide on how to set up your programming environment. If you're new to programming or the tools we'll be using, don't worry! Just follow the instructions below, and you'll be set up in no time.

## 1. Cloning the Workshop Repository

First, we need to get the workshop materials onto your computer by cloning our code repository.

### What you need:
- A terminal application, which allows you to type and execute text-based commands.
- Git installed (if you don't have it, download it [here](https://git-scm.com/downloads)).

### Steps:

1. **Open Your Terminal:**
   - **Windows**: Search for "Command Prompt" or "PowerShell" and open it.
   - **Mac**: Search for "Terminal" in Spotlight (Cmd + Space) and open it.
   - **Linux**: Search for "Terminal" or press "Ctrl + Alt + T" to open it.
2. **Create a New Folder and Navigate There:**
   - Decide on a location where you want to store your workshop materials. For example, you can create a new folder in your "Documents" directory.
   - Type `cd` followed by the path to your chosen location, then press Enter.
     - Example: `cd /Users/yourusername/Documents/codepub`
3. **Clone the Repository:**
   - In your terminal, paste the following command: 
     - `git clone https://github.com/alexandraant161803/genai-workshop.git`
   - After the cloning is complete, you will find a new folder called "genai-workshop" with all the code inside.

## 2. Installing Node.js

### Steps:

1. **Install Node.js:**
   - Go to the [Node.js website](https://nodejs.org/en/) and download the installer for your operating system.
   - Run the installer and follow the instructions to install Node.js on your computer.

## 3. Installing Docker
Docker is a tool that allows you to run applications in a lightly isolated environment called a container.

### Steps:

1. **Download and Install Docker:**
   - [Download Docker](https://www.docker.com/products/docker-desktop) for your operating system and install it on your computer.
   - Open the Docker Desktop application to make sure it's running in the background.

## 4. Running the Workshop Code with Docker 🐳

We'll use Docker to automatically set up and connect the front-end and back-end parts of our workshop project.

### Steps:

1. **Return to Your Terminal:**
   - It should still be open from the previous steps.
2. **Navigate to the Workshop Folder:**
   - Type `cd path-to-genai-workshop-folder` into your terminal, replacing "path-to-genai-workshop-folder" with the actual path where your workshop folder is located (e.g., `cd /Users/yourusername/Documents/codepub/genai-workshop`), and press Enter.
3. **Start the Project with Docker:**
   - Copy and paste `docker-compose up --build` into your terminal and press Enter.
   - Wait for the process to complete. This may take a few minutes.
4. **Access the Frontend:**
   - Open a web browser and go to `http://localhost:4137` to view the workshop's front-end interface.
   - Optionally, you can also check the back-end documentation at `http://localhost:8000/docs`.

**Congratulations!** You've successfully set up your environment for the GenAI Workshop. If you encounter any issues, don't hesitate to ask for help.

### Ready to Start!
- Your primary task is to write prompts that will be used to interact with the Azure OpenAI API. You can find templates for these located in: `backend/gen_ai_workshop_ai/prompts.py`. This is where you should make changes. 
- When you make changes and save the file, you should see the updates reflected on the front-end interface when you click "Get recipe".
- These prompts are crucial because they instruct the AI on what response you are expecting. You fortunately do not need to worry about the underlying logic of scraping websites or processing the information—that's all handled for you! Here's what you need to know about the context you have available:

### What is `recipe_information`?

When you provide a recipe URL to the `/recipe` API endpoint that we've created, the `fetch_and_transform_content` function goes to work. It retrieves data from the recipe website and transforms it into a structured format we refer to as `recipe_information`. This may include:

- A list of ingredients
- Preparation steps
- Cooking methods or techniques mentioned in the recipe
- Any other relevant data extracted from the recipe page

### How is `recipe_information` used?

The `recipe_information` is what you will use to create a personalized prompt that helps to guide the AI's response in a meaningful way. For instance, you might use that information to ask the AI to suggest alternatives to certain ingredients, provide additional cooking instructions, or even get creative with different recipe variations.

When constructing the `USER_MESSAGE`, the `recipe_information` is inserted into the prompt where the placeholder `{recipe_information}` is located. This formatted prompt is then sent to the Azure OpenAI API through the `ask_chatgpt` function.


### Recipe URLs for Testing:

- [Tomato and Garlic Pasta](https://www.allrecipes.com/recipe/11691/tomato-and-garlic-pasta/)
- [Creamy Pasta with Crispy Mushrooms](https://www.bonappetit.com/recipe/creamy-pasta-with-crispy-mushrooms)

Enjoy the workshop!
