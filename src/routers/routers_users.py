from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from src.infra.sqlalchemy.config import database
from src.schemas import schemas
from src.infra.sqlalchemy.repository.repository_user import RepositoryUser

router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED)
def signup(user: schemas.User, database: Session = Depends(database.get_db)):
  create_user = RepositoryUser(database).create(user)
  return create_user

@router.get('/users', status_code=status.HTTP_200_OK, response_model=List[schemas.User])
def list_users(database: Session = Depends(database.get_db)):
  users = RepositoryUser(database).index()
  return users