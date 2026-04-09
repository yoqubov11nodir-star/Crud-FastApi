from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from . import views, schemas

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=list[schemas.ProductResponse])
def read_all(db: Session = Depends(get_db)):
    return views.get_all(db)

@router.post("/", response_model=schemas.ProductResponse)
def create_item(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return views.create(db, product)

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