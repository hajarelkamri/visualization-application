#  SciDataViz - Application de Visualisation de Données Scientifiques

Une application desktop complète pour l'analyse et la visualisation de données scientifiques avec une interface utilisateur intuitive.


##  Description

SciDataViz est une application desktop développée en Python qui permet aux scientifiques, chercheurs et analystes de données de visualiser et analyser leurs ensembles de données de manière interactive. L'application offre une suite complète d'outils pour le nettoyage, l'analyse statistique et la visualisation de données.

##  Fonctionnalités

###  Système d'Authentification
- **Inscription** et **connexion** sécurisées des utilisateurs
- Interface moderne avec design responsive
- Gestion des sessions utilisateur

###  Gestion des Données
- **Importation** de fichiers CSV
- **Nettoyage automatique** des données :
  - Suppression des doublons
  - Gestion des valeurs manquantes
  - Correction des valeurs aberrantes
- **Affichage tabulaire** avec navigation

###  Analyse Statistique
- Calcul des **mesures statistiques** :
  - Moyenne, Médiane
  - Écart-type
  - Quartiles
- **Matrice de corrélation** interactive
- Analyse en temps réel

###  Visualisations Avancées
- **Graphiques en barres** personnalisables
- **Nuages de points** (Scatter plots)
- **Camemberts** (Pie charts)
- **Courbes** (Line charts)
- **Export** des visualisations combinées

###  Interface Utilisateur
- Design **moderne et ergonomique**
- **Sidebar** de navigation intuitive
- **Dashboard** en temps réel avec horloge
- Thème coloré professionnel

##  Technologies Utilisées

### Backend
- **Python 3.8+** - Langage principal
- **Pandas** - Manipulation des données
- **NumPy** - Calculs scientifiques
- **Matplotlib/Seaborn** - Visualisations
- **PIL (Pillow)** - Traitement d'images

### Frontend
- **Tkinter** - Interface graphique
- **ttk** - Widgets thématiques modernes
- **FigureCanvasTkAgg** - Intégration des graphiques

### Autres
- **CSV** - Format de données
- **Pickle** - Sérialisation
- **OS** - Gestion des fichiers

## Installation

### Prérequis
- Python 3.8 ou supérieur
- pip 

### Installation


Cloner le repository : 
```bash
git clone https://github.com/hajarelkamri/SciDataViz.git
cd SciDataViz
Créer un environnement virtuel 
python -m venv venv
# Sur Windows
venv\Scripts\activate
# Sur Mac/Linux
source venv/bin/activate
Installer les dépendances
pip install -r requirements.txt
Dépendances principales
shell
Copier le code
pandas>=1.5.0
numpy>=1.21.0
matplotlib>=3.5.0
seaborn>=0.11.0
pillow>=9.0.0
 Utilisation  : 
Lancement de l'application: 

python SciDataViz.py
Workflow typique
Authentification

Créer un compte ou se connecter

Interface sécurisée avec validation

Importation des données

Naviguer vers "Upload CSV file"

Sélectionner votre fichier CSV

Nettoyage des données

Accéder à "Cleaning data"

Application automatique des traitements

Validation des résultats

Analyse statistique

Consultation des mesures dans le sidebar

Visualisation de la matrice de corrélation

Visualisation

Accéder à "Data visualization"

Créer différents types de graphiques

Personnaliser les axes et paramètres

Export

Générer un dashboard combiné
