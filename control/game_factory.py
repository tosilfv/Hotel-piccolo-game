"""
Build and return a game instance.
"""
from game_objects.background import Background
from game_objects.player import Player
from game_objects.screen import Screen
from control.game import Game
from control.input_handler import InputHandler
from control.mediator import Mediator


def create_game() -> Game:
    """
    Build a Game class instance.

    Returns:
        Game(screen, background, player, mediator, input_handler): Built game instance.
    """
    screen = Screen()
    background = Background(screen)
    player = Player(screen)
    mediator = Mediator(background, player)
    input_handler = InputHandler(mediator)

    return Game(
        screen=screen,
        background=background,
        player=player,
        mediator=mediator,
        input_handler=input_handler
    )
