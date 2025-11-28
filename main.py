from fastapi import Depends, FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from jose import jwt
import os

import database_models
from database import Sessionlocal, engine
from models import Product
from auth_models import User as UserModel
from auth_schemas import UserCreate, UserOut, UserLogin
from utils_auth import hash_password, verify_password, create_access_token, SECRET_KEY

load_dotenv()

app = FastAPI()

# ------------------------
# CORS (MUST BE AT TOP)
# ------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------
# DB Session
# ------------------------
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------
# Product List (define BEFORE init_db)
# ------------------------
products = [
    Product(id=1, name="Laptop", description="A high performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A high-end smartphone", price=799.99, quantity=20),
    Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=30),
    Product(id=4, name="Mouse", description="A wireless mouse", price=49.99, quantity=40),
    Product(id=5, name="Keyboard", description="A mechanical keyboard", price=79.99, quantity=50)
]

# ------------------------
# Create tables
# ------------------------
database_models.Base.metadata.create_all(bind=engine)

# ------------------------
# Initialize DB with default products
# ------------------------
def init_db():
    db = Sessionlocal()
    if db.query(database_models.Product).count() == 0:
        for p in products:
            db.add(database_models.Product(**p.model_dump()))
        db.commit()
init_db()

# ------------------------
# Routes
# ------------------------

@app.get("/")
def greet():
    return {"message": "Welcome to Ecommerce Application"}

# REGISTER
@app.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(UserModel).filter(UserModel.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")

    if db.query(UserModel).filter(UserModel.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = UserModel(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# LOGIN
@app.post("/token")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    token = create_access_token({"sub": db_user.username})

    return {"access_token": token, "token_type": "bearer"}

# PROTECTED
@app.get("/protected")
def protected_route(Authorization: str = Header(None)):
    if Authorization is None:
        raise HTTPException(status_code=401, detail="Missing token")

    token = Authorization.split(" ")[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"message": "You are logged in", "user": payload["sub"]}
    except:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

# PRODUCTS CRUD
@app.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()

@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if product:
        return product
    return {"message": "Product not found"}

@app.post("/products/")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return {"message": "Updated successfully"}
    return {"message": "Product not found"}

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Deleted successfully"}
    return {"message": "Product not found"}
