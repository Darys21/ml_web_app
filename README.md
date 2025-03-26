# MLFlowApp - Application de Formation de Modèles ML

Cette application web permet de gérer et d'entraîner des modèles de machine learning sur des données de traduction texte.

## Fonctionnalités

- **Gestion des données**
  - Upload de fichiers CSV contenant des paires de traduction (texte source → texte cible)
  - Support des fichiers CSV avec les colonnes 'input' et 'target'

- **Entraînement des modèles**
  - Choix entre différents algorithmes de ML :
    - Régression Linéaire
    - Random Forest
  - Interface web intuitive pour sélectionner le modèle
  - Sauvegarde automatique des modèles entraînés

- **Visualisation des résultats**
  - Affichage des métriques de performance
  - Génération de graphiques comparatifs
  - Interface de visualisation interactive

## Structure du Projet

```
.
├── app.py              # Point d'entrée de l'application Flask
├── data/               # Dossier pour les fichiers CSV
├── models/            # Dossier pour les modèles sauvegardés
├── static/            # Fichiers statiques (CSS, images)
├── templates/         # Templates HTML
└── requirements.txt   # Dépendances Python
```

## Installation

1. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Initialiser DVC pour la gestion des données :
```bash
dvc init
dvc add data
```

## Utilisation

1. Lancer l'application :
```bash
python app.py
```

2. Accéder à l'interface web :
```
http://localhost:5000
```

3. Suivre ces étapes :
   - Uploader un fichier CSV
   - Sélectionner un modèle
   - Entraîner le modèle
   - Voir les résultats

## Technologies Utilisées

- Backend: Flask
- Versioning: DVC
- ML: Scikit-learn
- Visualisation: Matplotlib

## Notes

- Les fichiers de données sont suivis avec DVC pour une meilleure gestion des versions
- Les modèles entraînés sont sauvegardés dans le dossier 'models/'
- Les résultats de l'entraînement sont visualisés via une interface web interactive
