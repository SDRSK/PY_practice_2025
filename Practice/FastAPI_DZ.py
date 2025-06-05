"""
Ознайомитися із бібліотекою requests та FastAPI. 
Написати простий HTTP сервер за допомогою FastAPI, 
який завжди поверне відповідь {‘status’: ‘ok’}, отримати цю відповідь за допомогою бібліотеки requests (окрема програма)
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(content={"status": "ok"})
