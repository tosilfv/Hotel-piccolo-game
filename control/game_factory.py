"""
Factory for creating and configuring a Piccolo game instance.

Initializes the game components and connects their dependencies.
"""
from control.game import Game
from control.input_handler import InputHandler
from control.mediator import Mediator
from game_objects.audio_manager import AudioManager
from game_objects.background import Background
from game_objects.bag import Bag
from game_objects.player import Player
from game_objects.screen import Screen
from game_objects.trolley import Trolley

def create_game() -> Game:
    """Create and return a fully configured Game instance."""
    screen = Screen()
    audio_manager = AudioManager()
    background = Background(screen)

    player = Player(screen, mediator=None)
    trolley = Trolley(screen, mediator=None)
    bag = Bag(screen, mediator=None)

    mediator = Mediator(
        background, player, trolley, bag, audio_manager
    )

    player.mediator = mediator
    trolley.mediator = mediator
    bag.mediator = mediator

    input_handler = InputHandler(mediator)

    return Game(
        screen=screen,
        background=background,
        player=player,
        trolley=trolley,
        bag=bag,
        mediator=mediator,
        input_handler=input_handler
    )
