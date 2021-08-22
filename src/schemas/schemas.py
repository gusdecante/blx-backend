from pydantic import BaseModel
from typing import Optional, List

class ProductResponse(BaseModel):
  id: Optional[int] = None
  name: str
  details: str
  price: float
  available: bool

  class Config:
    orm_mode = True

class User(BaseModel):
  id: Optional[int] = None
  name: str
  password: Optional[str]
  phone: str
  products: List[ProductResponse] = []
  # myProducts: List[Product]
  # mySales: List[Request]
  # myPurchases: List[Request]
  
  class Config:
    orm_mode = True

class UserRequest(BaseModel):
  id: Optional[int] = None
  name: str
  phone: str
  
  class Config:
    orm_mode = True

class Product(BaseModel):
  id: Optional[int] = None
  # user: User
  name: str
  details: str
  price: float
  available: bool = False
  user_id: Optional[int]
  user: Optional[UserRequest]

  class Config:
    orm_mode = True



class Request(BaseModel):
  id: Optional[int] = None
  user: User
  product: Product
  quantity: int
  delivery: bool = True
  address: str
  observations: Optional[str] = "Sem observações"
