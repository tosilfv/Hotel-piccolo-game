"""
Build and return a game instance.
"""
from game_objects.audio_manager import AudioManager
from game_objects.background import Background
from game_objects.bag import Bag
from game_objects.player import Player
from game_objects.screen import Screen
from game_objects.trolley import Trolley
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
            * Trolley
            * Bag
            * Mediator
            * InputHandler
        - Connect mediator to background, player, trolley, bag and audio manager
        - Connect input handler to mediator
        - Return a fully constructed Game instance ready to run

    Returns:
        Game(screen, background, player, trolley, bag, mediator, input_handler): Built game instance.
    """
    screen = Screen()
    audio_manager = AudioManager()
    background = Background(screen)

    # 1. Create instances of the player, trolley and bag with no mediator at first
    player = Player(screen, mediator=None)
    trolley = Trolley(screen, mediator=None)
    bag = Bag(screen, mediator=None)

    # 2. Then create the mediator
    mediator = Mediator(background, player, trolley, bag, audio_manager)

    # 3. Lastly attach mediator to player, trolley and bag
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
