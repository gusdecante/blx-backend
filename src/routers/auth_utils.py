from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm.session import Session
from jose import JWTError
from src.infra.sqlalchemy.config import database
from src.infra.providers import token_provider
from src.infra.sqlalchemy.repository.repository_user import RepositoryUser

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

def obtain_logged_user(token: str = Depends(oauth2_schema), database: Session = Depends(database.get_db)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
    try:
        phone = token_provider.verify_access_token(token)
    except JWTError:
        raise exception

    if not phone:
        raise exception

    user = RepositoryUser(database).get_by_phone(phone)

    if not user:
        raise exception

    return user