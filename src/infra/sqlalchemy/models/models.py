from sqlalchemy import Column, Integer, Float, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

class User(Base):

  __tablename__ = 'user'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  password = Column(String)
  phone = Column(String)
  
  products = relationship('Product', back_populates='user')
  deals = relationship('Deal', back_populates='user')
  
class Product(Base):

  __tablename__ = 'product'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  details = Column(String)
  price = Column(Float)
  available = Column(Boolean)
  sizes = Column(String)
  user_id = Column(Integer, ForeignKey('user.id', name='fk_user'))
  
  user = relationship('User', back_populates='products')

class Deal(Base):
  __tablename__ = 'deal'

  id = Column(Integer, primary_key=True, index=True)
  qtt = Column(Integer)
  delivery_place = Column(String)
  delivery_type = Column(String)
  comments = Column(String)
  
  user_id = Column(Integer, ForeignKey('user.id', name='fk_deal_user'))
  product_id = Column(Integer, ForeignKey('product.id', name='fk_deal_product'))

  user = relationship('User', back_populates='deals')
  product = relationship('Product')
