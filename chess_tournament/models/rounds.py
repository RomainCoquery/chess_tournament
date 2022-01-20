from datetime import datetime
from chess_tournament.models.matchs import Match


class Round:
    def __init__(self, name):
        self.name = name
        self.start_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.end_date = None
        self.matches = []

    def get_players(self):
        """Get all the players from the round"""
        return [player for match in self.matches for player in
                match.get_players()]

    def add_match(self, match):
        """add matchs in the round"""
        self.matches.append(match)

    def serialized_round(self):
        matches = []
        for match in self.matches:
            matches.append(Match.serialized_match(match))
        start_date = self.start_date if self.start_date else None
        end_date = self.end_date if self.end_date else None

        return{
            'name': self.name,
            'start_date': start_date,
            'end_date': end_date,
            'matches': matches
        }

    @classmethod
    def get_all(cls, store, round_dict):
        rounds = []
        for r in round_dict:
            round = Round(r['name'])
            round.start_date = r['start_date'] if r['start_date'] else None
            round.end_date = r['end_date'] if r['end_date'] else None
            round.matches = Match.get_all(store, r['matches'])
            rounds.append(round)
