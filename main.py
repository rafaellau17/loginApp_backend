from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(login_request : LoginRequest):
    if (login_request.username == "PW" and login_request.password == "123"):
        return {
            "msg": "Acceso concedido"
        }
    else:
        raise HTTPException(
            status_code=400,
            detail="Error en login, credenciales incorrectas")
    