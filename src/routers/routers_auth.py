from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config import database
from src.schemas import schemas
from src.infra.sqlalchemy.repository.repository_user import RepositoryUser
from src.infra.providers import hash_provider, token_provider
from src.routers.auth_utils import obtain_logged_user

router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=schemas.UserReponse)
def signup(user: schemas.User, database: Session = Depends(database.get_db)):
  is_phone_exist = RepositoryUser(database).get_by_phone(user.phone)

  if is_phone_exist:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already exist a user with this phone")
  
  user.password = hash_provider.generate_hash(user.password)
  create_user = RepositoryUser(database).create(user)
  return create_user

@router.post('/token', response_model=schemas.LoginSuccess,status_code=status.HTTP_200_OK)
def login(login_data: schemas.LoginData, database: Session = Depends(database.get_db)):
  password = login_data.password
  phone = login_data.phone

  user = RepositoryUser(database).get_by_phone(phone)

  if not user:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Credentials are incorrect")
  
  password_checked = hash_provider.verify_hash(password, user.password)

  if not password_checked:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Credentials are incorrect")

  token = token_provider.create_access_token({'sub': user.phone})
  return schemas.LoginSuccess(user=user, access_token=token)

@router.get('/me', response_model=schemas.UserReponse)
def me(user: schemas.User = Depends(obtain_logged_user), database: Session = Depends(database.get_db)):
  return user