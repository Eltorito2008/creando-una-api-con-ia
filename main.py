# main.py - Versión corregida
from fastapi import FastAPI, Depends
import os
import psycopg
from typing import Generator

# Importar routers
from routers.clientes_router import router as clientes_router
from routers.productos_router import router as productos_router
from routers.pedidos_router import router as pedidos_router

app = FastAPI(title="Carrito de Compra API")

# Incluir routers
app.include_router(clientes_router)
app.include_router(productos_router)
app.include_router(pedidos_router)

# Función de conexión simplificada
def get_db():
    password = os.getenv("password")
    if not password:
        raise ValueError("No password found in environment variables")
    
url= f"postgresql://postgres.pwfanhwpbybcaoqtnuec:{password}@aws-0-us-west-2.pooler.supabase.com:6543/postgres"

    
conn = psycopg.connect(url, sslmode="require")
return conn

@app.get("/")
def root():
    return {"message": "API Carrito de Compra funcionando"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/test-db")
def test_db():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 as test")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return {"database": "connected", "result": result[0]}
    except Exception as e:
        return {"database": "error", "error": str(e)}