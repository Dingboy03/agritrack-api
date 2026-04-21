from pydantic import BaseModel
from datetime import date


class RecolteCreate(BaseModel):
    type_produit: str
    poids_kg: float
    date: date
    id_agriculteur: int
    id_entrepot: int


class RecolteResponse(RecolteCreate):
    id: int

    class Config:
        from_attributes = True


class AgriculteurCreate(BaseModel):
    nom: str
    cooperative: str
    telephone: str


class AgriculteurResponse(AgriculteurCreate):
    id: int

    class Config:
        from_attributes = True


class EntrepotCreate(BaseModel):
    nom_lieu: str
    capacite_max: float


class EntrepotResponse(EntrepotCreate):
    id: int

    class Config:
        from_attributes = True
