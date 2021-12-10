from constants import NUMBER_OF_ROUNDS
from chess_tournament.models.rounds import Round
from chess_tournament.models.matchs import Match
from chess_tournament.models.players import Player


class Tournament:
    """Tournament with is attributes tournament_name, location,
    creation_date, number_of_rounds, timer, description"""
    def __init__(self, tournament_name, location, creation_date, timer,
                 description):
        self.tournament_name = tournament_name
        self.location = location
        self.creation_date = creation_date
        self.number_of_rounds = NUMBER_OF_ROUNDS
        self.timer = timer or 'bullet' or 'blitz' or 'coup_rapide'
        self.description = description
        self.players = []
        self.rounds = []

    def add_tournament_player(self, player):
        """Add player in the tournament"""
        if isinstance(player, Player):
            self.players.append(player)

    def create_first_round(self):
        """Create first round and the matches from this one"""
        first_round = Round(name="Round1")
        players = sorted(self.players, key=lambda
            player: player.rank, reverse=False)
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
        players = sorted(self.players, key=lambda
            player_: (float(player_.score), int(player_.rank)), reverse=True)
        missing_players = []
        locked_id_ = []
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
        for player in players:
            if len(players) != len(locked_id_):
                if player.id_ not in locked_id_:
                    missing_players.append(player)
                    for i in range(len(missing_players), step=2):
                        new_round.add_match(Match(player, player))
        self.rounds.append(new_round)

    def validate(self):
        return (
                isinstance(self.location, str) and
                isinstance(self.timer, str) and
                isinstance(self.description, str)
        )

    def edit(self, tournament_name, location, creation_date, timer,
             description):
        self.tournament_name = tournament_name
        self.location = location
        self.creation_date = creation_date
        self.number_of_rounds = NUMBER_OF_ROUNDS
        self.timer = timer or 'bullet' or 'blitz' or 'coup_rapide'
        self.description = description
