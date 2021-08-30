from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryDeal():
    def __init__(self, database: Session):
        self.database = database

    def create(self, deal: schemas.Deal):
        db_deal = models.Deal(qtt=deal.qtt, delivery_place=deal.delivery_place, delivery_type=deal.delivery_type, comments=deal.comments, user_id=deal.user_id, product_id=deal.product_id)

        self.database.add(db_deal)
        self.database.commit()
        self.database.refresh(db_deal)
        return db_deal

    def get_deal_by_id(self, id: int):
        query = select(models.Deal).where(models.Deal.id == id)
        deal = self.database.execute(query).one()
        return deal[0]

    def index_deals_by_user_id(self, user_id: int):
        query = select(models.Deal).where(models.Deal.user_id == user_id)
        deals = self.database.execute(query).scalars().all()
        return deals

    def index_sales_by_user_id(self, user_id: int):
        query = select(models.Deal, models.Product).join_from(models.Deal, models.Product).where(models.Product.user_id == user_id)
        deals = self.database.execute(query).scalars().all()
        return deals