# 🌾 Agri-Track API

![CI](https://github.com/Dingboy03/agritrack-api/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)

> API de traçabilité agricole des récoltes (coton, mangues, karité)
> depuis le champ de l'agriculteur jusqu'à l'entrepôt d'exportation — Burkina Faso.



## 📌 Description & Contexte

Agri-Track est une API backend conçue pour les coopératives agricoles
du Burkina Faso. Elle permet d'enregistrer chaque récolte à la sortie
du champ et de suivre les stocks en entrepôt en temps réel.
Le système garantit l'intégrité des données : validation des poids,
contrôle des types de produits autorisés, et traçabilité complète
de l'agriculteur jusqu'à l'entrepôt d'exportation.



##  Prérequis & Installation

**Versions requises :**
- Python 3.11+
- pip 23+

**Installation pas à pas :**

```bash
# 1. Cloner le dépôt
git clone https://github.com/Dingboy03/agritrack-api.git
cd agritrack-api

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate
# Windows : venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'API
uvicorn main:app --reload
```

- API disponible sur : `http://127.0.0.1:8000`
- Documentation interactive : `http://127.0.0.1:8000/docs`



## 🚀 Utilisation & Exemples

### Enregistrer une récolte

```bash
curl -X POST http://127.0.0.1:8000/recoltes \
  -H "Content-Type: application/json" \
  -d '{
    "type_produit": "coton",
    "poids_kg": 150.5,
    "date": "2026-04-17",
    "id_agriculteur": 1,
    "id_entrepot": 2
  }'
```

**Réponse (201) :**
```json
{
  "message": "Récolte enregistrée avec succès",
  "id": 1
}
```

### Consulter le stock d'un entrepôt

```bash
curl http://127.0.0.1:8000/entrepots/2/stock
```

**Réponse (200) :**
```json
{
  "entrepot_id": 2,
  "nom": "Entrepôt Bobo-Dioulasso",
  "stock_total_kg": 450.5,
  "capacite_max_kg": 15000
}
```

### Codes d'erreur

| Code | Cause |
|---|---|
| 400 | Poids négatif ou nul |
| 400 | Produit hors liste (coton / mangue / karité) |
| 404 | Entrepôt introuvable |



## 🧪 Lancer les tests

```bash
pytest tests/
```



##  Guide de Contribution

1. Ne jamais coder directement sur `main`
2. Créer une branche de feature :
```bash
git checkout -b feature/nom-de-la-feature
```
3. Respecter la convention de nommage des commits :

| Type | Usage |
|---|---|
| `feat` | Nouvelle fonctionnalité |
| `fix` | Correction de bug |
| `test` | Ajout ou modification de tests |
| `docs` | Documentation |
| `ci` | Fichiers GitHub Actions / pipeline |

**Exemple :** `feat(recoltes): ajouter la route POST /recoltes`

4. Pousser la branche et ouvrir une Pull Request vers `main`
5. Attendre l'approbation d'au moins 1 membre de l'équipe
6. Le pipeline CI doit être  vert avant tout merge



##  Équipe

| Membre | Rôle |
|---|---|
| Azania | Scrum Master |
| Djamel | Développeur 1 — Feature enregistrement |
| Abdoulfatah | Développeur 2 — Feature stock & Tests |


##  Équipe

| Membre | Rôle |
|---|---|
| Azania | Scrum Master |
| Djamel | Développeur 1 — Feature enregistrement |
| Abdoulfatah | Développeur 2 — Feature stock & Tests |

##  Licence

Ce projet est sous licence [MIT](LICENSE).

##  Licence

Ce projet est sous licence [MIT](LICENSE).
