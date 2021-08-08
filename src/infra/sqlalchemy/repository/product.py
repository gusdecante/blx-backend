from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryProduct():
  def __init__(self, database: Session):
    self.database = database
  # schema - é o que vai e volta do request
  # model - é o que vai e volta do banco de dados
  def create(self, product: schemas.Product):
    db_product = models.Product(name=product.name, details=product.details, price=product.price, available=product.available)

    self.database.add(db_product)
    self.database.commit()
    self.database.refresh(db_product)
    return db_product

  def index(self):
    products = self.database.query(models.Product).all()
    return products