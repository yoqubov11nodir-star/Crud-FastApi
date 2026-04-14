from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from . import views, schemas
from typing import Optional

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=list[schemas.ProductResponse])
def read_all(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query("", description="Nomi bo'yicha qidirish")
):
    return views.get_all(db, skip=skip, limit=limit, search=search)

@router.post("/", response_model=schemas.ProductResponse)
def create_item(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return views.create(db, product)

@router.get("/{product_id}", response_model=schemas.ProductResponse)
def read_one(product_id: int, db: Session = Depends(get_db)):
    res = views.get_one(db, product_id)
    if not res: raise HTTPException(status_code=404, detail="Topilmadi")
    return res

@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_item(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    res = views.update(db, product_id, product)
    if not res: raise HTTPException(status_code=404, detail="Topilmadi")
    return res

@router.delete("/{product_id}")
def delete_item(product_id: int, db: Session = Depends(get_db)):
    res = views.delete(db, product_id)
    if not res: raise HTTPException(status_code=404, detail="Topilmadi")
    return {"message": "O'chirildi"}