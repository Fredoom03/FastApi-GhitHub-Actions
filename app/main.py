from app.deps import create_database_and_tables
from app.routes import user

from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_database_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(user.router)


@app.get("/health")
async def service_health():
    return {"status": "healhty"}
