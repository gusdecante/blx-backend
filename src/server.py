from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repository.repository_product import RepositoryProduct
from src.schemas import schemas
from src.infra.sqlalchemy.repository.repository_user import RepositoryUser
from src.infra.sqlalchemy.config import database

app = FastAPI()

# CORS
origins = [
  "http://localhost:3000"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins= origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# Depends injeção de dependência
@app.post('/products', status_code=status.HTTP_201_CREATED, response_model=schemas.ProductResponse)
def create_products(product: schemas.Product, database: Session = Depends(database.get_db)):
  created_product = RepositoryProduct(database).create(product)
  return created_product

@app.get('/products', status_code=status.HTTP_200_OK, response_model=List[schemas.Product])
def list_products(database: Session = Depends(database.get_db)):
  products = RepositoryProduct(database).index()
  return products

@app.put('/products/{id}', response_model=schemas.ProductResponse)
def update_products(id: int, product: schemas.Product, database: Session = Depends(database.get_db)):
  RepositoryProduct(database).update(id, product)
  product.id = id
  return product

@app.delete('/products/{id}')
def delete_products(id: int, database: Session = Depends(database.get_db)):
  RepositoryProduct(database).delete(id)
  return id

@app.post('/signup', status_code=status.HTTP_201_CREATED)
def signup(user: schemas.User, database: Session = Depends(database.get_db)):
  create_user = RepositoryUser(database).create(user)
  return create_user

@app.get('/users', status_code=status.HTTP_200_OK, response_model=List[schemas.User])
def list_users(database: Session = Depends(database.get_db)):
  users = RepositoryUser(database).index()
  return users