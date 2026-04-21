from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Agriculteur(Base):
    __tablename__ = "agriculteurs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nom = Column(String(100), nullable=False)
    cooperative = Column(String(100), nullable=False)
    telephone = Column(String(20), unique=True)

    recoltes = relationship("Recolte", back_populates="agriculteur")


class Entrepot(Base):
    __tablename__ = "entrepots"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nom_lieu = Column(String(100), nullable=False)
    capacite_max = Column(Float, nullable=False)

    recoltes = relationship("Recolte", back_populates="entrepot")


class Recolte(Base):
    __tablename__ = "recoltes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type_produit = Column(String(50), nullable=False)
    poids_kg = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    id_agriculteur = Column(Integer, ForeignKey("agriculteurs.id"), nullable=False)
    id_entrepot = Column(Integer, ForeignKey("entrepots.id"), nullable=False)

    agriculteur = relationship("Agriculteur", back_populates="recoltes")
    entrepot = relationship("Entrepot", back_populates="recoltes")
