# TP-2 Visualisation de données massives

Nettoyage et préparation du dataset `catnat_dirty.csv` pour une analyse de détection d'anomalies.

## Lancer le script

```bash
python main.py
```

## Ce que fait le script

1. Supprime les doublons
2. Nettoie la colonne `Start Year`
3. Traite les valeurs manquantes
4. Supprime les valeurs aberrantes
5. Normalise les catégories (Region, Country, Disaster Type)
6. Crée les features `Decennie` et `Has_Deaths`
7. Exporte le résultat dans `catnat_clean.csv`

## Données

| Fichier | Description |
|---|---|
| `catnat_dirty.csv` | Dataset brut |
| `catnat_clean.csv` | Dataset nettoyé |

## Dépendances

```bash
pip install pandas numpy ydata-profiling
```

## Réponses exercice 9

1. Ouvrez Tableau Public
2. Connectez-vous au fichier catnat_clean.csv
3. Vérifiez dans l'écran "Source de données" :
- - Les types sont-ils corrects ? (# pour nombres, Abc pour texte)

Les types sont corrects.

- - Les nombres sont-ils bien reconnus ?

Les nombres sont bien reconnus.

4. Créez un bar chart : Type_Catastrophe vs COUNT(ID_Catastrophe)
- Les catégories sont-elles propres ? (pas de doublons)

Aucun doublon, tout est propre.

5. Créez un bar chart : Region vs SUM(Deces)
- Les 5 régions sont-elles bien distinctes ?

Les régions sont bien distinctes.

6. Créez une carte avec Country
- Les pays sont-ils reconnus ?

Les pays sont bien reconnus et les inconnus sont filtrés.

## Pour les curieux

- Script automatisé
```bash
python pipeline.py
```

- Utilisation de `pandas-profiling` avec génération d'un `rapport.html`