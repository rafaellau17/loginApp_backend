from uuid import uuid4
from fastapi import APIRouter

from main import Videojuego

router = APIRouter(
    prefix="/videojuegos",
    tags=["Videojuegos"]
)

videojuegos = []

@router.get("/")
async def list_videojuegos():
    return {
        "msg": "",
        "data": videojuegos
    }
