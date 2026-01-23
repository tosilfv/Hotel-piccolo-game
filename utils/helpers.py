"""
Helper functions for game utilities.
"""
import pygame
import logging
from utils.constants import (DEFAULT_FONT_SIZE, DEFAULT_SURFACE_COLOR,
                             DEFAULT_SURFACE_SIZE, DEFAULT_TEXT_SURFACE_SIZE,
                             WHITE)


# Load image
def load_image(path: str, default_color=DEFAULT_SURFACE_COLOR, default_size=DEFAULT_SURFACE_SIZE) -> pygame.Surface:
    """
    Load an image file with error handling and placeholder fallback.
    
    Args:
        path (str): File path to the image file.
        default_color (tuple): RGB color tuple for placeholder.
        default_size (tuple): Width and height for placeholder surface.
    
    Returns:
        pygame.Surface: Loaded image surface or placeholder surface if loading fails.
    
    If an image fails to load (e.g. file not found, invalid format), a placeholder image
    with a default color and size will be returned instead.

    Note:
        Assumes that pygame and pygame.font have been initialized
        before this function is called.
    """
    try:
        # Attempt to load the image
        image = pygame.image.load(path).convert_alpha()
        return image
    except pygame.error as e:
        # Handle Pygame-specific errors
        error_message = f"Error loading image from '{path}': {e}"
        logging.error(error_message)  # Log the error
    except FileNotFoundError:
        # Handle case where the file is not found
        error_message = f"File not found: '{path}'."
        logging.error(error_message)  # Log the error

    # If loading fails, return a placeholder surface
    placeholder = pygame.Surface(default_size)
    placeholder.fill(default_color)

    # Draw a "placeholder" message on the image
    font = pygame.font.Font(None, DEFAULT_FONT_SIZE)
    text_surface = font.render("Image not found", True, WHITE)

    # Position the text on the surface
    placeholder.blit(text_surface, DEFAULT_TEXT_SURFACE_SIZE)

    return placeholder
