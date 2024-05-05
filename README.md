# GenAI Workshop Setup Guide
Welcome to this GenAI Workshop! To get you up and running smoothly, we've prepared a step-by-step guide on how to set up your programming environment. If you're new to programming or the tools we'll be using, don't worry! Just follow the instructions below, and you'll be set up in no time.

First step is getting this repository locally and getting the backend and frontend running. 
You can do this using docker (step 4) or you can run each part natively on your system (step 5).

## 1. Cloning the Workshop Repository
First, we need to get the workshop materials onto your computer by cloning our code repository.

### What you need:
- A terminal application, which allows you to type and execute text-based commands.
- Git installed (if you don't have it, download it [here](https://git-scm.com/downloads)).

### Steps:
 
1. **Open Your Terminal/Command Prompt:**
   - **Windows**: Search for "Command Prompt" or "PowerShell" and open it.
   - **Mac**: Search for "Terminal" in Spotlight (Cmd + Space) and open it.
   - **Linux**: Search for "Terminal" or press "Ctrl + Alt + T" to open it.
2. **Create a New Folder and Navigate There:**
   - Decide on a location where you want to store your workshop materials. For example, you can create a new folder in your "Documents" directory.
   - Type `cd` followed by the path to your chosen location, then press Enter.
     - Example: `cd /Users/yourusername/Documents/workshop`
3. **Clone the Repository:**
   - In your terminal, paste the following command: 
     - `git clone https://github.com/alexandraant161803/genai-workshop.git`
   - After the cloning is complete, you will find a new folder called "genai-workshop" with all the code inside.

## 2. Installing Node.js

### Steps:

1. **Install Node.js:**
   - Go to the [Node.js website](https://nodejs.org/en/) and download the installer for your operating system.
   - Run the installer and follow the instructions to install Node.js on your computer.

## 4. Running the Workshop Code with Docker 🐳 (recommended)

Docker is a tool that allows you to run applications in a lightly isolated environment called a container. We'll use Docker to automatically set up and connect the front-end and back-end parts of our workshop project.

### Steps:

1. **Download and Install Docker:**
   - [Download Docker](https://www.docker.com/products/docker-desktop) for your operating system and install it on your computer.
   - Open the Docker Desktop application to make sure it's running in the background.

2. **Return to Your Terminal:**
   - It should still be open from the previous steps.
3. **Navigate to the Workshop Folder:**
   - Type `cd path-to-genai-workshop-folder` into your terminal, replacing "path-to-genai-workshop-folder" with the actual path where your workshop folder is located (e.g., `cd /Users/yourusername/Documents/codepub/genai-workshop`), and press Enter.
4. **Start the Project with Docker:**
   - Copy and paste `docker-compose up --build` into your terminal and press Enter.
   - Wait for the process to complete. This may take a few minutes. It will look something like this:
    <img width="573" alt="image" src="https://github.com/alexandraant161803/genai-workshop/assets/140720562/80698b4d-5284-4b62-868f-884eb120cb33">

5. **Access the Frontend:**
   - Open a web browser and go to `http://localhost:4173` to view the workshop's front-end interface.
   - Optionally, you can also check the back-end documentation at `http://localhost:8000/docs`.

**Congratulations!** You've successfully set up your environment for the GenAI Workshop. If you encounter any issues, don't hesitate to ask for help.

## 5. Run backend and frontend natively ‍💻👩‍💻
### Backend API
To run natively you need python3 installed on your system.

Follow these steps to start the application:

1. Navigate to the the backend directory in your terminal: 
    ```
    cd genai-workshop/backend/
    ```
2. Create a virtual python environment:
    * MacOS 🍎: 
    ```
    python3 -m venv gen_ai_workshop_env
    ```
    * Windows 🪟: 
    ```
    python -m venv gen_ai_workshop_env
    ```
3. Activate the virtual environment:
    * MacOS 🍎: 
    ```
    source gen_ai_workshop_env/bin/activate
    ```
    * Windows 🪟: 
    ```
    .\gen_ai_workshop_env\Scripts\activate
    ```
4. Install dependencies:
    * Run 
    ```
    pip install -r requirements.txt
    ```
    * And
    ```
    playwright install && playwright install-deps
    ```
5. Run the application:
    * Run 
    ```
    uvicorn gen_ai_workshop_api.main:app --host 0.0.0.0 --port 8000
    ```
    * Note you can add flag `--reload` to enable hot reloading, this might NOT work on Windows. You should now be able to access the API and its documentation at `http://localhost:8000/docs`

### Frontend 
You need to have [NodeJS](https://nodejs.org/en) installed locally.

From the root of the frontend run the following commands
```
npm config set -- '//gitlab.netlight.com/api/v4/projects/1217/packages/npm/:_authToken' "glpat-dBh68ynPbn-bRjziPAVP"
```

```
npm i
```
to install the projects dependencies. Once those have installed, run

```
npm run dev
```

Now the project should be running on `localhost:5173`.


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
