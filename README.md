# Projet 06 — Équilibre macroéconomique islamique IIS–ILM

Application académique développée en Python avec Flask pour calculer et représenter graphiquement l’équilibre du modèle IIS–ILM présenté dans le mémoire.

## Objectif

L’application détermine le point d’intersection entre :

- Le marché des biens, représenté par la courbe IIS.
- Le marché monétaire, représenté par la courbe ILM.

Elle affiche le revenu d’équilibre R* et le taux de profit attendu rp*.

## Paramètres

L’utilisateur peut renseigner dix paramètres :

| Paramètre | Désignation dans l’application |
|---|---|
| `alpha` | Paramètre de consommation |
| `psi` | Paramètre d’investissement |
| `I0` | Investissement autonome |
| `C0` | Consommation autonome |
| `Z` | Montant de la zakat |
| `D` | Dépenses volontaires |
| `beta` | Paramètre lié aux transactions |
| `d` | Paramètre lié au rendement |
| `phi0` | Demande minimale |
| `M_OF` | Offre monétaire |

## Fonctionnement

La fonction `calculate_iis_ilm_equilibrium` calcule les pentes et les constantes des deux courbes, puis résout leur intersection.

L’interface affiche :

- Le revenu d’équilibre R*.
- Le taux de profit attendu rp*.
- Les deux courbes et leur point d’intersection.

Les résultats numériques sont arrondis à deux décimales. Le graphique est produit avec Chart.js.

## Fichiers

- `app.py` : serveur Flask et traitement des paramètres saisis.
- `models.py` : calcul mathématique de l’équilibre.
- `templates/index.html` : formulaire, résultats et graphique.
- `requirements.txt` : dépendance Python.

## Installation

Depuis le dossier du projet :

```bash
python -m pip install -r requirements.txt
```

## Lancement local

```bash
python app.py
```

Ouvrir ensuite :

http://127.0.0.1:5001

La présentation utilise Bootstrap et le graphique utilise Chart.js, chargés depuis des CDN. Une connexion Internet est donc nécessaire pour charger ces ressources.

## Conditions de calcul et portée

Le calcul d’une intersection unique nécessite des valeurs non nulles de `psi` et de `d`, ainsi que des pentes distinctes pour les deux courbes.

Les paramètres préremplis servent à illustrer le fonctionnement. Le calcul d’une intersection ne garantit pas, à lui seul, que les valeurs obtenues soient économiquement admissibles.

Le projet constitue une simulation académique fondée sur les équations retenues dans le mémoire. Le serveur est configuré pour un usage local en mode développement.
