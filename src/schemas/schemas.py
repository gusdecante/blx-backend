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

class UserReponse(BaseModel):
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
  user: Optional[UserReponse]

  class Config:
    orm_mode = True



class Deal(BaseModel):
  id: Optional[int] = None
  qtt: int
  delivery_place: Optional[str]
  delivery_type: str
  comments: Optional[str] = "Sem observações"
  
  user_id: Optional[int]
  product_id: Optional[int]

  user: Optional[UserReponse]
  product: Optional[ProductResponse]

  class Config:
      orm_mode = True

