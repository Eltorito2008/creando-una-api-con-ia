# pedido_manager.py - Versión corregida
from pydantic import BaseModel
import psycopg

class Pedido(BaseModel):
    id_pedido: int
    id_producto: int
    id_cliente: int

class PedidoManager:
    def insertar_pedido(self, pedido: Pedido, cursor: psycopg.Cursor):
        try:
            cursor.execute(
                "INSERT INTO pedido (id_pedido, id_cliente, id_producto) VALUES (%s, %s, %s)",
                (pedido.id_pedido, pedido.id_cliente, pedido.id_producto)
            )
            return {"mensaje": "Pedido insertado correctamente"}
        except psycopg.IntegrityError as e:
            return {"error": f"Error de integridad: {e}"}
        except Exception as e:
            return {"error": f"Error al insertar pedido: {e}"}

    def eliminar_pedido(self, id_pedido: int, cursor: psycopg.Cursor):
        try:
            cursor.execute("DELETE FROM pedido WHERE id_pedido = %s", (id_pedido,))
            if cursor.rowcount == 0:
                return {"error": f"Pedido {id_pedido} no encontrado"}
            return {"mensaje": f"Pedido {id_pedido} eliminado"}
        except Exception as e:
            return {"error": f"Error al eliminar pedido: {e}"}

    def mostrar_pedidos(self, cursor: psycopg.Cursor):
        try:
            cursor.execute("""
                SELECT p.id_pedido, c.nombre, c.apellido, pr.nombre, pr.precio 
                FROM pedido p 
                INNER JOIN cliente c ON p.id_cliente = c.id_cliente 
                INNER JOIN productos pr ON p.id_producto = pr.id_producto
            """)
            return [{
                "id_pedido": row[0],
                "cliente_nombre": row[1],
                "cliente_apellido": row[2],
                "producto_nombre": row[3],
                "producto_precio": row[4]
            } for row in cursor.fetchall()]
        except Exception as e:
            return {"error": f"Error al obtener pedidos: {e}"}