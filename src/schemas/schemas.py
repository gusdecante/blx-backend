from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
  id: Optional[str] = None
  name: str
  password: str
  phone: str
  # myProducts: List[Product]
  # mySales: List[Request]
  # myPurchases: List[Request]
  
  class Config:
    orm_mode = True

class Product(BaseModel):
  id: Optional[str] = None
  # user: User
  name: str
  details: str
  price: float
  available: bool = False

  class Config:
    orm_mode = True

class ProductResponse(BaseModel):
  name: str
  details: str
  price: float

  class Config:
    orm_mode = True

class Request(BaseModel):
  id: Optional[str] = None
  user: User
  product: Product
  quantity: int
  delivery: bool = True
  address: str
  observations: Optional[str] = "Sem observações"
