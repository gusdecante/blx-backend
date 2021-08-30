from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryProduct():
  def __init__(self, database: Session):
    self.database = database
  # schema - é o que vai e volta do request
  # model - é o que vai e volta do banco de dados
  def create(self, product: schemas.Product):
    db_product = models.Product(name=product.name, details=product.details, price=product.price, available=product.available, user_id=product.user_id)

    self.database.add(db_product)
    self.database.commit()
    self.database.refresh(db_product)
    return db_product

  def index(self):
    products = self.database.query(models.Product).all()
    return products

  def get_by_id(self, id: int):
    query = select(models.Product).where(models.Product.id == id)
    product = self.database.execute(query).first()
    return product

  def update(self, id: int, product: schemas.Product):
    update_stmt = update(models.Product).where(models.Product.id == id).values(name=product.name,
    details=product.details, price=product.price, available=product.available)
    self.database.execute(update_stmt)
    self.database.commit()

  def delete(self, id: int):
    delete_stmt = delete(models.Product).where(models.Product.id == id)
    self.database.execute(delete_stmt)
    self.database.commit()
    