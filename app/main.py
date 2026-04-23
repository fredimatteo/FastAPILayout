# This is the main entry point for the FastAPI application.
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FastAPI Template",
    description="FastAPI Template",
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello coder!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)