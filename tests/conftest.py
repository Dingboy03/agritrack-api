import sys
import os

# Ajouter le chemin du projet
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine, Base
from app import models


@pytest.fixture(scope="function")
def client():
    return TestClient(app)


@pytest.fixture(scope="function")
def db_session():
    # Supprimer et recréer les tables
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Créer les données de test
    agriculteur = models.Agriculteur(
        nom="Test Farmer",
        cooperative="Coop Test",
        telephone="12345678"
    )
    db.add(agriculteur)

    entrepot = models.Entrepot(
        nom_lieu="Entrepôt Test",
        capacite_max=1000.0
    )
    db.add(entrepot)

    db.commit()

    # Rafraîchir pour obtenir les IDs
    db.refresh(agriculteur)
    db.refresh(entrepot)

    yield {
        "db": db,
        "agriculteur_id": agriculteur.id,
        "entrepot_id": entrepot.id
    }

    db.close()