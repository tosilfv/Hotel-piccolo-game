"""
Game loop management.
"""

import pygame
from classes.background import Background
from classes.player import Player
from classes.screen import Screen
from classes.user import User

# Game
class Game:
    """
    Game loop manager.

    Attributes:
        screen: Screen instance for display operations.
        background: Background instance for scene rendering.
        player: Player instance for character management.
        user: User instance for input management.
    """
    def __init__(self, screen, background, player, user) -> None:
        self.screen = screen
        self.background = background
        self.player = player
        self.user = user

    def run(self) -> None:
        """
        Executes one frame of the game loop.

        Performs the following operations in order:
        1. Draw background
        2. Draw player
        3. Update user input
        4. Update pygame display
        5. Tick the game clock to maintain framerate

        Should be called continuously in the main.py Game Loop.
        """
        # Draw
        self.background.draw()
        self.player.draw()

        # Update
        self.user.update()
        pygame.display.update()

        # Clock
        self.screen.clock.tick(self.screen.framerate)

# Create Objects
_screen = Screen()
_background = Background(_screen)
_player = Player(_screen)
_user = User()

# Create Game
game = Game(_screen, _background, _player, _user)
