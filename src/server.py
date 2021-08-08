from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repository.product import RepositoryProduct
from src.infra.sqlalchemy.repository.user import RepositoryUser
from src.infra.sqlalchemy.config import database

database.create_db()

app = FastAPI()

# Depends injeção de dependência
@app.post('/product')
def create_products(product: schemas.Product, database: Session = Depends(database.get_db)):
  created_product = RepositoryProduct(database).create(product)
  return created_product

@app.get('/products')
def list_products(database: Session = Depends(database.get_db)):
  products = RepositoryProduct(database).index()
  return products

@app.post('/user')
def create_users(user: schemas.User, database: Session = Depends(database.get_db)):
  create_user = RepositoryUser(database).create(user)
  return create_user

@app.get('/users')
def list_users(database: Session = Depends(database.get_db)):
  users = RepositoryUser(database).index()
  return users