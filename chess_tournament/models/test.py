import datetime

PLAYERS_PER_TOURNAMENT = 8
NUMBER_OF_ROUND = 4
PROGRAM_NAME = 'chess_tournament'


# ajoute un round au tournoi
# print la liste de rounds du tournament
# créer un match entre 2 players et l'ajouter au round

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    def create_match(self, player1, player2):
        self.matchs.append(([player1, 0], [player2, 0]))

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
        first_round_matches = list(zip(list_a, list_b))
        self.matches.append(first_round_matches)

    def __repr__(self):
        return f"{self.name} {self.start_date} {self.matches}"

class Player:
    """Player with is attributes id_player, last_name, first_name,
    date_of_birth, gender"""
    def __init__(self, id_, last_name, first_name, birthday, gender, rank):
        self.id_ = id_ or int()
        self.last_name = last_name or str()
        self.first_name = first_name or str()
        self.birthday = birthday or str()
        self.gender = gender or str()
        self.rank = rank or int()

    def full_name(self):
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

    def start_first_round(self):
        first_round = Round(name="Round1")
        self.rounds.append(first_round)

    def start_other_round(self):
        other_round = Round(name='Round2')
        self.rounds.append(other_round)

    def add_tournament_player(self, player):
        if isinstance(player, Player):
            self.players.append(player)

    def __repr__(self):
        return f"{self.tournament_name} {self.location, self.creation_date}"


tournoi = Tournament(tournament_name='le tournoi', location='Paris',
                     creation_date='12.10.2021', timer='bullet',
                     description='le grand tournoi des débutants en python')
tournoi2 = Tournament(tournament_name='tournoi2', location='Paris',
                     creation_date='12.10.2021', timer='bullet',
                     description='le grand tournoi des débutants en python')

player_one = Player(id_=1, first_name='Breton', last_name='Pedro',
                 birthday='18.10.1900', gender='M', rank=None)
player_two = Player(id_=2, first_name='Raoul', last_name='bernard',
                    birthday='12.10.2020', gender='F', rank=10)

tournoi.location='Lyon'
tournoi.add_tournament_player(player_one)
tournoi.start_first_round()
tournoi.start_other_round()

tournoi.players.append(123)
tournoi.add_tournament_player(player_two)


round_test = Round(name="round test")
round_test.create_first_round()

print(player_one, player_two)
print(round_test)
print(tournoi, tournoi2)
print(tournoi.location)
print(tournoi.players)
print(tournoi.rounds)
print(tournoi.players[0].birthday)
print(tournoi.rounds[0].start_date)
print(tournoi.rounds[0].matches)

