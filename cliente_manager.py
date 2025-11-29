# cliente_manager.py - Versión corregida
from pydantic import BaseModel
import psycopg

class Cliente(BaseModel):
    nombre: str
    apellido: str

class ClienteManager:
    def agregar_cliente(self, cliente: Cliente, cursor: psycopg.Cursor):
        try:
            cursor.execute(
                "INSERT INTO cliente (nombre, apellido) VALUES (%s, %s)",
                (cliente.nombre, cliente.apellido)
            )
            return {"mensaje": f"Cliente '{cliente.nombre}' agregado"}
        except Exception as e:
            return {"error": f"Error al agregar cliente: {e}"}

    def eliminar_cliente(self, id_cliente: int, cursor: psycopg.Cursor):
        try:
            cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
            if cursor.rowcount == 0:
                return {"error": f"Cliente {id_cliente} no encontrado"}
            return {"mensaje": f"Cliente {id_cliente} eliminado"}
        except Exception as e:
            return {"error": f"Error al eliminar cliente: {e}"}

    def modificar_cliente(self, id_cliente: int, cliente: Cliente, cursor: psycopg.Cursor):
        try:
            cursor.execute(
                "UPDATE cliente SET nombre = %s, apellido = %s WHERE id_cliente = %s",
                (cliente.nombre, cliente.apellido, id_cliente)
            )
            if cursor.rowcount == 0:
                return {"error": f"Cliente {id_cliente} no encontrado"}
            return {"mensaje": f"Cliente {id_cliente} actualizado"}
        except Exception as e:
            return {"error": f"Error al modificar cliente: {e}"}

    def mostrar_clientes(self, cursor: psycopg.Cursor):
        try:
            cursor.execute("SELECT * FROM cliente")
            return [{"id_cliente": row[0], "nombre": row[1], "apellido": row[2]} for row in cursor.fetchall()]
        except Exception as e:
            return {"error": f"Error al obtener clientes: {e}"}