import sys
import os
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
    
    yield {"db": db, "agriculteur_id": agriculteur.id, "entrepot_id": entrepot.id}
    
    db.close()

def test_creer_recolte_succes(client, db_session):
    response = client.post("/api/recoltes", json={
        "type_produit": "coton",
        "poids_kg": 150.5,
        "date": "2025-03-15",
        "id_agriculteur": db_session["agriculteur_id"],
        "id_entrepot": db_session["entrepot_id"]
    })
    
    assert response.status_code == 201
    data = response.json()
    assert data["type_produit"] == "coton"
    assert data["poids_kg"] == 150.5

def test_creer_recolte_poids_zero(client, db_session):
    response = client.post("/api/recoltes", json={
        "type_produit": "mangue",
        "poids_kg": 0,
        "date": "2025-03-15",
        "id_agriculteur": db_session["agriculteur_id"],
        "id_entrepot": db_session["entrepot_id"]
    })
    
    assert response.status_code == 400

def test_creer_recolte_produit_invalide(client, db_session):
    response = client.post("/api/recoltes", json={
        "type_produit": "ananas",
        "poids_kg": 50,
        "date": "2025-03-15",
        "id_agriculteur": db_session["agriculteur_id"],
        "id_entrepot": db_session["entrepot_id"]
    })
    
    assert response.status_code == 400

# Test A — Poids négatif → HTTP 400
def test_creer_recolte_poids_negatif(client, db_session):
    response = client.post("/api/recoltes", json={
        "type_produit": "coton",
        "poids_kg": -50,
        "date": "2025-03-15",
        "id_agriculteur": db_session["agriculteur_id"],
        "id_entrepot": db_session["entrepot_id"]
    })
    assert response.status_code == 400

# Test B — Somme de 3 récoltes → 450 kg
def test_stock_entrepot_somme(client, db_session):
    for poids in [100, 200, 150]:
        client.post("/api/recoltes", json={
            "type_produit": "coton",
            "poids_kg": poids,
            "date": "2025-03-15",
            "id_agriculteur": db_session["agriculteur_id"],
            "id_entrepot": db_session["entrepot_id"]
        })
    
    response = client.get(f"/api/entrepots/{db_session['entrepot_id']}/stock")
    assert response.status_code == 200
    assert response.json()["stock_total_kg"] == 450.0