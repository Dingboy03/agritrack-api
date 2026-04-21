from app.database import SessionLocal, engine, Base
from app import models


def init_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        agriculteurs = [
            models.Agriculteur(
                nom="Amadou Diallo",
                cooperative="Coopérative Nord",
                telephone="70123456"
            ),
            models.Agriculteur(
                nom="Fatoumata Sanou",
                cooperative="Coopérative Sud",
                telephone="70234567"
            ),
            models.Agriculteur(
                nom="Ibrahim Traoré",
                cooperative="Coopérative Est",
                telephone="70345678"
            ),
        ]

        for agriculteur in agriculteurs:
            db.add(agriculteur)

        entrepots = [
            models.Entrepot(
                nom_lieu="Entrepôt Principal Ouagadougou",
                capacite_max=10000.0
            ),
            models.Entrepot(
                nom_lieu="Entrepôt Secondaire Bobo-Dioulasso",
                capacite_max=7500.0
            ),
        ]

        for entrepot in entrepots:
            db.add(entrepot)

        db.commit()

        print("✅ Base de données initialisée avec succès!")
        print(f"📊 {len(agriculteurs)} agriculteurs ajoutés")
        print(f"🏭 {len(entrepots)} entrepôts ajoutés")

    except Exception as e:
        print(f"❌ Erreur: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    init_database()
