"""
Game loop management.
"""
import pygame
from utils.constants import (CHANGE_TO_ENTRANCE, CHANGE_TO_YARD)


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
        5. Update pygame display
        6. Tick the game clock to maintain framerate

        Should be called continuously in the main.py game loop.

        Returns:
            None
        """
        # Input
        self.input_handler.process_input()

        # Draw
        self.background.draw()
        self.player.draw()

        # Update game state before rendering
        self.player.update()
        self._handle_edge_transition()

        # Render current frame
        pygame.display.update()

        # Clock
        self.screen.clock.tick(self.screen.framerate)  # slows the game to framerate speed

        return None

    def _handle_edge_transition(self) -> None:
        """
        Handles edge transition.

        Returns:
            None
        """
        screen_width = self.screen.screen.get_width()
        margin = 10

        at_right_edge = self.player.rect.right >= screen_width - margin
        at_left_edge = self.player.rect.left <= margin
        scene = self.mediator.current_scene

        if at_right_edge:
            self._transition_scene(scene, spawn_on_left=True, screen_width=screen_width, margin=margin)
        elif at_left_edge:
            self._transition_scene(scene, spawn_on_left=False, screen_width=screen_width, margin=margin)

    def _transition_scene(
        self,
        scene: str,
        *,
        spawn_on_left: bool,
        screen_width: int,
        margin: int
    ) -> None:
        """
        Handles screen transition.

        Attributes:
            scene (str): Current background.
            spawn_on_left (bool): Is player going to spawn to left.
            spawn_on_left (int): The screen width.
            margin (int): The margin between player and screen edge.

        Returns:
            None
        """
        if scene == "entrance":
            self.mediator.handle_command(CHANGE_TO_YARD)
        elif scene == "yard":
            self.mediator.handle_command(CHANGE_TO_ENTRANCE)
        else:
            return

        if spawn_on_left:
            self.player.rect.left = margin
        else:
            self.player.rect.right = screen_width - margin
