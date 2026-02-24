import pandas as pd
import numpy as np

df = pd.read_csv("../data/catnat_dirty.csv")

# ===========================
# EXERCICE 1
# ===========================
print("="*60)
print("EXERCICE 1")
print("="*60 + "\n")

# 1. Affichez les dimensions du dataset
print(f"Dimensions : {df.shape}")

# 2. Affichez les types de données avec info()
print(f"\n Infos :")
df.info()

# 3. Comptez les valeurs manquantes par colonne (nombre et pourcentage)
print(f"\n Vaeurs manquantes par colonne :")
print(df.isnull().sum())
print("\n En pourcentage % :")
print((df.isnull().sum() / len(df) * 100).apply(lambda x: f"{x:.1f}%"))

# 4. Comptez le nombre de doublons
print(f"\n Nombre de doublons : {df.duplicated().sum()}")

# 5. Affichez les valeurs uniques de Region — repérez les incohérences
print(f"\n Valeurs uniques de 'Region' :\n {df['Region'].value_counts()}")

# 6. Affichez les statistiques de Total Deaths — repérez les anomalies
print(f"\n Statistiques de 'Total Deaths' :\n {df['Total Deaths'].describe()}")

# Questions
print("\n Questions :")
print(f"\nIl y a {df.duplicated().sum()} doublons.")
print(f"\nLes 5 colonnes qui ont le plus de valeurs manquantes sont : {df.isnull().sum().sort_values(ascending=False).head(5)}")
asia_variants = df['Region'][df['Region'].str.lower() == 'asia']
print(f"\nLes différentes variantes pour 'Asia' :\n {asia_variants.value_counts()}")
print(f"\nIl y a {(df['Total Deaths'] < 0).sum()} valeur(s) négative(s) pour 'Total Deaths'.")


# ===========================
# EXERCICE 2
# ===========================
print("\n")
print("="*60)
print("EXERCICE 2")
print("="*60 + "\n")

# 1. Affichez quelques lignes dupliquées pour vérifier
print(df[df.duplicated(keep=False)])

# 2. Supprimez les doublons exacts
df = df.drop_duplicates()

# 3. Vérifiez que les doublons ont bien été supprimés
print(df[df.duplicated(keep=False)])


# ===========================
# EXERCICE 3
# ===========================
print("\n")
print("="*60)
print("EXERCICE 3")
print("="*60 + "\n")

# 1. Vérifiez le type de Start Year
print(f"Le type de 'Start Year' est : {df['Start Year'].dtypes}")

# 2. Affichez quelques valeurs problématiques (contenant "Year" ou "AD")
mask = df['Start Year'].astype(str).str.contains('Year|AD', na=False)
print(df[mask]['Start Year'].value_counts())

# 3. Nettoyez la colonne : supprimez le texte et convertissez en numérique
df['Start Year'] = df['Start Year'].astype(str).str.replace(r'[^0-9]', '', regex=True)
df['Start Year'] = pd.to_numeric(df['Start Year'], errors='coerce')

# 4. Vérifiez le résultat
print(f"\nLe nouveau type de 'Start Year' est : {df['Start Year'].dtypes}")


# ===========================
# EXERCICE 4
# ===========================
print("\n")
print("="*60)
print("EXERCICE 4")
print("="*60 + "\n")

# 1. Pour Region (peu de nulls) : supprimez les lignes avec null
df = df.dropna(subset=['Region'])

# 2. Pour Event Name : remplacez les nulls par "Non nommé"
df['Event Name'] = df['Event Name'].fillna("Non nommé")

# 3. Pour Total Deaths : décidez d'une stratégie et appliquez-la
df['Total Deaths'] = df['Total Deaths'].fillna(df['Total Deaths'].median())

# 5. Vérifiez le résultat
print(df[['Region', 'Event Name', 'Total Deaths', 'Magnitude']].isnull().sum())


# ===========================
# EXERCICE 5
# ===========================
print("\n")
print("="*60)
print("EXERCICE 5")
print("="*60 + "\n")

# 1. Identifiez les valeurs négatives dans Total Deaths
print("Valeurs négatives :")
print(df[df['Total Deaths'] < 0])

# 2. Identifiez les valeurs aberrantes dans Magnitude (> 10)
print("\nValeurs aberrantes >10 :")
print(df[df['Magnitude'] > 10])

# 3. Décidez : supprimer ou corriger ?
print("On supprime les valeurs négatives de 'Total Deaths'.")
print("\nOn met NaN pour Magnitude.")

# 4. Appliquez le traitement
df = df[df['Total Deaths'] >= 0]
df.loc[df['Magnitude'] > 10, 'Magnitude'] = None

# 5. Vérifiez le résultat
print(df['Total Deaths'].min())
print(df['Magnitude'].max())


# ===========================
# EXERCICE 6
# ===========================
print("\n")
print("="*60)
print("EXERCICE 6")
print("="*60 + "\n")

# 1. Nettoyez Region : strip + title case
df['Region'] = df['Region'].str.strip().str.title()

# 2. Vérifiez avec value_counts() — combien de catégories maintenant ?
print(df['Region'].value_counts())
print("\nOn a bien une catégorie par continent.")

# 3. Nettoyez Disaster Type de la même manière
df['Disaster Type'] = df['Disaster Type'].str.strip().str.title()

# 4. Nettoyez Country : strip + title case
df['Country'] = df['Country'].str.strip().str.title()

# 5. Corrigez les variantes de pays (USA → United States, etc.)
#pd.set_option('display.max_rows', None)
#print(df['Country'].value_counts())

country_mapping = {
    'United States Of America': 'United States',
    'Us': 'United States',
    'U.S.A.': 'United States',
    'Etats-Unis': 'United States',
}
df['Country'] = df['Country'].replace(country_mapping)
print(f"\nNombre de pays : {df['Country'].nunique()}")
print(df['Country'].value_counts().head(10))


# ===========================
# EXERCICE 7
# ===========================
print("\n")
print("="*60)
print("EXERCICE 7")
print("="*60 + "\n")

# 1. Créez une colonne Decennie à partir de Start Year
df['Decennie'] = (df['Start Year'] // 10) * 10

# 2. Créez une colonne Has_Deaths (booléen : True si Total Deaths > 0)
df['Has_Deaths'] = df['Total Deaths'] > 0

# 3. Vérifiez vos nouvelles colonnes
print(df[['Decennie', 'Has_Deaths']].head(10))


# ===========================
# EXERCICE 8
# ===========================
print("\n")
print("="*60)
print("EXERCICE 8")
print("="*60 + "\n")

# 1. Sélectionnez les colonnes utiles pour l'analyse
df_export = df[['DisNo.', 'Region', 'Country', 'Has_Deaths', 'Decennie', 'Disaster Type', 'Total Deaths']]

# 2. Renommez les colonnes si nécessaire (noms clairs, sans espaces)
df_export = df_export.rename(columns={'Disaster Type': 'Type_Catastrophe'})
df_export = df_export.rename(columns={'DisNo.': 'ID_Catastrophe'})
df_export = df_export.rename(columns={'Total Deaths': 'Deces'})

# 3. Faites une vérification finale avec info() et head()
df_export.info()

# 4. Exportez en CSV : catnat_clean.csv
df_export.to_csv("../data/catnat_clean.csv", index=False)