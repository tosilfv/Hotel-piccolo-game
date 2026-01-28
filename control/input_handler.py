"""
Input handler for separating user input from other game operations.
"""
import pygame
from utils.commands import Command


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
        """
        # Returns a list of boolean values whether each key is pressed or not
        keys = pygame.key.get_pressed()

        # Left
        if keys[pygame.K_LEFT]:
            self.mediator.handle_command(Command.MOVE_LEFT)

        # Right
        elif keys[pygame.K_RIGHT]:
            self.mediator.handle_command(Command.MOVE_RIGHT)

        # Jump
        if keys[pygame.K_SPACE]:
            self.mediator.handle_command(Command.JUMP)
        
        # Not moving reset command
        if not any(keys):
            self.mediator.handle_command(Command.STOP)
