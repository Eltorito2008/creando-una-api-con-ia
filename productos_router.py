from fastapi import APIRouter, Depends
import psycopg
from database.db_manager import get_db_cursor
from managers.producto_manager import ProductoManager, Producto

router = APIRouter(prefix="/productos", tags=["Productos"])
producto_manager = ProductoManager()

@router.get("/")
def obtener_productos(cursor: psycopg.Cursor = Depends(get_db_cursor)):
    return producto_manager.mostrar_productos(cursor)

@router.post("/")
def agregar_producto(producto: Producto, cursor: psycopg.Cursor = Depends(get_db_cursor)):
    return producto_manager.agregar_producto(producto, cursor)

@router.put("/{id_producto}")
def modificar_producto(id_producto: int, producto: Producto, cursor: psycopg.Cursor = Depends(get_db_cursor)):
    return producto_manager.modificar_producto(id_producto, producto, cursor)

@router.delete("/{id_producto}")
def eliminar_producto(id_producto: int, cursor: psycopg.Cursor = Depends(get_db_cursor)):
    return producto_manager.eliminar_producto(id_producto, cursor)