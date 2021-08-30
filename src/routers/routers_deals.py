from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config import database
from src.schemas import schemas
from src.infra.sqlalchemy.repository.repository_deal import RepositoryDeal

router = APIRouter()

@router.post('/deals', status_code=status.HTTP_201_CREATED, response_model=schemas.Deal)
def create(deal: schemas.Deal, database: Session = Depends(database.get_db)):
    created_deal = RepositoryDeal(database).create(deal)
    return created_deal

@router.get('/deals/{id}', response_model=schemas.Deal)
def get_deal_by_id(id: int, database: Session = Depends(database.get_db)):
    try:
        deal = RepositoryDeal(database).get_deal_by_id(id)
        return deal
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Deal with the id={id} Not Found")

@router.get('/deals/{user_id}/purchases', response_model=List[schemas.Deal])
def index_deals(user_id: int, database: Session = Depends(database.get_db)):
    deals = RepositoryDeal(database).index_deals_by_user_id(user_id)
    return deals

@router.get('/deals/{user_id}/sales', response_model=List[schemas.Deal])
def index_sales(user_id: int, database: Session = Depends(database.get_db)):
    deals = RepositoryDeal(database).index_sales_by_user_id(user_id)
    return deals

