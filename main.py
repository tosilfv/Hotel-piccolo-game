"""
Main entry point for the Piccolo game.

This module initializes and runs the game loop and delegates game logic
to the Game class. The game continues running until the user closes the window.
"""
import sys
import pygame
from control.game_factory import create_game
from utils.logging_config import configure_logging

# Logging
configure_logging()

# This function starts the game
def run_game():
    """Main game loop"""
    # Initialize all required Pygame modules before creating the game
    pygame.init()
    pygame.font.init()

    game = create_game()
    game_is_on = True

    while game_is_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_on = False
        game.run()

    # Quit and exit
    pygame.quit()
    sys.exit()

# This ensures that the game starts only when the file is ran directly
if __name__ == "__main__":
    run_game()
