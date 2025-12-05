# 🧠 MiniMind

> **Projet réalisé dans le cadre de la Nuit de l'Info 2025 - Défi AI4GOOD**

MiniMind est une application pédagogique interactive permettant aux jeunes de **découvrir et expérimenter l'intelligence artificielle** de manière simple et ludique. Ce projet combine un agent IA conversationnel avec des outils d'analyse de texte et de visualisation de données.

## 🎯 Objectif

Permettre aux collégiens, lycéens et étudiants débutants de comprendre le fonctionnement de l'IA à travers :
- Une interface conversationnelle intuitive
- Des outils d'analyse de texte en temps réel
- Des visualisations de données interactives
- Une expérience d'apprentissage pratique et engageante

## ✨ Fonctionnalités

### 🤖 Agent IA Conversationnel
- Interface de chat interactive propulsée par Google Gemini
- Réponses intelligentes et contextuelles
- Personnalisation de l'interface (changement de couleur de fond)

### 📊 Analyse de Texte
- **Analyse de sentiment** : Détecte si un texte est positif, négatif ou neutre
- **Détection d'émotions** : Identifie les émotions spécifiques (joie, colère, tristesse, peur, surprise)
- **Extraction de mots-clés** : Trouve les mots les plus importants dans un texte
- **Analyse d'entités** : Identifie les personnes, lieux, organisations mentionnés
- **Analyse de lisibilité** : Évalue la complexité et le niveau de lecture d'un texte
- **Fréquence des mots** : Analyse les mots les plus fréquents

### 📈 Visualisation de Données
- **Graphiques en nuage de points** : Visualisation de corrélations
- **Graphiques en barres** : Comparaison de données catégorielles
- Données basées sur le dataset `tips.csv`

## 🛠️ Technologies Utilisées

### Backend
- **Python 3.x**
- **Strands Agents** : Framework pour créer des agents IA
- **Google Gemini AI** : Modèle de langage pour l'IA conversationnelle
- **FastAPI** : API web performante
- **Pandas & NumPy** : Analyse de données
- **Matplotlib** : Visualisation de données
- **TextBlob & scikit-learn** : Traitement du langage naturel

### Frontend
- **Next.js 16** : Framework React pour l'interface utilisateur
- **React 19** : Bibliothèque UI
- **TypeScript** : Typage statique
- **TailwindCSS** : Styling moderne
- **CopilotKit** : Intégration de l'agent IA
- **AG UI Client** : Interface utilisateur pour l'agent

## 📦 Installation

### Prérequis
- Python 3.8 ou supérieur
- Node.js 18 ou supérieur
- npm ou pnpm

### 1. Cloner le dépôt
```bash
git clone https://github.com/keynar-erwann/MiniMind.git
cd MiniMind
```

### 2. Configuration du Backend

```bash
# Installer les dépendances Python
pip install -r requirements.txt

# Créer un fichier .env et ajouter votre clé API Google Gemini
echo "GOOGLE_API_KEY=votre_clé_api_ici" > .env
```

### 3. Configuration du Frontend

```bash
# Aller dans le dossier frontend
cd frontend

# Installer les dépendances
pnpm install
# ou
npm install
```

## 🚀 Utilisation

### Démarrer le Backend

```bash
# À la racine du projet
python agent.py
```

L'agent IA démarrera et sera accessible via l'interface web.

### Démarrer le Frontend

```bash
# Dans le dossier frontend
cd frontend
pnpm dev
# ou
npm run dev
```

Ouvrez votre navigateur à l'adresse [http://localhost:3000](http://localhost:3000)

## 💡 Exemples d'Utilisation

### Analyse de Sentiment
```
Utilisateur : "J'adore cette application, elle est géniale !"
MiniMind : Sentiment détecté : Positif
```

### Extraction de Mots-clés
```
Utilisateur : Analyse ce texte : "L'intelligence artificielle transforme notre société..."
MiniMind : Mots-clés principaux : intelligence, artificielle, transforme, société...
```

### Visualisation de Données
```
Utilisateur : Montre-moi un graphique en barres
MiniMind : [Affiche un graphique interactif basé sur tips.csv]
```

## 📚 Structure du Projet

```
MiniMind/
├── agent.py                    # Agent IA principal avec tous les outils
├── sentiment_analysis.py       # Module d'analyse de sentiment
├── data_visualization.py       # Module de visualisation
├── requirements.txt            # Dépendances Python
├── tips.csv                   # Dataset pour les visualisations
├── project.md                 # Documentation du défi
├── .env                       # Variables d'environnement (à créer)
└── frontend/                  # Application Next.js
    ├── app/
    │   ├── page.tsx          # Page principale
    │   ├── layout.tsx        # Layout de l'application
    │   └── api/
    │       └── copilotkit/
    │           └── route.ts  # Route API pour l'agent
    ├── package.json
    └── ...
```

## 🎓 Aspects Pédagogiques

Ce projet démontre plusieurs concepts clés de l'IA :

1. **Traitement du Langage Naturel (NLP)** : Comment l'IA comprend et analyse le texte
2. **Modèles de Langage** : Utilisation de Google Gemini pour la conversation
3. **Analyse de Sentiment** : Classification automatique des émotions
4. **Extraction d'Information** : Identification automatique d'entités et de mots-clés
5. **Visualisation de Données** : Présentation graphique des résultats

## 🏆 Défi AI4GOOD - Nuit de l'Info 2024

Ce projet a été développé pour le défi **MiniMind** organisé par **AI4GOOD** lors de la Nuit de l'Info 2024. L'objectif était de créer un prototype IA pédagogique permettant aux jeunes de découvrir l'intelligence artificielle de manière interactive.

### Critères du Défi
- ✅ Application accessible via navigateur
- ✅ Objectif pédagogique : montrer le fonctionnement de l'IA
- ✅ Interaction utilisateur intuitive
- ✅ Documentation du projet
- ✅ Démonstration interactive

## 👥 Équipe

Projet développé pendant la Nuit de l'Info 2024.

## 📄 Licence

Ce projet est open source et disponible pour un usage éducatif.

## 🔗 Liens Utiles

- [Documentation Strands Agents](https://strands.dev)
- [Google Gemini AI](https://ai.google.dev)
- [Next.js Documentation](https://nextjs.org/docs)
- [CopilotKit](https://copilotkit.ai)

---

**Fait avec ❤️ pour l'éducation et la démocratisation de l'IA**
