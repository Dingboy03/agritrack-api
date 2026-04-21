from fastapi.testclient import TestClient
from app.main import app


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


def test_creer_recolte_poids_negatif(client, db_session):
    response = client.post("/api/recoltes", json={
        "type_produit": "karité",
        "poids_kg": -50,
        "date": "2025-03-15",
        "id_agriculteur": db_session["agriculteur_id"],
        "id_entrepot": db_session["entrepot_id"]
    })

    assert response.status_code == 400