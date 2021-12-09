

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
        """update player score after match"""
        self.score = self.score + score

    def validate(self):
        return (
                isinstance(self.id_, int) and
                isinstance(self.last_name, str) and
                isinstance(self.first_name, str) and
                isinstance(self.gender, str) and
                isinstance(self.rank, int)
        )

    def edit(self, id_, last_name, first_name, birthday, gender, rank):
        self.id_ = id_
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank

    def full_name(self):
        """define the full name of player"""
        return f"{self.first_name} {self.last_name}"
