import datetime

PLAYERS_PER_TOURNAMENT = 8
NUMBER_OF_ROUND = 4
PROGRAM_NAME = 'chess_tournament'
# comment tu fais pour ajouter le player1 au tournament1?
# print la liste de joueurs du tournament
# ajoute un round au tournoi
# print la liste de rounds du tournament
# créer un match entre 2 players et l'ajouter au round

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    def set_winner(self, winner):
        self.winner = winner
        if winner == 1:
            self.player1.update_score(1)
        elif winner == 2:
            self.player2.update_score(1)
        else:
            self.player1.update_score(0.5)
            self.player2.update_score(0.5)

class Round:
    def __init__(self, name):
        self.start_date = datetime.datetime.now()
        self.name = name
        self.matches = []

    def create_first_round(self):
        list_a = [1, 2, 3, 4]
        list_b = [5, 6, 7, 8]
        list(zip(list_a, list_b))
        first_round = list
        self.matches.append(first_round)

class Players:
    """initialize a list of players"""
    def __init__(self):
        self.players_list = []

    def add_player(self, id_player, last_name, first_name, date_of_birth, gender):
        a_player = Player(id_player, last_name, first_name, date_of_birth, gender)
        self.players_list.append(a_player)

    def __repr__(self):
        return str(self)

class Player:
    """Player with is attributes id_player, last_name, first_name,
    date_of_birth, gender"""
    def __init__(self, id_player, last_name, first_name, date_of_birth, gender):
        self.id_player = id_player
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = None

    def __repr__(self):
        return f" {self.id_player} {self.last_name} {self.first_name} " \
               f"{self.date_of_birth} {self.gender} {self.ranking}"

class Tournaments:
    """initialize a list of tournaments"""
    def __init__(self):
        self.tournaments_list = []

    def add_tournament(self, tournament_name, location, creation_date,
                       timer, description):
        a_tournament = Tournament(tournament_name, location, creation_date,
                                  timer, description)
        self.tournaments_list.append(a_tournament)

    def __repr__(self):
        return f"{self.tournaments_list}"

class Tournament:
    """Tournament with is attributes tournament_name, location,
    creation_date, number_of_rounds, timer, description"""
    def __init__(self, tournament_name, location, creation_date,
                 timer, description):
        self.tournament_name = tournament_name
        self.location = location
        self.creation_date = creation_date
        self.number_of_rounds = NUMBER_OF_ROUND
        self.timer = timer
        self.description = description
        self.tournament_player = []
        self.tournament_rounds = []

    def start_first_round(self):
        first_round = Round(name="Round1")
        self.tournament_rounds.append(first_round)

    def add_tournament_player(self):
        player = Player(id_player=None, last_name=None, first_name=None,
                        date_of_birth=None, gender=None)
        self.tournament_player.append(player)

    def __repr__(self):
        return f"{self.tournament_name} {self.location}"


tournoi = Tournament(tournament_name='le tournoi', location='Paris',
                     creation_date='12.10.2021', timer='bullet',
                     description='le grand tournoi des débutants en python')
a = Tournaments()
a.add_tournament(tournament_name='test', location='lyon',
                 creation_date='10.10.2000', timer='blitz',
                 description="j'espère que ça va fonctionner")
player_one = Player(id_player=1, first_name='Breton', last_name='Pedro',
                 date_of_birth='18.10.1900', gender='M')

print(player_one)
print(tournoi)
print(a)