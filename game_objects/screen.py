"""
Screen management for the game.
"""
import pygame
from utils.constants import (CAPTION, DISPLAY_SIZE, FRAMERATE)


class Screen:
    """
    Manages the game window and display settings and sets screen caption.

    Attributes:
        screen: Pygame screen display surface (the game window).
        clock: Pygame Clock object for framerate control.
        framerate (int): Target grames per second.
    """
    
    def __init__(self):
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        self.clock = pygame.time.Clock()
        self.framerate = FRAMERATE
        pygame.display.set_caption(CAPTION)
