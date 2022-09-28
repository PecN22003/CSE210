default_images = ["parachute_0.txt", "parachute_1.txt", "parachute_2.txt", "parachute_3.txt", "parachute_4.txt", "parachute_dead.txt"]

class Guesser:

    def __init__(self, images: list[str] = default_images) -> None:
        self.bad_guesses = 0
        self.images = images
        self._dead = False

    def increment_bad_guesses (self, increment: bool = True) -> None:
        self.bad_guesses += int(increment)

    def is_dead(self) -> bool:
        self._dead = self.bad_guesses >= 5
        return self._dead