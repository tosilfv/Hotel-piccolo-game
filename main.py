"""
Main entry point for the Piccolo game.

Initializes Pygame, creates the game instance, and manages the main game loop
until the user closes the window.
"""
import pygame
from control.game_factory import create_game
from utils.logging_config import configure_logging

def run_game() -> None:
    """
    Initialize and run the main game loop.
    """
    configure_logging()
    pygame.init()

    try:
        game = create_game()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not running:
                break

            game.run()

    finally:
        pygame.quit()

if __name__ == "__main__":
    run_game()
