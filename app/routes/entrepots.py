from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy import func
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


@router.get("/entrepots/{id}/stock")
def get_stock_entrepot(id: int, db: Session = Depends(get_db)):
    # Vérifier que l'entrepôt existe
    entrepot = db.query(models.Entrepot).filter(models.Entrepot.id == id).first()
    if not entrepot:
        raise HTTPException(status_code=404, detail="Entrepôt non trouvé")
    
    # Calculer la somme des poids
    total = db.query(func.sum(models.Recolte.poids_kg)).filter(models.Recolte.id_entrepot == id).scalar()
    
    return {
        "entrepot_id": id,
        "nom_lieu": entrepot.nom_lieu,
        "stock_total_kg": total or 0.0
    }
