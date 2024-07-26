import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import {{tmp}}

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

app.include_router({{tmp}}.router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, log_level="debug")
