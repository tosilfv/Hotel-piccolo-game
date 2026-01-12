"""
Input handler for separating user input from other game operations.
"""
import pygame
from utils.constants import (CMD_MOVE_LEFT, CMD_MOVE_RIGHT)

# Input Handler
class InputHandler:
    """
    Handles user input and translates it into mediator commands.

    Attributes:
        mediator: Mediator instance for game internal communication.
    """
    def __init__(self, mediator) -> None:
        self.mediator = mediator

    def process_input(self) -> None:
        """
        Process user input for mediator commands.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.mediator.handle_command(CMD_MOVE_LEFT)

        if keys[pygame.K_RIGHT]:
            self.mediator.handle_command(CMD_MOVE_RIGHT)
