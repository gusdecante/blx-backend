from pydantic.schema import schema
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryUser():
  def __init__(self, database: Session):
    self.database = database

  def create(self, user: schemas.User):
    db_user = models.User(name= user.name, password=user.password, phone=user.phone)

    self.database.add(db_user)
    self.database.commit()
    self.database.refresh(db_user)
    return db_user

  def index(self):
    users = self.database.query(models.User).all()
    return users

  def get_by_phone(self, phone) -> schemas.User:
    query = select(models.User).where(models.User.phone == phone)
    return self.database.execute(query).scalars().first()