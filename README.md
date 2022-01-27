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
#### Installation des packages 
```
pip install -r requirements.txt
```
#### Valider le code avec flake8(https://flake8.pycqa.org/en/latest/) et flake8-html(https://pypi.org/project/flake8-html/)
```
#pour flake8 :
python -m pip install flake8
flake8 --max-line-length=119 chess_tournament
#pour flake8-html
pip install flake8-html
flake8 --format=html --htmldir=flake-report
```
#### Lancer le script
```
python -m chess_tournament
```
La base de données est enregistrées dans le dossier ***chess_tournament -> models -> database***.