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
        for i in cast.get_all_actors():
            i.move_next()
        return super().execute(cast, script)