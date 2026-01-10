"""
User interaction for the game.
"""
import pygame

# User
class User:
    """
    User interaction.

    Attributes:
        left (bool): Whether keyboard left is pressed.
        right (bool): Whether keyboard right is pressed.
    """
    def __init__(self) -> None:
        self.left = False
        self.right = False

    def user_input(self) -> None:
        """
        Handle user keyboard input.
        """
        keys = pygame.key.get_pressed()

        # Left
        if keys[pygame.K_LEFT]:
            self.left = True
        else:
            self.left = False
        
        # Right
        if keys[pygame.K_RIGHT]:
            self.right = True
        else:
            self.right = False
        
        # Left and right simultaneously
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            self.left = False
            self.right = False

    def update(self) -> None:
        """
        Update user state for the current frame.
        """
        self.user_input()
