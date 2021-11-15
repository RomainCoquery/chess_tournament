import datetime
from copy import deepcopy

PLAYERS_PER_TOURNAMENT = 8
NUMBER_OF_ROUND = 4
PROGRAM_NAME = 'chess_tournament'


# ajoute un round au tournoi
# print la liste de rounds du tournament # Fait
# créer un match entre 2 players et l'ajouter au round

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    def set_winner(self, winner):
        """Define winner from the match"""
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
        self.name = name
        self.start_date = datetime.datetime.now()
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def __repr__(self):
        return f"{self.name} {self.start_date} {self.matches}"

class Player:
    """Player with is attributes id_player, last_name, first_name,
    birthday, gender, rank"""
    def __init__(self, id_, last_name, first_name, birthday, gender, rank):
        self.id_ = id_ or int()
        self.last_name = last_name or str()
        self.first_name = first_name or str()
        self.birthday = birthday or str()
        self.gender = gender or str()
        self.rank = rank or int()
        self.history = []

    def full_name(self):
        """define the full name of player"""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f" {self.id_} {self.last_name} {self.first_name} " \
               f"{self.birthday} {self.gender} {self.rank}"

class Tournament:
    """Tournament with is attributes tournament_name, location,
    creation_date, number_of_rounds, timer, description"""
    def __init__(self, tournament_name, location, creation_date,
                 timer, description):
        self.tournament_name = tournament_name or str()
        self.location = location or str()
        self.creation_date = creation_date or datetime.datetime.now()
        self.number_of_rounds = NUMBER_OF_ROUND or int()
        self.timer = timer or bullet or blitz or coup_rapide or str()
        self.description = description or str()
        self.players = []
        self.rounds = []

    def add_tournament_player(self, player):
        if isinstance(player, Player):
            self.players.append(player)

    def create_first_round(self):
        """Create first round and the matches from this one"""
        first_round = Round(name="Round1")
        players = deepcopy(sorted(self.players, key=lambda
            player: player.rank, reverse=True))
        length = len(players)
        middle_index = length // 2
        above = players[:middle_index]
        below = players[middle_index:]
        for player1, player2 in zip(above, below):
            player1 : Player
            player2 : Player
            player1.history.append(player2.id_)
            player2.history.append(player1.id_)
            first_round.add_match(Match(player1, player2))
            self.rounds.append(first_round)

    def start_other_round(self):
        other_round = Round(name="Round2")
        self.rounds.append(other_round)

    def __repr__(self):
        return f"{self.tournament_name} {self.location} {self.creation_date} " \
               f"{self.number_of_rounds} {self.timer} {self.description} " \
               f"{self.players} {self.rounds}"


tournoi = Tournament(tournament_name='le tournoi', location='Paris',
                     creation_date='12.10.2021', timer='bullet',
                     description='le grand tournoi des débutants en python')
tournoi2 = Tournament(tournament_name='tournoi2', location='Paris',
                     creation_date='12.10.2021', timer='bullet',
                     description='le grand tournoi des débutants en python')

player_one = Player(id_=1, first_name='Breton', last_name='Pedro',
                 birthday='18.10.1900', gender='M', rank=20)
player_two = Player(id_=2, first_name='Raoul', last_name='bernard',
                    birthday='12.10.2020', gender='F', rank=10)


tournoi.add_tournament_player(player_one)
tournoi.add_tournament_player(player_two)
tournoi.create_first_round()
tournoi.start_other_round()


# print(player_one, player_two)
# print(tournoi, tournoi2)
# print(tournoi.location)
# print(tournoi.players)
print(tournoi.rounds)
# print(tournoi.players[0].birthday)
# print(tournoi.rounds[1].name)
# print(tournoi.rounds[1].start_date)
# print(tournoi.rounds[1].matches)
