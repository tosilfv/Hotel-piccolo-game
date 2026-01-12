"""
Build and return a Game instance.
"""
from classes.background import Background
from classes.player import Player
from classes.screen import Screen
from control.game import Game
from control.input_handler import InputHandler
from control.mediator import Mediator

# Create Game
def create_game() -> Game:
    """
    Build a Game instance.

    Returns:
        Game(screen, background, player, mediator, input_handler): Built Game instance.
    """
    screen = Screen()
    background = Background(screen)
    player = Player(screen)
    mediator = Mediator(player)
    input_handler = InputHandler(mediator)

    return Game(
        screen=screen,
        background=background,
        player=player,
        mediator=mediator,
        input_handler=input_handler
    )
