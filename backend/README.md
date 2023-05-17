# Prompts backend
This is a frontend source code for *prompts* app.

## Setup and run
1. Install the dependencies:
   ```sh
   poetry install
   ```
2. Create .env file and [fill in .env file](#env-variables-description):
   ```sh
   cp .env.example .env
   ```
   
    Or use the env variables when running the app in any other way, environmental variables from environment have 
the priority over the ones in .env file.
3.  Run migrations
   ```sh
   poetry run alembic upgrade head
   ```
4. *(Optional)* Initialize DB with some dummy data:
   ```sh
   poetry run python init_db.py
   ```
5. Run the app:
   ```sh
   poetry run uvicorn main:app --host 0.0.0.0 --port 8000
   ```
   The app will be accessible at http://localhost:8000.

## Or run using Docker:
Build:
```sh
docker build -t prompts-backend:latest .
```
Run:
```sh
docker run -tdi \
 -e POSTGRES_SERVER='localhost:5432' \
 -e POSTGRES_DB='prompts'
 -e POSTGRES_USER='postgres'
 -e POSTGRES_PASSWORD='1234' 
 -p 8000:8000
 prompts-backend:latest
```
Or fill in .env file and run without env variables in shell:
```sh
docker run -tdi -p 8000:8000 prompts-backend:latest
```
The app will be accessible at http://localhost:8000.

## ## [Env variables description](#env-variables-description):
**POSTGRES_SERVER** - address of the postgres server  
**POSTGRES_DB** - db name in postgres server  
**POSTGRES_USER** - postgres username  
**POSTGRES_PASSWORD** - postgres password  