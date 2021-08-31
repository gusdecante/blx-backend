from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.infra.sqlalchemy.config import database
from src.schemas import schemas
from src.infra.sqlalchemy.repository.repository_user import RepositoryUser
from src.infra.providers import hash_provider

router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=schemas.UserReponse)
def signup(user: schemas.User, database: Session = Depends(database.get_db)):
  is_phone_exist = RepositoryUser(database).get_by_phone(user.phone)

  if is_phone_exist:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already exist a user with this phone")
  user.password = hash_provider.generate_hash(user.password)
  create_user = RepositoryUser(database).create(user)
  return create_user
