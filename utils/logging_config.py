"""
Logging configuration for the game.
"""
import logging

# Logging
def configure_logging() -> None:
    """
    Configure global logging settings for the Piccolo game.

    Sets up file-based error logging with a standard format. This function
    should be called once during application startup before any game logic runs.

    This function is intentionally isolated from game logic to keep
    logging configuration centralized and predictable.
    """
    logging.basicConfig(
        filename='piccolo_game_errors.log',
        level=logging.ERROR,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    logging.getLogger("piccolo").setLevel(logging.ERROR)
