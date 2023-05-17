# Prompts Arch

Welcome to [Prompts Arch📚](https://promptsarch.sabaleuski.dev) project, an archive of prompt engineering! 🚀

Prompt Arch is designed to enhance the capabilities of ChatGPT by providing a collection of "best practiced" prompts with examples and descriptions. Built specifically for prompt engineering, Prompt Arch enables developers and users to craft highly effective and engaging interactions with ChatGPT.

With the exponential growth of natural language processing (NLP) applications, it has become crucial to guide language models effectively. Prompt Arch is here to address this need, serving as a repository of curated prompts that act as best practices for optimizing request and response generation. 

The goal of Prompts Arch is to leverage these prompts, so that people can unlock the true potential of ChatGPT, make conversations more precise, contextually aware, and satisfying.

Prompts arch can be found here: https://promptsarch.sabaleuski.dev 🚀

## Setup and run using Docker:
1. Create .env file of the frontend part.
    ```sh
    cd frontend && cp .env.example .env
    ```

2. Fill in the `.env` file with env variables.
The description of env variables for fronted can be found [here](https://github.com/desobolevsky/prompts/tree/main/frontend#env-variables-description).

    In case of the docker run the value for `VUE_APP_PROMPTS_API_BASE_URL` is going to be `http://localhost:8000`.

    ```
    VUE_APP_PROMPTS_API_BASE_URL=http://localhost:8000
    ```

3. Run docker-compose:
    ```sh
    docker-compose up
    ```

The app itself will be accessible at http://localhost:8080.  
The backend API will be accessible at http://localhost:8000.  
Also you can connect to Postgres at localhost:5432.  

## Contributing

If you're excited about prompt engineering and want to contribute to Prompt Arch, you're welcome with open arms! Here's how you can contribute to the project:

* **Share Your Prompts** 📦  
If you have a collection of prompts that have worked wonders, you're free to share them here! Use [this template](https://github.com/desobolevsky/prompts/blob/main/.github/ISSUE_TEMPLATE/prompt-proposal.md), add the prompts and examples, and submit the issue! That way you'll expand the prompt library and empower even more people to create exceptional conversations.
* **Enhance Descriptions** 📄  
You can improve existing prompt descriptions or create new ones that captivate and guide users effectively. Your words will be the guiding light for prompt engineers across the globe.
* **Сontribute Examples** 📚  
Examples are the fuel that ignites the creative fire in prompt engineering. If you have remarkable examples that showcase the true potential of prompts, please share them! Submit your examples through GitHub issues.
* **Contribute to the source code** 💻  
If you encounter a bug, or want to see some feature in Prompts Arch, or you just want to review the source code, you're very welcome to contribute in Prompts Arch source code. You're also welcome to fork the Prompt Arch repository, and modify it however you want.


## Tech
Prompts arch uses a number of open source tools to work properly.

Frontend is built with Vue.js🌄 and uses the following lib:
* 🌐 [axios](https://github.com/axios/axios)

Backend is built with Python🐍 and uses the following libs:
* ⚡ [FastAPI](https://github.com/tiangolo/fastapi)
* 🔍 [pydantic](https://github.com/pydantic/pydantic)
* 🧪 [alembic](https://github.com/sqlalchemy/alembic)
* 🗄️ [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy)
* 🦄 [uvicorn](https://github.com/encode/uvicorn)

## TODOs:
- [x] ~~**Prompt Proposal template**~~
- [ ] "Contribute" link in the app
- [ ] Prompts tags
- [ ] Prompts rating
- [ ] OpenAI integration with in-app requests to ChatGPT