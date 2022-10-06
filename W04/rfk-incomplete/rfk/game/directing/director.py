from random import randint, shuffle

from game.casting.gem import Gem
from game.casting.asteroid import Asteroid

from game.shared.point import Point
from game.shared.color import Color
from game.shared.constants import FONT_SIZE, COLS, MAX_Y, ROWS, CELL_SIZE


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        gems = cast.get_actors("gems")
        asteroids = cast.get_actors("asteroids")

        new_gem = Gem()
        color = [0 ,0 ,255]
        shuffle(color)
        new_gem.set_color(Color(color[0], color[1], color[2]))
        new_gem.set_font_size = FONT_SIZE
        new_gem.set_position(CELL_SIZE*Point(randint(0,COLS-1), 0))
        new_gem.set_velocity(Point(0,CELL_SIZE))
        cast.add_actor("gems", new_gem)

        new_asteroid = Asteroid()
        new_asteroid.set_color(Color(120, 120, 120))
        new_asteroid.set_font_size = FONT_SIZE
        new_asteroid.set_position(Point(CELL_SIZE*randint(0,COLS-1), 0))
        new_asteroid.set_velocity(Point(0,CELL_SIZE))
        cast.add_actor("asteroids", new_asteroid)

        banner.set_text(f"score: {banner.get_score()}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        for gem in gems:  
            gem.move_next()
            if robot.get_position().equals(gem.get_position()):
                cast.remove_actor("gems", gem)
                banner.increment_score()
                banner.set_text(f"score: {banner.get_score()}") 
            if gem.get_position().get_y() > MAX_Y:
                cast.remove_actor("gems", gem)

        for asteroid in asteroids:
            asteroid.move_next()
            if robot.get_position().equals(asteroid.get_position()):
                cast.remove_actor("asteroids", asteroid)
                banner.decrement_score()
                banner.set_text(f"score: {banner.get_score()}")  
            if asteroid.get_position().get_y() > MAX_Y:
                cast.remove_actor("asteroids", asteroid)
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()