from fastapi import FastAPI
from contextlib import asynccontextmanager
from quoteGenerator.db import init_db
from quoteGenerator.api import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield  # app runs after this point
    # Optionally add teardown/cleanup logic after `yield`

app = FastAPI(lifespan=lifespan)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Quote Generator API. Use /generate or /history"}

app.include_router(router)
