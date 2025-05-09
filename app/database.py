import psycopg2
import redis
import os
import time

# PostgreSQL connection with retry
def get_db_connection(retries=5, delay=5):
    for attempt in range(retries):
        try:
            conn = psycopg2.connect(
                host=os.getenv("POSTGRES_HOST", "db"),
                database=os.getenv("POSTGRES_DB", "productsdb"),
                user=os.getenv("POSTGRES_USER", "user"),
                password=os.getenv("POSTGRES_PASSWORD", "password")
            )
            print("✅ Connected to PostgreSQL.")
            return conn
        except psycopg2.OperationalError as e:
            print(f"❌ Attempt {attempt + 1}: Failed to connect to DB: {e}")
            time.sleep(delay)
    raise Exception("❌ Could not connect to the database after several attempts.")

# Redis connection
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

# Create table if not exists (run once at startup)
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
