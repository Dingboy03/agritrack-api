# 🌾 Agri-Track API

API de traçabilité agricole pour l'enregistrement des récoltes (coton, mangues, karité) au Burkina Faso.

## 🚀 Installation

### 1. Cloner le projet
git clone https://github.com/Dingboy03/agritrack-api.git

cd agritrack-api

### 2. Créer un environnement virtuel
python -m venv venv
venv\Scripts\activate

### 3. Installer les dépendances
pip install -r requirements.txt

### 4. Initialiser la base de données
python init_db.py

Cela va créer :

✅ 3 agriculteurs de test

✅ 2 entrepôts de test

✅ Les tables nécessaires

### 5. Lancer l'API
uvicorn app.main:app --reload

### 6.📚 Documentation interactive

Une fois l'API lancée, accède à :

Swagger UI : http://localhost:8000/docs


### 7.🧪 Tester l'API

.Aller sur http://localhost:8000/docs

.Clique sur POST /api/recoltes

.Clique sur "Try it out"

.Remplis le formulaire

.Exécute

### 8.🧪 Lancer les tests

pytest tests/test_recoltes.py -v

Résultat attendu :

#tests/test_recoltes.py::test_creer_recolte_succes PASSED
#tests/test_recoltes.py::test_creer_recolte_poids_zero PASSED
#tests/test_recoltes.py::test_creer_recolte_produit_invalide PASSED
#tests/test_recoltes.py::test_creer_recolte_poids_negatif PASSED

### 9.📋 Données de test disponibles

#Agriculteurs (après init_db.py)

ID	Nom	Coopérative	Téléphone

1	Amadou Diallo	Coopérative Nord	70123456

2	Fatoumata Sanou	Coopérative Sud	70234567

3	Ibrahim Traoré	Coopérative Est	70345678

#Entrepôts

ID	Lieu	Capacité max (kg)

1	Entrepôt Principal Ouagadougou	10000

2	Entrepôt Secondaire Bobo-Dioulasso	7500

### 10.📦 Technologies utilisées

FastAPI - Framework web

SQLAlchemy - ORM

SQLite - Base de données

Pytest - Tests unitaires

Uvicorn - Serveur ASGI

# 👥 Équipe

Développeur : @DjamelSteephen

Projet : Agri-Track - Traçabilité agricole
