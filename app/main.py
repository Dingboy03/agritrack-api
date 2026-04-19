from fastapi import FastAPI
from app.routes import recoltes, agriculteurs, entrepots
from app.database import engine, Base
from app import models

# Créer toutes les tables
print("Création des tables...")
Base.metadata.create_all(bind=engine)
print("Tables créées avec succès!")

app = FastAPI(title="Agri-Track API", description="API de traçabilité agricole", version="1.0.0")

# Inclure les routes
app.include_router(recoltes.router, prefix="/api", tags=["Récoltes"])
app.include_router(agriculteurs.router, prefix="/api", tags=["Agriculteurs"])
app.include_router(entrepots.router, prefix="/api", tags=["Entrepôts"])

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API Agri-Track", "status": "online"}

@app.get("/health")
def health():
    return {"status": "OK"}