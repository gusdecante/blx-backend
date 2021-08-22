from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from src.schemas import schemas
from src.infra.sqlalchemy.config import database
from src.infra.sqlalchemy.repository.repository_product import RepositoryProduct

router = APIRouter()

# Depends injeção de dependência
@router.post('/products', status_code=status.HTTP_201_CREATED, response_model=schemas.ProductResponse)
def create_products(product: schemas.Product, database: Session = Depends(database.get_db)):
  created_product = RepositoryProduct(database).create(product)
  return created_product

@router.get('/products', status_code=status.HTTP_200_OK, response_model=List[schemas.Product])
def list_products(database: Session = Depends(database.get_db)):
  products = RepositoryProduct(database).index()
  return products

@router.put('/products/{id}', response_model=schemas.ProductResponse)
def update_products(id: int, product: schemas.Product, database: Session = Depends(database.get_db)):
  RepositoryProduct(database).update(id, product)
  product.id = id
  return product

@router.delete('/products/{id}')
def delete_products(id: int, database: Session = Depends(database.get_db)):
  RepositoryProduct(database).delete(id)
  return id