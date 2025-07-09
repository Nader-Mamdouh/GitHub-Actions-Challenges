from fastapi import FastAPI

app = FastAPI(title="Simple FastAPI Project", description="A demo FastAPI application", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
