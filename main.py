from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI()

origins = {
    "*"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class LoginRequest(BaseModel):
    username: str = Field(...,min_length=5)
    password: str = Field(...,min_length=8)

class Categoria(BaseModel):
    id: str | None = None
    nombre: str

class Videojuego(BaseModel):
    id: str | None = None
    nombre: str
    descripcion: str
    url_imagen: str
    categoria: Categoria

@app.post("/login")
async def login(login_request : LoginRequest):
    if (login_request.username == "PROGRAWEB" and login_request.password == "123123123"):
        return {
            "msg": "Acceso concedido"
        }
    else:
        raise HTTPException(
            status_code=400,
            detail="Error en login, credenciales incorrectas")

videojuegos = []

@app.get("/videojuegos")
async def list_videojuegos():
    return {
        "msg": "",
        "data": videojuegos
    }
