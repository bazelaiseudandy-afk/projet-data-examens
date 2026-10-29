"""Vérifie le projet : uv run test_projet.py. Ne pas modifier : la note est calculée avec ce fichier d'origine."""

from pathlib import Path

import pandas as pd

import inspect

import analyse

DOSSIER = Path(__file__).parent / "donnees"

def forme(objet):
    if isinstance(objet, pd.DataFrame):
        valeurs = objet.round(2).astype(object).where(objet.notna(), None).values.tolist()
        return {"index": [str(i) for i in objet.index], "colonnes": [str(c) for c in objet.columns], "valeurs": valeurs}
    if isinstance(objet, pd.Series):
        valeurs = objet.round(2).astype(object).where(objet.notna(), None).tolist()
        return {"index": [str(i) for i in objet.index], "valeurs": valeurs}
    if isinstance(objet, float):
        return round(objet, 2)
    if isinstance(objet, list):
        return [str(v) for v in objet]
    return objet


def resume_nettoyage(propre):
    texte = [c for c in propre.columns if not pd.api.types.is_numeric_dtype(propre[c])]
    nombres = [c for c in propre.columns if pd.api.types.is_numeric_dtype(propre[c])]
    return {
        "forme": list(propre.shape),
        "manquants": int(propre.isna().sum().sum()),
        "doublons": int(propre.duplicated().sum()),
        "nombres": {c: round(float(propre[c].sum()), 1) for c in nombres},
        "textes": {c: sorted(propre[c].unique().tolist()) for c in texte if propre[c].nunique() <= 30},
    }


def resume_jointure(complet):
    return {"lignes": len(complet), "colonnes": sorted(str(c) for c in complet.columns), "manquants": int(complet.isna().sum().sum())}


def lire(nom):
    return pd.read_csv(DOSSIER / f"{nom}.csv")


def contexte():
    return {"brut": lire("resultats_brut"), "propre": lire("resultats_brut".replace("brut", "propre")), "ecoles": lire("ecoles"), "communes": lire("communes")}


ATTENDU = {'diagnostic': {'lignes': 1529, 'manquants': 18, 'doublons': 25}, 'nettoyer': {'forme': [1486, 6], 'manquants': 0, 'doublons': 0, 'nombres': {'annee': 3008403.0, 'moyenne': 14756.4}, 'textes': {'code_ecole': ['E01', 'E02', 'E03', 'E04', 'E05', 'E06', 'E07', 'E08', 'E09', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'E23', 'E24', 'E25'], 'filiere': ['LLA', 'SES', 'SMP', 'SVT'], 'sexe': ['F', 'M']}}, 'enrichir': {'lignes': 1486, 'colonnes': ['annee', 'candidat', 'code_ecole', 'commune', 'departement', 'ecole', 'filiere', 'moyenne', 'population', 'secteur', 'sexe'], 'manquants': 135}, 'taux_par_filiere': {'index': ['SMP', 'SVT', 'SES', 'LLA'], 'valeurs': [62.7, 50.4, 46.3, 42.1]}, 'moyenne_secteur_annee': {'index': ['Congréganiste', 'Privé', 'Public'], 'colonnes': ['2024', '2025'], 'valeurs': [[11.49, 11.07], [10.2, 10.13], [9.42, 9.02]]}, 'communes_en_difficulte': ['Carrefour', 'Hinche', 'Jérémie', 'Les Cayes'], 'evolution_par_departement': {'index': ['Nord-Ouest', 'Artibonite', 'Sud-Est', 'Centre', 'Nord', 'Ouest', 'Sud', "Grand'Anse"], 'colonnes': ['2024', '2025', 'ecart'], 'valeurs': [[38.6, 54.5, 15.9], [44.4, 48.8, 4.4], [58.9, 62.5, 3.6], [26.2, 25.9, -0.3], [57.6, 52.4, -5.2], [60.1, 51.2, -8.9], [42.2, 33.3, -8.9], [35.3, 23.8, -11.5]]}}

MESSAGES = {'diagnostic': "diagnostic : résultat différent de l'attendu. Relisez la consigne : Renvoie un dictionnaire : lignes, manquants (total des valeurs manquantes), doublons (lignes en double).", 'nettoyer': "nettoyer : résultat différent de l'attendu. Relisez la consigne : Renvoie un tableau sans doublons ni moyenne manquante, moyenne en float, filières et codes d'école écrits d'une seule façon.", 'enrichir': "enrichir : résultat différent de l'attendu. Relisez la consigne : Renvoie les résultats avec école, commune, secteur, département et population, sans perdre aucun candidat.", 'taux_par_filiere': "taux_par_filiere : résultat différent de l'attendu. Relisez la consigne : Renvoie le taux de réussite (moyenne >= 10) en % de chaque filière, arrondi à 1 décimale, du plus haut au plus bas.", 'moyenne_secteur_annee': "moyenne_secteur_annee : résultat différent de l'attendu. Relisez la consigne : Renvoie le tableau secteur (lignes) × année (colonnes) des moyennes, arrondies à 2 décimales.", 'communes_en_difficulte': "communes_en_difficulte : résultat différent de l'attendu. Relisez la consigne : Renvoie la liste triée des communes dont le taux de réussite (en %) est sous le seuil.", 'evolution_par_departement': "evolution_par_departement : résultat différent de l'attendu. Relisez la consigne : Renvoie, par département, le taux de réussite en % en 2024 et 2025 (arrondis à 1) et la colonne ecart = 2025 - 2024, trié par ecart décroissant."}


def verifier(nom, appel):
    try:
        resultat = appel(contexte())
        assert resultat is not None, "la fonction renvoie None : il reste pass, ou il manque return"
        if nom == "nettoyer":
            assert "read_csv" not in inspect.getsource(analyse.nettoyer), "nettoyer doit partir du tableau brut reçu, sans lire de fichier"
            obtenu = resume_nettoyage(resultat)
        elif nom == "enrichir":
            obtenu = resume_jointure(resultat)
        else:
            obtenu = forme(resultat)
        assert obtenu == ATTENDU[nom], MESSAGES[nom]
        print(f"  ✔ {nom}")
        return 1
    except Exception as erreur:
        print(f"  ✘ {nom} : {str(erreur) or type(erreur).__name__}")
        return 0


def main():
    total = 0
    total += verifier("diagnostic", lambda c: analyse.diagnostic(c["brut"]))
    total += verifier("nettoyer", lambda c: analyse.nettoyer(c["brut"]))
    total += verifier("enrichir", lambda c: analyse.enrichir(c["propre"], c["ecoles"], c["communes"]))
    total += verifier("taux_par_filiere", lambda c: analyse.taux_par_filiere(c["propre"]))
    total += verifier("moyenne_secteur_annee", lambda c: analyse.moyenne_secteur_annee(c["propre"], c["ecoles"], c["communes"]))
    total += verifier("communes_en_difficulte", lambda c: analyse.communes_en_difficulte(c["propre"], c["ecoles"], c["communes"], 40))
    total += verifier("evolution_par_departement", lambda c: analyse.evolution_par_departement(c["propre"], c["ecoles"], c["communes"]))
    print(f"\nTests : {total} / 7")


if __name__ == "__main__":
    main()
