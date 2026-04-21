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
    "/agriculteurs",
    response_model=schemas.AgriculteurResponse,
    status_code=status.HTTP_201_CREATED
)
def creer_agriculteur(
    agriculteur: schemas.AgriculteurCreate,
    db: Session = Depends(get_db)
):
    db_agriculteur = models.Agriculteur(**agriculteur.dict())
    db.add(db_agriculteur)
    db.commit()
    db.refresh(db_agriculteur)
    return db_agriculteur


@router.get("/agriculteurs", response_model=list[schemas.AgriculteurResponse])
def lister_agriculteurs(db: Session = Depends(get_db)):
    return db.query(models.Agriculteur).all()
