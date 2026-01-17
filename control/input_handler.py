"""
Input handler for separating user input from other game operations.
"""
import pygame
from utils.constants import (CMD_JUMP, CMD_MOVE_LEFT, CMD_MOVE_RIGHT)


# Input handler
class InputHandler:
    """
    Handles user input and translates it into mediator commands.

    Attributes:
        mediator: Mediator instance for game internal communication.
    """
    
    def __init__(self, mediator):
        self.mediator = mediator

    def process_input(self) -> None:
        """
        Process user input for mediator commands.
        
        Attributes:
            keys: Pygame key method.
        
        Returns:
            None
        """
        # Returns a list of boolean values whether each key is pressed or not
        keys = pygame.key.get_pressed()

        # Command to left
        if keys[pygame.K_LEFT]:
            self.mediator.handle_command(CMD_MOVE_LEFT)

        # Command to right
        if keys[pygame.K_RIGHT]:
            self.mediator.handle_command(CMD_MOVE_RIGHT)

        # Command to jump
        if keys[pygame.K_SPACE]:
            self.mediator.handle_command(CMD_JUMP)
        
        return None
