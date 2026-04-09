from sqlalchemy.orm import Session
from . import models, schemas

def get_all(db: Session):
    return db.query(models.Product).all()

def get_one(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def create(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update(db: Session, product_id: int, product_data: schemas.ProductCreate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db_product.name = product_data.name
        db_product.price = product_data.price
        db_product.description = product_data.description
        db.commit()
        db.refresh(db_product)
    return db_product

def delete(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product