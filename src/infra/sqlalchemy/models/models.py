from sqlalchemy import Column, Integer, Float, Boolean, String
from src.infra.sqlalchemy.config.database import Base

class Product(Base):

  __tablename__ = 'product'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  details = Column(String)
  price = Column(Float)
  available = Column(Boolean)

class User(Base):

  __tablename__ = 'user'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  phone = Column(String)