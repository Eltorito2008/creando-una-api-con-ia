from typing import Generator
import os
from dotenv import load_dotenv
import psycopg

load_dotenv()
password = os.getenv("password")

url= f"postgresql://postgres.pwfanhwpbybcaoqtnuec:{password}@aws-0-us-west-2.pooler.supabase.com:6543/postgres"

def get_db_cursor() -> Generator[psycopg.Cursor, None, None]:
    conn = psycopg.connect(url, sslmode="require")
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()