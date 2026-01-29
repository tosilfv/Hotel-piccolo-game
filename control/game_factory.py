"""
Build and return a game instance.
"""
from game_objects.audio_manager import AudioManager
from game_objects.background import Background
from game_objects.player import Player
from game_objects.screen import Screen
from control.game import Game
from control.input_handler import InputHandler
from control.mediator import Mediator


def create_game() -> Game:
    """
    Build a Game class instance.

    Responsibilities:
        - Instantiate and wire all core game components:
            * Screen
            * AudioManager
            * Background
            * Player
            * Mediator
            * InputHandler
        - Connect mediator to background, player, and audio manager
        - Connect input handler to mediator
        - Return a fully constructed Game instance ready to run

    Returns:
        Game(screen, background, player, mediator, input_handler): Built game instance.
    """
    screen = Screen()
    audio_manager = AudioManager()
    background = Background(screen)

    # 1. Create the player with no mediator at first
    player = Player(screen, mediator=None)

    # 2. Then create the mediator
    mediator = Mediator(background, player, audio_manager)

    # 3. Lastly attach mediator to player
    player.mediator = mediator

    input_handler = InputHandler(mediator)

    return Game(
        screen=screen,
        background=background,
        player=player,
        mediator=mediator,
        input_handler=input_handler
    )
