from app.deps import create_database_and_tables
from app.routes import user


from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn



@asynccontextmanager
async def lifespan(app: FastAPI):
    create_database_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(user.router)


@app.get("/health")
async def service_health():
    return {"status": "healhty"}


# def main():
#     create_database_and_tables()
#     uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)


# if __name__ == "__main__":
#     create_database_and_tables()
#     main()
