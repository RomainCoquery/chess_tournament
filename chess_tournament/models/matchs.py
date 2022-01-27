

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    def serialized_match(self):
        if self.winner is None:
            id = self.winner
        elif self.winner is False:
            id = False
        else:
            id = self.winner.id

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
                elif m['winner'] is False:
                    winner = False

            match = Match(player1=player1, player2=player2)
            match.winner = winner
            matches.append(match)

        return matches
