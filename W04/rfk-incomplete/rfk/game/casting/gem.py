from game.casting.actor import Actor


class Gem(Actor):
    def __init__(self):
        super().__init__()
        self._text = "*"