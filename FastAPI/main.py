import database_models
from database import engine, session
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from sqlalchemy.orm import Session

from fastapi import Depends, FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=("http://localhost:3000"), allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)


@app.get("/")
def greet():
    return {"message": "Welcome to FastAPI and Uvicorn learning"}


products = [
    Product(id=1, name="Phone", description="Budget Phone", price=99, quantity=10),
    Product(id=2, name="Laptop", description="Gaming Laptop", price=999, quantity=6),
    Product(id=3, name="Tablet", description="Lenovo Tablet", price=150, quantity=10),
    Product(id=4, name="Speaker", description="Bass Booster", price=50, quantity=20),
]


def init_db():
    db = session()

    count = db.query(database_models.Product).count()

    print("Count: ", count)

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

        db.commit()


init_db()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):  # noqa: B008

    db_prodcuts = db.query(database_models.Product).all()
    return db_prodcuts


@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):

    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )
    if db_product:
        return db_product

    return "Product not found"


@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product


@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product updated successfully..."
    else:
        return "Product not found..."


@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted successfully.."
    else:
        return "Product not found..."
