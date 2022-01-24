

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

    def serialized_match(self):
        if self.winner is None:
            id = self.winner
        elif self.winner == 1:
            id = self.player1.id
        elif self.winner == 2:
            id = self.player2.id
        else:
            id = self.player1.id, self.player2.id

        return {
            'player1': self.player1.id,
            'player2': self.player2.id,
            'winner': id
        }

    @classmethod
    def get_all(cls, store, match_dict):
        matches = []
        winner = None
        player1 = None
        player2 = None
        for m in match_dict:
            for p in store["players"]:
                if p.id == (m['player1']):
                    player1 = p
                if p.id == (m['player2']):
                    player2 = p
                if p.id == (m['winner']):
                    winner = p
                elif m['winner'] is None:
                    winner = None

            match = Match(player1=player1, player2=player2)
            match.winner = winner
            matches.append(match)

        return matches
