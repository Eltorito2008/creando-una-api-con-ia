from fastapi import APIRouter, Depends
import psycopg
from database.db_manager import get_db_cursor
from managers.pedido_manager import PedidoManager, Pedido

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])
pedido_manager = PedidoManager()

@router.get("/")
def obtener_pedidos(cursor: psycopg.Cursor = Depends(get_db_cursor)):
    return pedido_manager.mostrar_pedidos(cursor)

@router.post("/")
def agregar_pedido(pedido: Pedido, cursor: psycopg.Cursor = Depends(get_db_cursor)):
    return pedido_manager.insertar_pedido(pedido, cursor)

@router.delete("/{id_pedido}")
def eliminar_pedido(id_pedido: int, cursor: psycopg.Cursor = Depends(get_db_cursor)):
    return pedido_manager.eliminar_pedido(id_pedido, cursor)