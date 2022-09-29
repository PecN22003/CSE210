from random import choice
from game.words import words as dictionary

class Hider:
    """
    The person that picks a word
    """
    def __init__(self) -> None:

        # Pick a random word from the dictionary
        self._word = choice(dictionary.split(","))

        # length of the word
        self.length = len(self._word)

        # which letters have been guessed
        self.hint_string = []
        for _ in range(self.length):
            self.hint_string.append("_")

        self.guessed_letters = set()

    def check_letter(self, letter: str) -> bool:
        """
        Checks if a letter is in the word, and will update the hint_string list as appropriate

        letter (str of length 1): the guessed letter

        returns true if the letter is in the word, false otherwise
        """

        if len(letter) != 1:
            print("Bad guess: not enough letters, or too few")
            return True

        # lletter short for lowercase letter
        lletter = letter.lower()

        self.guessed_letters.add(lletter)

        return_value = False
        for i, value in enumerate(self._word):
            if lletter == value:
                self.hint_string[i] = value
                return_value = True
        return return_value

    def check_finished(self) -> bool:
        return "".join(self.hint_string) == self._word
    