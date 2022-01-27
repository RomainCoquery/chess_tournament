import datetime

PLAYERS_PER_TOURNAMENT = 8
NUMBER_OF_ROUND = 4


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    def get_players(self):
        """Get all the players from the match"""
        return [self.player1, self.player2]

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

    def __repr__(self):
        return f"{self.player1} {self.player2}"


class Round:
    def __init__(self, name):
        self.name = name
        self.start_date = datetime.datetime.now()
        self.matches = []

    def get_players(self):
        return [player for match in self.matches for player in
                match.get_players()]

    def add_match(self, match):
        self.matches.append(match)

    def __repr__(self):
        return f"{self.name} {self.start_date} {self.matches}"


class Player:
    """Player with is attributes id_player, last_name, first_name,
    birthday, gender, rank"""
    def __init__(self, id_, last_name, first_name, birthday, gender, rank):
        self.id_ = id_
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank
        self.score = 0
        self.history = []

    def update_score(self, score):
        self.score = self.score + score

    def validate(self):
        return (isinstance(self.id_, int)
                and isinstance(self.last_name, str)
                and isinstance(self.first_name, str)
                and isinstance(self.gender, str)
                and isinstance(self.rank, int))

    def full_name(self):
        """define the full name of player"""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f" {self.id_} {self.last_name} {self.first_name} " \
               f"{self.birthday} {self.gender} {self.rank} {self.score} " \
               f"{self.history} "


class Tournament:
    """Tournament with is attributes tournament_name, location,
    creation_date, number_of_rounds, timer, description"""
    def __init__(self, tournament_name, location, creation_date,
                 timer, description):
        self.tournament_name = tournament_name
        self.location = location
        self.creation_date = creation_date or datetime.datetime.now()
        self.number_of_rounds = NUMBER_OF_ROUND
        self.timer = timer or 'bullet' or 'blitz' or 'coup_rapide'
        self.description = description
        self.players = []
        self.rounds = []

    def add_tournament_player(self, player):
        if isinstance(player, Player):
            self.players.append(player)

    def create_first_round(self):
        """
        Create first round and the matches from this one
        """
        first_round = Round(name="Round1")
        players = sorted(self.players, key=lambda player: player.rank, reverse=False)
        length = len(players)
        middle_index = length // 2
        above = players[:middle_index]
        below = players[middle_index:]
        for player1, player2 in zip(above, below):
            player1.history.append(player2.id_)
            player2.history.append(player1.id_)
            first_round.add_match(Match(player1, player2))
        self.rounds.append(first_round)

    def start_other_round(self):
        """Create other round and the matches from this one"""
        new_round = Round(name="Round"+str(len(self.rounds)+1))
        players = sorted(self.players, key=lambda player_: (float(player_.score), int(player_.rank)), reverse=True)
        locked_id_ = []
        missing_players = []
        for player in players:
            if player.id_ in locked_id_:
                continue
            locked_id_.append(player.id_)
            for opponent in players:
                if opponent.id_ in locked_id_ or opponent.id_ in player.history:
                    continue
                locked_id_.append(opponent.id_)
                player.history.append(opponent.id_)
                opponent.history.append(player.id_)
                new_round.add_match(Match(player, opponent))
                break
            else:
                missing_players.append(player.id_)
                locked_id_.remove(player.id_)
        for player in players:
            if player.id_ in missing_players:
                locked_id_.append(player.id_)
                missing_players.remove(player.id_)
                for opponent in players:
                    if opponent.id_ in missing_players:
                        locked_id_.append(opponent.id_)
                        missing_players.remove(opponent.id_)
                        new_round.add_match(Match(player, opponent))
        self.rounds.append(new_round)

    def __repr__(self):
        return f"{self.tournament_name} {self.location} {self.creation_date} " \
               f"{self.number_of_rounds} {self.timer} {self.description} " \
               f"{self.players} {self.rounds}"


'''
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
player_three = Player(id_=3, first_name='baby', last_name='run run',
                      birthday='22.22.2001', gender='M', rank=30)
player_four = Player(id_=4, first_name='Pepe', last_name='Bo',
                     birthday='04.06.1995', gender='F', rank=40)
'''

# tournoi.add_tournament_player(player_one)
# tournoi.add_tournament_player(player_two)
# tournoi.add_tournament_player(player_three)
# tournoi.add_tournament_player(player_four)
# tournoi.create_first_round()
# tournoi.start_other_round()
# tournoi.start_other_round()
# tournoi.start_other_round()

# print(player_one, player_two)
# print(tournoi)
# print(tournoi.location)
# print(tournoi.players)
# print(tournoi.rounds)
# print(tournoi.players[0].birthday)
# print(tournoi.rounds[1].name)
# print(tournoi.rounds[1].start_date)
# print(tournoi.rounds[0].matches)


tournoi = Tournament(tournament_name='Tournoi', location='Ici',
                     creation_date='16.11.2021', timer='Blitz', description='test')

player_one = Player(id_=1, first_name='Breton', last_name='Pedro',
                    birthday='18.10.1900', gender='M', rank=20)
player_two = Player(id_=2, first_name='Raoul', last_name='bernard',
                    birthday='12.10.2020', gender='F', rank=10)
player_three = Player(id_=3, first_name='baby', last_name='run run',
                      birthday='22.22.2001', gender='M', rank=30)
player_four = Player(id_=4, first_name='Pepe', last_name='Bo',
                     birthday='04.06.1995', gender='F', rank=40)
player_five = Player(id_=5, first_name='Pablo', last_name='Picasso',
                     birthday='02.03.2000', gender='M', rank=523)
player_six = Player(id_=6, first_name='Marc', last_name='Bambi',
                    birthday='01.02.3026', gender='F', rank=235)
player_seven = Player(id_=7, first_name='Bea', last_name='Beo',
                      birthday='25.12.1782', gender='F', rank=852)
player_eight = Player(id_=8, first_name='Babe', last_name='Pig',
                      birthday='01.11.2005', gender='M', rank=3)


tournoi.add_tournament_player(player_eight)
tournoi.add_tournament_player(player_seven)
tournoi.add_tournament_player(player_six)
tournoi.add_tournament_player(player_five)
tournoi.add_tournament_player(player_four)
tournoi.add_tournament_player(player_three)
tournoi.add_tournament_player(player_two)
tournoi.add_tournament_player(player_one)

tournoi.create_first_round()

for index, match in enumerate(tournoi.rounds[0].matches, start=1):
    match_player1 = match.player1.first_name, match.player1.last_name, match.player1.rank, match.player1.score
    match_player2 = match.player2.first_name, match.player2.last_name, match.player2.rank, match.player2.score
    print("Match", index, ":"'\n', *match_player1, "VS", *match_player2)


tournoi.rounds[0].matches[0].set_winner(0)
tournoi.rounds[0].matches[1].set_winner(1)
tournoi.rounds[0].matches[2].set_winner(0)
tournoi.rounds[0].matches[3].set_winner(0)

print(tournoi.rounds[0].name)
print(tournoi.rounds[0].matches[0])
print(tournoi.rounds[0].matches[1])
print(tournoi.rounds[0].matches[2])
print(tournoi.rounds[0].matches[3])

tournoi.start_other_round()
print(tournoi.rounds[1].name)
print(tournoi.rounds[1].matches[0])
print(tournoi.rounds[1].matches[1])
print(tournoi.rounds[1].matches[2])
print(tournoi.rounds[1].matches[3])

tournoi.rounds[1].matches[0].set_winner(0)
tournoi.rounds[1].matches[1].set_winner(1)
tournoi.rounds[1].matches[2].set_winner(2)
tournoi.rounds[1].matches[3].set_winner(1)

tournoi.start_other_round()
print(tournoi.rounds[2].name)
print(tournoi.rounds[2].matches[0])
print(tournoi.rounds[2].matches[1])
print(tournoi.rounds[2].matches[2])
print(tournoi.rounds[2].matches[3])

tournoi.rounds[2].matches[0].set_winner(2)
tournoi.rounds[2].matches[1].set_winner(2)
tournoi.rounds[2].matches[2].set_winner(2)
tournoi.rounds[2].matches[3].set_winner(2)

tournoi.start_other_round()
print(tournoi.rounds[3].name)
print(tournoi.rounds[3].matches[0])
print(tournoi.rounds[3].matches[1])
print(tournoi.rounds[3].matches[2])
print(tournoi.rounds[3].matches[3])
