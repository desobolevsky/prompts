import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.v1.api import api_router

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
