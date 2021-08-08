from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repository.product import RepositoryProduct
from src.schemas import schemas
from src.infra.sqlalchemy.repository.user import RepositoryUser
from src.infra.sqlalchemy.config import database

app = FastAPI()

# Depends injeção de dependência
@app.post('/products', status_code=status.HTTP_201_CREATED, response_model=schemas.ProductResponse)
def create_products(product: schemas.Product, database: Session = Depends(database.get_db)):
  created_product = RepositoryProduct(database).create(product)
  return created_product

@app.get('/products', status_code=status.HTTP_200_OK, response_model=List[schemas.Product])
def list_products(database: Session = Depends(database.get_db)):
  products = RepositoryProduct(database).index()
  return products

@app.post('/user', status_code=status.HTTP_200_OK)
def create_users(user: schemas.User, database: Session = Depends(database.get_db)):
  create_user = RepositoryUser(database).create(user)
  return create_user

@app.get('/users', status_code=status.HTTP_201_CREATED)
def list_users(database: Session = Depends(database.get_db)):
  users = RepositoryUser(database).index()
  return users