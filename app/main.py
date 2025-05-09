from fastapi import FastAPI, HTTPException
from app.models import Product
from app.database import get_db_connection, init_db, redis_client

app = FastAPI()

# Init DB on startup
@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def read_root():
    return {"message": "Hello in Simple FastAPI App"}

@app.get("/products")
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, description FROM products;")
    products = [{"name": row[0], "description": row[1]} for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return products

@app.post("/products")
def create_product(product: Product):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, description) VALUES (%s, %s);", (product.name, product.description))
    conn.commit()
    cursor.close()
    conn.close()

    # Store latest product name in Redis
    redis_client.set("latest_product", product.name)

    return {"message": "Product added successfully"}