# PROMPTS
This is [PROMPTS](https://promptsarch.sabaleuski.dev) project 🫠!

## Setup and run using Docker:
1. Create .env file of the frontend part.
    ```sh
    cd frontend && cp .env.example .env
    ```

2. Fill in the `.env` file with env variables.
The description of env variables for fronted can be found [here](https://github.com/desobolevsky/prompts/tree/main/frontend#env-variables-description).

    In case of the docker run the value for `VUE_APP_PROMPTS_API_BASE_URL` is going to be `http://backend`.

    ```
    VUE_APP_PROMPTS_API_BASE_URL=http://backend
    ```

3. Run docker-compose:
    ```sh
    docker-compose up
    ```

The app itself will be accessible at http://localhost:8080.  
The backend API will be accessible at http://localhost:8000.  
Also you can connect to Postgres at localhost:5432.  
