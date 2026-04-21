from fastapi import APIRouter, HTTPException, Depends, status
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
    "/recoltes",
    response_model=schemas.RecolteResponse,
    status_code=status.HTTP_201_CREATED
)
def enregistrer_recolte(
    recolte: schemas.RecolteCreate,
    db: Session = Depends(get_db)
):
    produits_autorises = ["coton", "mangue", "karité"]

    if recolte.type_produit not in produits_autorises:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Type de produit invalide. "
                f"Choisir parmi: {', '.join(produits_autorises)}"
            )
        )

    if recolte.poids_kg <= 0:
        raise HTTPException(
            status_code=400,
            detail="Le poids doit être strictement supérieur à 0"
        )

    agriculteur = db.query(models.Agriculteur).filter(
        models.Agriculteur.id == recolte.id_agriculteur
    ).first()
    if not agriculteur:
        raise HTTPException(
            status_code=404,
            detail="Agriculteur non trouvé"
        )

    entrepot = db.query(models.Entrepot).filter(
        models.Entrepot.id == recolte.id_entrepot
    ).first()
    if not entrepot:
        raise HTTPException(
            status_code=404,
            detail="Entrepôt non trouvé"
        )

    stock_actuel = db.query(models.Recolte).filter(
        models.Recolte.id_entrepot == recolte.id_entrepot
    ).all()
    total_actuel = sum([r.poids_kg for r in stock_actuel])

    if total_actuel + recolte.poids_kg > entrepot.capacite_max:
        raise HTTPException(
            status_code=400,
            detail="Capacité maximale de l'entrepôt dépassée"
        )

    db_recolte = models.Recolte(**recolte.model_dump())
    db.add(db_recolte)
    db.commit()
    db.refresh(db_recolte)

    return db_recolte


@router.get("/recoltes", response_model=list[schemas.RecolteResponse])
def lister_recoltes(db: Session = Depends(get_db)):
    return db.query(models.Recolte).all()
