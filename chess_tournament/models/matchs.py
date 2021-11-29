

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
