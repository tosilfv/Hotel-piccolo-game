"""
Game loop management.
"""
import pygame

# Game
class Game:
    """
    Game loop manager.

    Attributes:
        screen: Screen instance for display operations.
        background: Background instance for scene rendering.
        player: Player instance for character management.
        mediator: Mediator instance for game internal communication.
        input_handler: InputHandle instance for separating user input.
    """
    def __init__(self, screen, background, player, mediator, input_handler) -> None:
        self.screen = screen
        self.background = background
        self.player = player
        self.mediator = mediator
        self.input_handler = input_handler

    def run(self) -> None:
        """
        Executes one frame of the game loop.

        Performs the following operations in order:
        1. Transform input to handler
        2. Draw background
        3. Draw player
        4. Update player
        5. Update pygame display
        6. Tick the game clock to maintain framerate

        Should be called continuously in the main.py Game Loop.
        """
        self.input_handler.process_input()

        # Draw
        self.background.draw()
        self.player.draw()

        # Update
        self.player.update()
        pygame.display.update()  # (Screen Flip)

        # Clock (Slow the Game to framerate speed)
        self.screen.clock.tick(self.screen.framerate)
