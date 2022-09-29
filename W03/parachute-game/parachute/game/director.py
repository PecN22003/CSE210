from game.terminal_service import TerminalService
from game.hider import Hider
from game.guesser import Guesser


class Director:

    def __init__(self) -> None:
        
        self._terminal_service = TerminalService()
        self._hider = Hider()
        self._guesser = Guesser()
        self._is_playing = True

    def start_game(self):
        self._do_outputs()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _do_outputs(self):
        self._terminal_service.write_text(f"{''.join(self._hider.hint_string)}\n")
        with open(f"parachute/parachute-man/{self._guesser.images[self._guesser.bad_guesses]}") as man:
            self._terminal_service.write_text(man.read())

    def _get_inputs(self):
        # get a letter guess
        guessed_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")

        # check if the letter is in the word
        letter_is_in_word = self._hider.check_letter(guessed_letter)

        # increment bad guess if needed
        self._guesser.increment_bad_guesses(not letter_is_in_word)

    def _do_updates(self):
        if self._hider.check_finished():
            self._is_playing = False
        if self._guesser.is_dead():
            self._is_playing = False
        