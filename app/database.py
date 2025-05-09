import psycopg2
import redis
import os
from psycopg2 import OperationalError

def get_db_connection():
    try:
        return psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "db"),
            database=os.getenv("POSTGRES_DB", "productsdb"),
            user=os.getenv("POSTGRES_USER", "user"),
            password=os.getenv("POSTGRES_PASSWORD", "password")
        )
    except OperationalError as e:
        print(f"Unable to connect to the database: {e}")
        raise

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
