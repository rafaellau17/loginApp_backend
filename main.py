from uuid import uuid4
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
    id: int
    nombre: str

class Videojuego(BaseModel):
    id: int
    nombre: str
    descripcion: str
    url_imagen: str
    categoria: Categoria

categorias = []

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
    
@app.post("/categoria")
async def create_categoria(categoria: Categoria):
    categoria.id = str(uuid4())
    # TODO: Trabajar con base de datos
    categorias.append(categoria)
    return categoria
   
@app.get("/categorias")
async def list_categorias():
    return categorias