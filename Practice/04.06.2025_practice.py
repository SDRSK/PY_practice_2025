from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int | None = None


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/real")
async def root():
    return {"message": "something real"}



@app.get("/params")
async def root(
    name: str | None = None,      # http://localhost:8000/?name=Alice
    age: int | None = None        # http://localhost:8000/?name=Alice&age=30
):
    return {
        "greeting": f"Hello, {name or 'World'}",
        "age": {age or 22}
    }



@app.post("/user")
async def create_user(user: User):
    return {"received": user}


@app.get("/secure-data")
async def secure_data(api_key: str | None = Header(None, alias="api-key")):
    verify_api_key(api_key)
    return {"received_api_key": api_key}


def verify_api_key(x_api_key: str):
    if x_api_key != 'my-secret-key':
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")