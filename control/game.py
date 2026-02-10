"""
Game loop management.
"""
import pygame


class Game:
    """
    Manages game loop.

    Responsibilities:
        - Execute the main game loop frame-by-frame
        - Coordinate input handling, rendering, and game state updates
        - Update player, background, and mediator states
        - Handle edge transitions when player reaches screen edges
        - Maintain framerate via screen clock
        - Serve as the central point connecting screen, background, player, mediator, and input handler

    Attributes:
        screen: Screen instance for display operations.
        background: Background instance for scene rendering.
        player: Player instance for character management.
        trolley: Trolley instance for trolley item management.
        mediator: Mediator instance for game internal communication.
        input_handler: InputHandler instance for separating user input.
    """

    def __init__(self, screen, background, player, trolley, mediator, input_handler):
        self.screen = screen
        self.background = background
        self.player = player
        self.trolley = trolley
        self.mediator = mediator
        self.input_handler = input_handler

    def run(self) -> None:
        """
        Execute one frame of the game loop.

        Performs the following operations in order:
        1. Transform input to handler
        2. Draw background
        3. Draw player
        4. Draw trolley
        5. Update player
        6. Handle edge transition
        7. Update Pygame display
        8. Tick the game clock to maintain framerate

        Should be called continuously in the main.py game loop.
        """
        # 1. Input
        self.input_handler.process_input()

        # 2.-4. Draw
        self.background.draw()
        self.player.draw()
        self.trolley.draw()

        # 5.-6. Update game state before rendering
        running = self.mediator.running
        self.player.update(running)
        self.mediator.handle_edge_transition()

        # 7. Render current frame
        pygame.display.update()

        # 8. Clock slows the game to framerate speed
        self.screen.clock.tick(self.screen.framerate)
