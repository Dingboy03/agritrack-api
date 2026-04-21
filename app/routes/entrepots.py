from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/entrepots",
    response_model=schemas.EntrepotResponse,
    status_code=status.HTTP_201_CREATED
)
def creer_entrepot(
    entrepot: schemas.EntrepotCreate,
    db: Session = Depends(get_db)
):
    db_entrepot = models.Entrepot(**entrepot.dict())
    db.add(db_entrepot)
    db.commit()
    db.refresh(db_entrepot)
    return db_entrepot


@router.get("/entrepots", response_model=list[schemas.EntrepotResponse])
def lister_entrepots(db: Session = Depends(get_db)):
    return db.query(models.Entrepot).all()
