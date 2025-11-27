from fastapi import Depends, FastAPI
from models import Product
from database import Sessionlocal,engine
import  database_models
from sqlalchemy.orm import Session
app = FastAPI()

database_models.Base.metadata.create_all(bind=engine) #creating all the tables in the database 

@app.get("/")

def greet():
    print ("Welcome to Ecommerce Application")
    return {"message": "Welcome to Ecommerce Application"}

products =[
    Product(id=1, name="Laptop", description="A high performance laptop",price= 999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A high-end smartphone", price= 799.99, quantity=20),
    Product(id=3, name="Headphones", description="Noise-cancelling headphones", price= 199.99, quantity=30),
    Product(id=4, name="Mouse", description="A wireless mouse", price= 49.99, quantity=40),
    Product(id=5, name="Keyboard", description="A mechanical keyboard", price= 79.99, quantity=50)
   
]

def get_db():
    db= Sessionlocal()  
    try:
        yield db  
    finally:
        db.close() 

def init_db():
    db= Sessionlocal()  
    count = db.query(database_models.Product).count()

    if count ==0:  
        for product in products: 
            db.add(database_models.Product(**product.model_dump())) 
        db.commit()  
init_db()  

@app.get("/products") 
def  get_all_products(db: Session =  Depends(get_db)): 
   db_products = db.query(database_models.Product).all() 

   return db_products

@app.get("/product/{id}")
def get_product_by_id(id: int,db:Session= Depends(get_db)): 
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first() #
    if db_product: 
            return db_product
    return {"message": "Product not found"}     

@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)): #depends is used to get the database session
    db.add(database_models.Product(**product.model_dump()))  #model_dump() is used to convert the pydantic model to a dictionary
    db.commit()
    return product

@app.put("/product")
def update_product(id: int, product: Product, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()  #this will fetch the product with the given id and store it in db_product , filter is used to filter the records based on the condition
    if db_product:
        db_product.name= product.name #this will update the name of the product
        db_product.description= product.description
        db_product.price= product.price
        db_product.quantity= product.quantity
        db.commit()
        return "Product updated successfully"
    else:
        return {"message": "Product not found"}


@app.delete("/product/")
def delete_product(id: int, db: Session = Depends(get_db)):  
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()  #this will fetch the product with the given id and store it in db_product , filter is used to filter the records based on the condition
    if db_product:
        db.delete(db_product)  #this will delete the product from the database
        db.commit()
        return "Product deleted successfully"
    else:
        return {"message": "Product not found"} 
       
       