from pathlib import Path

import pandas as pd
import streamlit as st

DOSSIER = Path(__file__).parent / "donnees"

st.set_page_config(page_title="Les résultats d'examens", page_icon="🎓", layout="wide")

st.title("Les résultats d'examens")
st.caption("Projet final, Python pour l'analyse de données, ESIH 2026. Données fictives.")

brut = pd.read_csv(DOSSIER / "resultats_brut.csv")
st.write(f"Le fichier brut compte {len(brut)} lignes.")
st.dataframe(brut.head(10), hide_index=True)
print("Forme :", brut.shape)
print("\nTypes des colonnes :")
print(brut.dtypes)
print("\nValeurs manquantes par colonne :")
print(brut.isna().sum())
print("\nLignes en double :", brut.duplicated().sum())

print("\nÉcritures différentes dans les colonnes de texte :")
for colonne in ["code_ecole", "filiere", "sexe"]:
    print(f"- {colonne} : {brut[colonne].nunique()} écritures")

print("Filières :", sorted(brut["filiere"].unique()))
print("Sexes :", sorted(brut["sexe"].unique()))

# Moyennes qui ne sont pas des nombres (ex. "11,6" ou "11.2/20")
converti = pd.to_numeric(brut["moyenne"], errors="coerce")
non_convertibles = brut.loc[converti.isna() & brut["moyenne"].notna(), "moyenne"]
print("\nMoyennes non numériques :", non_convertibles.nunique())
print(non_convertibles.drop_duplicates().head(15).tolist())

propre = brut.copy()

# a) Textes : enlever les espaces, tout mettre en majuscules
for colonne in ["code_ecole", "filiere", "sexe"]:
    propre[colonne] = propre[colonne].astype(str).str.strip().str.upper()

# b) Moyenne : retirer "/20", virgule -> point, convertir en nombre
propre["moyenne"] = (
    propre["moyenne"].astype(str)
    .str.replace("/20", "", regex=False)
    .str.replace(",", ".", regex=False)
    .str.strip()
)
propre["moyenne"] = pd.to_numeric(propre["moyenne"], errors="coerce")

# c) Doublons
avant = len(propre)
propre = propre.drop_duplicates()
print(f"Doublons supprimés : {avant - len(propre)}")          # 25

# d) Lignes sans moyenne
avant = len(propre)
propre = propre.dropna(subset=["moyenne"]).reset_index(drop=True)
print(f"Lignes sans moyenne supprimées : {avant - len(propre)}")  # 18

# Contrôle : (1486, 6), 0 manquant, 0 doublon, 4 filières, 2 sexes
print(propre.shape, int(propre.isna().sum().sum()), int(propre.duplicated().sum()))
print(propre["filiere"].nunique(), propre["sexe"].nunique())

ecoles = pd.read_csv(DOSSIER / "ecoles.csv")
communes = pd.read_csv(DOSSIER / "communes.csv")

print("Avant jointures :", len(propre))

# how="left" : on garde tous les candidats, même sans école connue
complet = propre.merge(ecoles, on="code_ecole", how="left")
print("Après jointure ecoles :", len(complet))
print("Codes sans école :", complet["ecole"].isna().sum())      # 27

complet = complet.merge(communes, on="commune", how="left")
print("Après jointure communes :", len(complet))                # 1486

# Colonne calculée : réussite si moyenne >= 10
complet["reussite"] = (complet["moyenne"] >= 10).astype(int)

# Le code absent (E25) : on garde les candidats, marqués "Inconnu"
complet[["commune", "secteur", "departement"]] = complet[
    ["commune", "secteur", "departement"]
].fillna("Inconnu")
complet["ecole"] = complet["ecole"].fillna("E25 (absente de ecoles.csv)")

# Contrôle : autant de lignes qu'avant les jointures
assert len(complet) == len(propre) == 1486

# Question 5 : quel code est absent ?
print(sorted(set(complet["code_ecole"]) - set(ecoles["code_ecole"])))  # ['E25']

# Enregistrement du fichier lu par app.py
complet.to_csv(DOSSIER / "resultats_propre.csv", index=False)
