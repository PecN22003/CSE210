from game.casting.actor import Actor


class Banner(Actor):
    def __init__(self):
        super().__init__()
        self._score = 0

    def increment_score(self):
        self._score += 1

    def decrement_score(self):
        self._score -= 1

    def get_score(self):
        return self._score