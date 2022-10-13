from random import random
from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor

class MoveActorsAction(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast, script):
        if not script.get_actions("update")[1].get_game_state():
            snakes = cast.get_actors("snakes")
            if random() < 0.2:
                for i in snakes:
                    i.grow_tail()

        for i in cast.get_all_actors():
            i.move_next()