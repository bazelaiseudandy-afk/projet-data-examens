# Projet final : les résultats d'examens

**Équipe de 5. Lancé le jeudi 29 octobre, à rendre le vendredi 6 novembre à 23 h 59.**

Un réseau de 25 écoles (fictives) vous confie les résultats de ses candidats aux examens de fin d'études secondaires, en 2024 et 2025. Le fichier sort tel quel du secrétariat. Le directeur veut savoir quelles filières, quels secteurs et quelles communes réussissent, et lesquelles décrochent. Un candidat réussit avec une moyenne d'au moins 10 sur 20.

| Fichier | Une ligne par | Colonnes |
|---|---|---|
| `donnees/resultats_brut.csv` | candidat | `candidat`, `annee`, `code_ecole`, `filiere` (SES, SVT, SMP, LLA), `sexe`, `moyenne` (sur 20) |
| `donnees/ecoles.csv` | école | `code_ecole`, `ecole`, `commune`, `secteur` |
| `donnees/communes.csv` | commune | `commune`, `departement`, `population` |

## Démarrer

Une seule personne accepte le projet et crée l'équipe, les quatre autres la rejoignent. Puis chacun :

```bash
cd cours-python
gh repo clone esih-classroom/projet-data-examens-NOM-DE-L-EQUIPE
cd projet-data-examens-NOM-DE-L-EQUIPE
uv sync
code .
```

## Ce qu'il faut rendre

Le fichier `donnees/resultats_propre.csv` est le résultat attendu de `nettoyer` : il permet de commencer les analyses pendant qu'un membre de l'équipe écrit le nettoyage. `nettoyer` doit le reproduire à partir du fichier brut, sans le lire.

1. **`analyse.py`** : les 7 fonctions demandées, vérifiées par `uv run test_projet.py`. Leur consigne exacte est dans leur docstring. Ajoutez les vôtres pour le rapport.
2. **`rapport.ipynb`** : le rapport rédigé, qui répond aux questions ci-dessous avec des tableaux, des graphiques titrés et des phrases. Exécuté du début à la fin avant le dernier push.
3. **`equipe.md`** : qui a fait quoi.
4. **Une présentation de 5 minutes**, 5 diapositives au plus, le jour fixé par l'enseignant.

### Les fonctions testées

| Fonction | Ce qu'elle renvoie |
|---|---|
| `diagnostic(brut)` | Renvoie un dictionnaire : lignes, manquants (total des valeurs manquantes), doublons (lignes en double). |
| `nettoyer(brut)` | Renvoie un tableau sans doublons ni moyenne manquante, moyenne en float, filières et codes d'école écrits d'une seule façon. |
| `enrichir(propre, ecoles, communes)` | Renvoie les résultats avec école, commune, secteur, département et population, sans perdre aucun candidat. |
| `taux_par_filiere(propre)` | Renvoie le taux de réussite (moyenne >= 10) en % de chaque filière, arrondi à 1 décimale, du plus haut au plus bas. |
| `moyenne_secteur_annee(propre, ecoles, communes)` | Renvoie le tableau secteur (lignes) × année (colonnes) des moyennes, arrondies à 2 décimales. |
| `communes_en_difficulte(propre, ecoles, communes, seuil)` | Renvoie la liste triée des communes dont le taux de réussite (en %) est sous le seuil. |
| `evolution_par_departement(propre, ecoles, communes)` | Renvoie, par département, le taux de réussite en % en 2024 et 2025 (arrondis à 1) et la colonne ecart = 2025 - 2024, trié par ecart décroissant. |

### Les questions du rapport

1. Quelles filières réussissent le mieux ? L'écart entre filières est-il le même en 2024 et en 2025 ?
2. Le secteur de l'école (public, privé, congréganiste) fait-il une différence ? Montrez-le avec un graphique.
3. Quelles communes et quels départements décrochent ? Lesquels progressent ?
4. Filles et garçons réussissent-ils de la même façon, dans chaque filière ?
5. Un code d'école des résultats est absent de `ecoles.csv` : lequel, combien de candidats, et comment l'avez-vous traité ?

## Travailler à cinq

Proposition de répartition : un membre pour le diagnostic et `nettoyer`, un pour `enrichir` et les jointures, deux pour les analyses et les graphiques, un pour le rapport et la présentation. Chacun commite son propre travail avec son compte, et tout le monde relit le rapport. Faites `git pull` avant de commencer et avant chaque `git push`.

Ne modifiez pas `test_projet.py` ni les fichiers de `donnees/`.

## Barème proposé (sur 20)

| Élément | Points |
|---|---|
| Tests automatiques (`uv run test_projet.py`), au prorata | 6 |
| Rapport : réponses justes, graphiques lisibles (titre, axes, unités), conclusions prudentes | 8 |
| Présentation de 5 minutes | 4 |
| Commits : chaque membre commite son travail, avec des messages clairs | 2 |

## Si ça coince

| Problème | Solution |
|---|---|
| `rejected ... fetch first` au `git push` | Un coéquipier a poussé avant vous : `git pull`, puis `git push` |
| Un test dit « la fonction renvoie None » | Il reste `pass`, ou il manque `return` |
| Moins ou plus de lignes après un `merge` | Clés écrites différemment, ou clé en double à droite : comptez avant et après |
| `ModuleNotFoundError: No module named 'pandas'` | Mauvais noyau : **Select Kernel**, puis `.venv` |

Bloqué ? Écrivez un commentaire dans l'issue, avec le message d'erreur en entier.
