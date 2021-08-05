from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
  id: Optional[str] = None
  name: str
  phone: str
  myProducts: List[Product]
  mySales: List[Request]
  myPurchases: List[Request]

class Product(BaseModel):
  id: Optional[str] = None
  user: User
  name: str
  details: str
  price: float
  available: bool = False

class Request(BaseModel):
  id: Optional[str] = None
  user: User
  product: Product
  quantity: int
  delivery: bool = True
  address: str
  observations: Optional[str] = "Sem observações"
