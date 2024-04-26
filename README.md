# GenAI Workshop
Welcome! Here are some instructions of how to get started!
First step is to get the backend and frontend running. 
You can do this using docker (recommended) or you can run each part natively on your system.

## Run backend and frontend with Docker 🐳 (Recommended)
When using docker, the frontend and backend will be started and connected automagically🪄
The backend is where you will be doing changes, and it supports hot reloading everytime you save.
Follow these steps: 
1. Open a terminal and navigate to the root of this repository
2. Run 
    ```
    docker-compose up --build
    ```
3. You should now be able to access the frontend at `http://localhost:4137` and the backend at `http://localhost:8000/docs`. 
Ensure the frontend can reach the backend, it should let you know 😉

## Run backend and frontend natively ‍💻👩‍💻
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

#### What is this config command?
As this project uses the Netlight design system, which is consumed via a private NPM registry, we need to set a valid token. To keep things simple, I (Jón) created a token for this workshop specifically, which will expire in mid April. If you want to run this locally and the token doesn't work, please check out [these instructions](https://nds-dev.edgez.live/?path=/docs/doc-installation-usage--docs).

## How to get started on the workshop?
1. Have a look at the backend code, more exactly Prompts.py
2. Experiment with the system and user messages to get it to convert the web content to a Recipe object.


## Recipe URLs to use
* https://www.allrecipes.com/recipe/11691/tomato-and-garlic-pasta/
* https://www.bonappetit.com/recipe/creamy-pasta-with-crispy-mushrooms

