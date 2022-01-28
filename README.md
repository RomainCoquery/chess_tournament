***Note : ce projet est réalisé pendant ma formation [OpenClassrooms](https://openclassrooms.com/fr/).***

# chess_tournament
### Cette application permet de gérer les tournois d'échec sous les règles du tournoi suisse.
### Compatible avec Python3 sur tout OS.
### Installation
#### Dézippez le code, créez un environnement virtuel et activez-le :
```
python -m venv .venv
source .venv/bin/activate
```
#### Installation des packages :
```
pip install -r requirements.txt
```
#### Valider le code avec flake8(https://flake8.pycqa.org/en/latest/) et flake8-html(https://pypi.org/project/flake8-html/):
```
#pour flake8 :
python -m pip install flake8
flake8 chess_tournament
#pour flake8-html
pip install flake8-html
flake8 --format=html --htmldir=flake-report
```
#### Lancer le script
```
python -m chess_tournament
```
#### Plan de l'application
##### Page d'accueil:
```
--------------------------------------------------------------
[          Welcome to Chess Tournament                       ]
--------------------------------------------------------------
1. List Players
2. New Player
3. List Tournaments
4. New Tournament

Q. Exit
Choice:
```
***De cette page vous pouvez avec le choix 2 Créer un nouveau joueur directement,
avec le choix 4 et si vous avez enregistré minimum 8 joueurs avant, vous pouvez 
créer un nouveau tournoi***
##### 1 Liste des joueurs:
```
--------------------------------------------------------------
[                   List players                             ]
--------------------------------------------------------------
        Id      Full_name       Birthday        Gender  Rank
        
1. View Player
2. New Player
3. Edit Player
4. Sort players by last_name
5. Sort players by rank
H. Homepage
Q. Exit
```
***Dans cette page, vos joueurs apparaissent, vous pouvez les voir en détail avec le choix 1,
créer un nouveau joueur choix 2, modifier un joueur choix 3, trier choix 4 par nom et 5 par classement,
H pour revenir à la page principale, Q pour quitter l'application***
##### 3 Liste des tournois:
```
--------------------------------------------------------------
[              List Tournaments                              ]
--------------------------------------------------------------
        Name    Location        Creation_date   Timer   Description
        
1. Detail Tournament
2. New Tournament
H. Homepage
Q. Exit

```
Dans cette page, vos tournois apparaissent, vous pouvez les voir en détail et les reprendre
s'ils ne sont pas terminés avec le choix 1,créer un nouveau tournoi choix 2,
H pour revenir à la page principale, Q pour quitter l'application
#### Où se trouve la base de données ?
Elle est enregistrée dans le dossier chess_tournament -> models -> database: db.json.
