import pandas as pd
import numpy as np


def charger_donnees(filepath):
    df = pd.read_csv(filepath)
    print(f"Données chargées : {df.shape}")
    return df

def supprimer_doublons(df):
    avant = len(df)
    df = df.drop_duplicates()
    print(f"Doublons supprimés : {avant - len(df)}")
    return df

def nettoyer_start_year(df):
    df['Start Year'] = df['Start Year'].astype(str).str.replace(r'[^0-9]', '', regex=True)
    df['Start Year'] = pd.to_numeric(df['Start Year'], errors='coerce')
    print(f"Start Year nettoyé (type : {df['Start Year'].dtype})")
    return df

def nettoyer_valeurs_manquantes(df):
    df = df.dropna(subset=['Region'])
    df['Event Name'] = df['Event Name'].fillna("Non nommé")
    df['Total Deaths'] = df['Total Deaths'].fillna(df['Total Deaths'].median())
    print("Valeurs manquantes traitées")
    return df

def corriger_aberrations(df):
    df = df[df['Total Deaths'] >= 0]
    df.loc[df['Magnitude'] > 10, 'Magnitude'] = None
    print("Aberrations corrigées")
    return df

def normaliser_categories(df):
    for col in ['Region', 'Disaster Type', 'Country']:
        df[col] = df[col].str.strip().str.title()
    country_mapping = {
        'United States Of America': 'United States',
        'Us': 'United States',
        'U.S.A.': 'United States',
        'Etats-Unis': 'United States',
    }
    df['Country'] = df['Country'].replace(country_mapping)
    print(f"Catégories normalisées ({df['Country'].nunique()} pays)")
    return df

def creer_features(df):
    df['Decennie'] = (df['Start Year'] // 10) * 10
    df['Has_Deaths'] = df['Total Deaths'] > 0
    print("Features créées : Decennie, Has_Deaths")
    return df

def exporter(df, filepath):
    df_export = df[['DisNo.', 'Region', 'Country', 'Has_Deaths', 'Decennie', 'Disaster Type', 'Total Deaths']]
    df_export = df_export.rename(columns={
        'Disaster Type': 'Type_Catastrophe',
        'DisNo.': 'ID_Catastrophe',
        'Total Deaths': 'Deces'
    })
    df_export.to_csv(filepath, index=False)
    print(f"Export terminé : {filepath}")


# ===========================
# PIPELINE PRINCIPAL
# ===========================

def pipeline(input_path, output_path):
    print("\n" + "="*50)
    print("PIPELINE DE NETTOYAGE")
    print("="*50 + "\n")

    df = charger_donnees(input_path)
    df = supprimer_doublons(df)
    df = nettoyer_start_year(df)
    df = nettoyer_valeurs_manquantes(df)
    df = corriger_aberrations(df)
    df = normaliser_categories(df)
    df = creer_features(df)
    exporter(df, output_path)

    print("\nPipeline OK")
    return df


if __name__ == "__main__":
    df = pipeline(
        input_path="../data/catnat_dirty.csv",
        output_path="../data/catnat_clean.csv"
    )