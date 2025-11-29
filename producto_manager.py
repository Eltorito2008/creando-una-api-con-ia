# producto_manager.py - Versión corregida
from pydantic import BaseModel
import psycopg

class Producto(BaseModel):
    nombre: str  # Cambiado de 'nomPRODUCTOS' a 'nombre'
    precio: float

class ProductoManager:
    def agregar_producto(self, producto: Producto, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO productos (nombre, precio) VALUES (%s, %s)",
            (producto.nombre, producto.precio)  # Usar 'nombre' en lugar de 'nomPRODUCTOS'
        )
        return {"mensaje": f"Producto '{producto.nombre}' agregado"}

    def eliminar_producto(self, id_producto: int, cursor: psycopg.Cursor):
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
        return {"mensaje": f"Producto {id_producto} eliminado"}

    def modificar_producto(self, id_producto: int, producto: Producto, cursor: psycopg.Cursor):
        cursor.execute(
            "UPDATE productos SET nombre = %s, precio = %s WHERE id_producto = %s",
            (producto.nombre, producto.precio, id_producto)  # Usar 'nombre' en lugar de 'nomPRODUCTOS'
        )
        return {"mensaje": f"Producto {id_producto} actualizado"}

    def mostrar_productos(self, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM productos")
        return [{"id_producto": row[0], "nombre": row[1], "precio": row[2]} for row in cursor.fetchall()]