"""
Game loop management.
"""
import pygame
from utils.commands import Command
from utils.constants import (EDGE_MARGIN, ENTRANCE, SCREEN_WIDTH, YARD)


class Game:
    """
    Manages game loop.

    Responsibilities:
        - Execute the main game loop frame-by-frame
        - Coordinate input handling, rendering, and game state updates
        - Update player, background, and mediator states
        - Handle scene transitions when player reaches screen edges
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
        self._handle_edge_transition()

        # 7. Render current frame
        pygame.display.update()

        # 8. Clock slows the game to framerate speed
        self.screen.clock.tick(self.screen.framerate)

    def _handle_edge_transition(self) -> None:
        """
        Handle transition when player reaches screen edge.
        """
        # For tests player object can be a Mock object that doesn't have a rect attribute
        try:
            left = self.player.rect.left
            right = self.player.rect.right
        except AttributeError:
            return

        # Prevent exploding in weird circumstances
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            return
        
        # Set constants
        screen_width = SCREEN_WIDTH

        # Set left and right edge values and save current scene
        at_left_edge = (left <= EDGE_MARGIN)
        at_right_edge = (right >= screen_width - EDGE_MARGIN)

        # Handle the transition when player exits scene to left
        if at_left_edge:
            self._scene_transition(spawn_on_left=False, screen_width=screen_width, margin=EDGE_MARGIN)

        # Handle the transition when player exits scene to right
        elif at_right_edge:
            self._scene_transition(spawn_on_left=True, screen_width=screen_width, margin=EDGE_MARGIN)

    def _scene_transition(self, *, spawn_on_left: bool, screen_width: int, margin: int) -> None:
        """
        Handle scene transition and player spawning and call mediator for scene change.

        Args:
            *: Forces following attributes to be called with their name included.
            spawn_on_left (bool): Whether player is going to spawn to left.
            screen_width (int): The screen width.
            margin (int): The margin between player and screen edge.
        """
        # Change scene using mediator commands
        if self.mediator.current_scene == ENTRANCE:
            self.mediator.handle_command(Command.CHANGE_TO_YARD)
        elif self.mediator.current_scene == YARD:
            self.mediator.handle_command(Command.CHANGE_TO_ENTRANCE)
        else:
            return

        # Spawn player
        if spawn_on_left:
            self.player.rect.left = margin
        else:
            self.player.rect.right = screen_width - margin
