# Projet final : les résultats d'examens

**Lien du tableau de bord :** (à coller ici une fois en ligne)

**Équipe de 5. Rendu le vendredi 6 novembre à 23 h 59. Soutenances les samedi 7 et dimanche 8 novembre.**

Un réseau de 25 écoles (fictives) vous confie les résultats de ses candidats aux examens de fin d'études secondaires, en 2024 et 2025. Le fichier sort tel quel du secrétariat. Le directeur veut savoir quelles filières, quels secteurs et quelles communes réussissent, et lesquelles décrochent. Un candidat réussit avec une moyenne d'au moins 10 sur 20.

| Fichier | Une ligne par | Colonnes |
|---|---|---|
| `donnees/resultats_brut.csv` | candidat | `candidat`, `annee`, `code_ecole`, `filiere` (SES, SVT, SMP, LLA), `sexe`, `moyenne` (sur 20) |
| `donnees/ecoles.csv` | école | `code_ecole`, `ecole`, `commune`, `secteur` |
| `donnees/communes.csv` | commune | `commune`, `departement`, `population` |

## Ce qu'il faut rendre

1. **`exploration.ipynb`** : toute votre démarche, exécutée, avec ses sorties et ses graphiques : diagnostic, nettoyage, jointures (qui écrivent `donnees/resultats_propre.csv`), puis une partie par question. C'est le plan de l'exercice sur l'électricité. Des contrôles chiffrés vous disent si votre nettoyage est juste.
2. **`app.py`** : le tableau de bord Streamlit, **en ligne**, présenté au décideur. Il lit `donnees/resultats_propre.csv` et ne refait pas le nettoyage.
3. **`equipe.md`** : qui a fait quoi, et le lien du tableau de bord.
4. **Une soutenance**, les samedi 7 et dimanche 8 novembre, après le rendu : présentation de 5 minutes avec le tableau de bord en ligne, puis deux questions individuelles par étudiant.

### Les questions

1. Quelles filières réussissent le mieux ? L'écart entre filières est-il le même en 2024 et en 2025 ?
2. Le secteur de l'école (public, privé, congréganiste) fait-il une différence ? Montrez-le avec un graphique.
3. Quelles communes et quels départements décrochent ? Lesquels progressent ?
4. Filles et garçons réussissent-ils de la même façon, dans chaque filière ?
5. Un code d'école des résultats est absent de `ecoles.csv` : lequel, combien de candidats, et comment l'avez-vous traité ?

### Ce que doit contenir le tableau de bord

- Un titre, le contexte en deux phrases, la source des données.
- Au moins **3 indicateurs** (`st.metric`) en haut de page.
- Au moins **2 filtres** dans la barre latérale (`st.sidebar.selectbox`, `st.sidebar.multiselect`), qui changent les indicateurs et les graphiques.
- Une partie par question (par exemple un onglet avec `st.tabs`) : un graphique titré, ou un tableau, et une phrase qui dit ce qu'on en conclut.
- Une conclusion : ce qu'il faut retenir, et les limites des données.

## Démarrer

Une seule personne accepte le projet et crée l'équipe, les quatre autres la rejoignent. Puis chacun :

```bash
cd cours-python
gh repo clone esih-classroom/projet-data-examens-NOM-DE-L-EQUIPE
cd projet-data-examens-NOM-DE-L-EQUIPE
uv sync
code .
```

Le tableau de bord se lance sur votre machine avec `uv run streamlit run app.py`, puis s'ouvre sur `http://localhost:8501`.

## Le tableau de bord, en six étapes

Les mêmes que dans l'exercice sur l'électricité. Après chaque étape, l'application en ligne est mise à jour.

| Étape | Ce qu'on ajoute |
|---|---|
| 1 | L'`app.py` de départ, tel quel, mis **en ligne dès le premier jour** |
| 2 | Lire `donnees/resultats_propre.csv` avec `@st.cache_data` ; le contexte et la source |
| 3 | Au moins deux filtres dans la barre latérale |
| 4 | Au moins trois indicateurs (`st.columns`, `st.metric`) |
| 5 | `st.tabs` : un onglet par question, avec un graphique titré et une phrase chiffrée |
| 6 | La conclusion, les limites des données, et les données filtrées dans un `st.expander` |

## Mettre l'application en ligne

Streamlit Community Cloud est gratuit, mais il ne déploie que depuis un dépôt dont vous êtes **administrateur** : le dépôt Classmoji ne convient pas. Un seul membre de l'équipe en fait une copie publique sur son propre compte GitHub, une seule fois, depuis le dossier du dépôt :

```bash
gh repo create projet-data-examens --public --source . --remote perso --push
```

Puis, sur [share.streamlit.io](https://share.streamlit.io) :

1. **Continue with GitHub**, et acceptez l'accès à vos dépôts.
2. **Create app**, puis **Deploy a public app from GitHub**.
3. Repository : `VOTRE-COMPTE/projet-data-examens` ; Branch : `main` ; Main file path : `app.py`.
4. App URL : un nom court et lisible, par exemple `projet-data-examens-votre-nom`.
5. **Advanced settings** : Python **3.14**, la version de votre machine. Puis **Deploy**.

L'application lit `donnees/resultats_propre.csv` : ce fichier doit être commité, sinon elle plante en ligne.

À chaque modification, on pousse vers les deux dépôts :

```bash
git add .
git commit -m "Ajoute la courbe de consommation"
git push
git push perso main
```

L'application en ligne se met à jour seule en une minute environ. Collez son lien en haut de ce README.

Les autres membres poussent seulement vers le dépôt Classmoji (`git push`). Le membre qui a la copie publique fait `git pull`, puis `git push perso main`, pour mettre l'application à jour.

## Travailler à cinq

Proposition de répartition : un membre pour le diagnostic et le nettoyage, un pour les jointures et les indicateurs, deux pour les analyses et les graphiques, un pour le tableau de bord et sa mise en ligne. Chacun commite son propre travail avec son compte. Faites `git pull` avant de commencer et avant chaque `git push`. Avant la soutenance, chacun relit tout le projet : les questions individuelles portent sur l'ensemble.

Ne modifiez pas les fichiers de `donnees/` fournis.

## Notation

Le projet compte pour **70 %** de la note du cours (le TP1 pour 30 %). Il n'y a pas d'examen sur table.

| Élément | Part |
|---|---|
| Présence à la soutenance | 10 % |
| Le projet : la présentation, et un notebook et un tableau de bord qui fonctionnent | 40 % |
| Questions individuelles : deux questions par étudiant, sur **tout** le projet | 50 % |

Les questions individuelles portent sur n'importe quelle partie du projet, pas seulement sur la vôtre : chaque membre doit comprendre le nettoyage, les jointures, chaque graphique et le code de `app.py`.

## Si ça coince

| Problème | Solution |
|---|---|
| `streamlit: command not found` | Lancez-la avec uv : `uv run streamlit run app.py` |
| `FileNotFoundError: ..._propre.csv` | Exécutez d'abord tout le notebook : c'est lui qui écrit le fichier propre |
| L'application en ligne affiche « Error running app » | **Manage app**, en bas à droite, montre l'erreur : souvent un fichier non commité ou une version de Python différente |
| L'application en ligne ne change pas | Vous avez oublié `git push perso main` |
| `rejected ... fetch first` au `git push` | Quelqu'un a poussé avant vous : `git pull`, puis `git push` |
| `ModuleNotFoundError: No module named 'pandas'` dans le notebook | Mauvais noyau : **Select Kernel**, puis `.venv` |

Bloqué ? Écrivez un commentaire dans l'issue, avec le message d'erreur en entier.
