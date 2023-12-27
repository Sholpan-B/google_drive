from fastapi import FastAPI
from app.routes import files, auth

app = FastAPI()

app.include_router(files.router)
app.include_router(auth.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
