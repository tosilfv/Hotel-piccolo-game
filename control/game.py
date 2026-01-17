"""
Game loop management.
"""
import pygame
from utils.constants import (CHANGE_TO_ENTRANCE, CHANGE_TO_YARD, ENTRANCE,
                             SCREEN_WIDTH, TEN, YARD)


# Game
class Game:
    """
    Manages game loop.

    Attributes:
        screen: Screen instance for display operations.
        background: Background instance for scene rendering.
        player: Player instance for character management.
        mediator: Mediator instance for game internal communication.
        input_handler: InputHandler instance for separating user input.
    """
    
    def __init__(self, screen, background, player, mediator, input_handler):
        self.screen = screen
        self.background = background
        self.player = player
        self.mediator = mediator
        self.input_handler = input_handler

    def run(self) -> None:
        """
        Execute one frame of the game loop.

        Performs the following operations in order:
        1. Transform input to handler
        2. Draw background
        3. Draw player
        4. Update player
        5. Handle edge transition
        6. Update pygame display
        7. Tick the game clock to maintain framerate

        Should be called continuously in the main.py game loop.

        Returns:
            None
        """
        # 1. Input
        self.input_handler.process_input()

        # 2.-3. Draw
        self.background.draw()
        self.player.draw()

        # 4.-5. Update game state before rendering
        self.player.update()
        self._handle_edge_transition()

        # 6. Render current frame
        pygame.display.update()

        # 7. Clock
        self.screen.clock.tick(self.screen.framerate)  # slows the game to framerate speed

        return None

    def _handle_edge_transition(self) -> None:
        """
        Handle transition when player reaches screen edge.

        Returns:
            None
        """
        # For tests player object can be a Mock object
        try:
            left = self.player.rect.left
            right = self.player.rect.right
        except AttributeError:
            return

        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            return
        
        # Set constants
        margin = TEN
        screen_width = SCREEN_WIDTH

        # Set left and right edge values and save current scene
        at_left_edge = (left <= margin)
        at_right_edge = (right >= screen_width - margin)
        scene = self.mediator.current_scene

        # Handle the transition when player exits scene to left
        if at_left_edge:
            self._scene_transition(scene, spawn_on_left=False, screen_width=screen_width, margin=margin)
        # Handle the transition when player exits scene to right
        elif at_right_edge:
            self._scene_transition(scene, spawn_on_left=True, screen_width=screen_width, margin=margin)

    def _scene_transition(self, scene: str, *, spawn_on_left: bool, screen_width: int, margin: int) -> None:
        """
        Handle scene transition by player spawning and calling mediator for scene change.

        Attributes:
            scene (str): Current background.
            *: Forces following attributes to be called with their name included.
            spawn_on_left (bool): Whether player is going to spawn to left.
            screen_width (int): The screen width.
            margin (int): The margin between player and screen edge.

        Returns:
            None
        """
        # Change scene
        if scene == ENTRANCE:
            self.mediator.handle_command(CHANGE_TO_YARD)
        elif scene == YARD:
            self.mediator.handle_command(CHANGE_TO_ENTRANCE)
        else:
            return

        # Spawn player
        if spawn_on_left:
            self.player.rect.left = margin
        else:
            self.player.rect.right = screen_width - margin
