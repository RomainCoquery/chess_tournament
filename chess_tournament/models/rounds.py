from datetime import datetime


class Round:
    def __init__(self, name):
        self.name = name
        self.start_date = datetime.now().strftime("%d/%m/%Y à %H:%M:%S")
        self.matches = []

    def get_players(self):
        """Get all the players from the round"""
        return [player for match in self.matches for player in
                match.get_players()]

    def add_match(self, match):
        """add matchs in the round"""
        self.matches.append(match)
