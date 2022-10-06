from game.casting.actor import Actor


class Asteroid (Actor):
    def __init__(self) -> None:
        super().__init__()
        self._text = "o"