from uuid import uuid4
from fastapi import APIRouter, HTTPException

from main import Categoria

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)

categorias = []

@router.get("/")
async def list_categorias():
    return {
        "msg": "",
        "data": categorias
    }

@router.post("/")
async def create_categoria(categoria: Categoria):
    categoria.id = str(uuid4())
    # TODO: Trabajar con base de datos
    categorias.routerend(categoria)
    return {
        "msg": "",
        "data": categoria
    }

@router.put("/")
async def update_categoria(categoria: Categoria):
    for cat in categorias:
        if cat.id == categoria.id:
            # Se encontró la categoria
            cat.nombre = categoria.nombre
            return cat
    raise HTTPException(
        status_code=404,
        detail="Categoria id no existente."
    )

@router.delete("/{categoria_id}")
async def delete_categoria(categoria_id : str):
    for i, cat in enumerate(categorias):
        if cat.id == categoria_id:
            categorias.pop(i)
            return {
                "msg": cat.nombre+" eliminado correctamente."
            }
    raise HTTPException(
        status_code=404,
        detail="Categoria id no encontrada."
    )

# Ejercicio 3
@router.get("/{categoria_id}")
async def get_categoria(categoria_id : str):
    for cat in categorias:
        if categoria_id == cat.id:
            return {
                "data": cat
            }
    raise HTTPException(
        status_code=404,
        detail="Categoria id no encontrado."
    )