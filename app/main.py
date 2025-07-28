import uvicorn

# from deps import create_database_and_tables

from fastapi import FastAPI
from app.routes import user


app = FastAPI()
app.include_router(user.router)


@app.get("/health")
async def service_health():
    return {"status": "healhty"}


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)


if __name__ == "__main__":
    # create_database_and_tables()
    main()
