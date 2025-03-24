from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from order_detail.model import OrderDetail
from order_detail.schema import OrderDetailCreate, OrderDetailResponse

router = APIRouter(prefix="/order-details", tags=["Order Details"])

@router.post("/", response_model=OrderDetailResponse)
def create_order_detail(detail: OrderDetailCreate, db: Session = Depends(get_db)):
    new_detail = OrderDetail(**detail.dict())
    db.add(new_detail)
    db.commit()
    db.refresh(new_detail)
    return new_detail

@router.get("/{detail_id}", response_model=OrderDetailResponse)
def get_order_detail(detail_id: int, db: Session = Depends(get_db)):
    detail = db.query(OrderDetail).filter(OrderDetail.id == detail_id).first()
    if not detail:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return detail
