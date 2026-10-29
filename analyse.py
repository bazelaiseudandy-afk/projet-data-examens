"""Projet final : les résultats d'examens.

Remplacez chaque pass par votre code. Vérifiez avec : uv run test_projet.py
Vous pouvez ajouter vos propres fonctions pour le rapport.
"""


import pandas as pd


SEUIL = 10


def diagnostic(brut):
    """Renvoie un dictionnaire : lignes, manquants (total des valeurs manquantes), doublons (lignes en double)."""
    pass


def nettoyer(brut):
    """Renvoie un tableau sans doublons ni moyenne manquante, moyenne en float, filières et codes d'école écrits d'une seule façon."""
    pass


def enrichir(propre, ecoles, communes):
    """Renvoie les résultats avec école, commune, secteur, département et population, sans perdre aucun candidat."""
    pass


def taux_par_filiere(propre):
    """Renvoie le taux de réussite (moyenne >= 10) en % de chaque filière, arrondi à 1 décimale, du plus haut au plus bas."""
    pass


def moyenne_secteur_annee(propre, ecoles, communes):
    """Renvoie le tableau secteur (lignes) × année (colonnes) des moyennes, arrondies à 2 décimales."""
    pass


def communes_en_difficulte(propre, ecoles, communes, seuil):
    """Renvoie la liste triée des communes dont le taux de réussite (en %) est sous le seuil."""
    pass


def evolution_par_departement(propre, ecoles, communes):
    """Renvoie, par département, le taux de réussite en % en 2024 et 2025 (arrondis à 1) et la colonne ecart = 2025 - 2024, trié par ecart décroissant."""
    pass
