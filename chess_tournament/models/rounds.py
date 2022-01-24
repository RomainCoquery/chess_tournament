from datetime import datetime
from chess_tournament.models.matchs import Match


class Round:
    def __init__(self, name):
        self.name = name
        self.start_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.end_date = None
        self.matches = []

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
    def get_all(cls, store, match_dict):
        rounds_ = []
        for r in match_dict:
            rounds = Round(r['name'])
            rounds.start_date = (r['start_date']) if r['start_date'] else None
            rounds.end_date = (r['end_date']) if r['end_date'] else None
            rounds.matches = Match.get_all(store, r['matches'])
            rounds_.append(rounds)

        return rounds_
