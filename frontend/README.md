
# Prompts frontend
This is a frontend source code for *prompts* app.

## Setup
Install the dependencies:
```
npm install
```

Create .env file and [fill in .env file](#env-variables-description):
```
cp .env.example .env
```

Run the project:
```
npm run serve
```

## Or run it with Docker:
Create and [fill in .env file](#env-variables-description).
Build the image:
```
docker build . -t prompts-frontend:latest
```
Run:
```
docker run -tdi -p 8080:80 prompts-frontend:latest
```

The app will be accessible on http://localhost:8080 address.

## [Env variables description](#env-variables-description):
**VUE_APP_PROMPTS_API_BASE_URL** - the url of prompts backend instance.
