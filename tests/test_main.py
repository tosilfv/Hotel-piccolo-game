"""Unit tests for main.py"""
import main
import pygame
from unittest.mock import patch, MagicMock


class TestMain:
    """Test Main class"""

    def setup_method(self, method):
        """Setup before each test"""
        # main is already imported at top level
        self.main = main

    def test_main_import(self):
        """Test that main.py is imported"""
        assert self.main is not None

    def test_main_creates_game(self):
        """Test that main.py creates and runs a game"""
        # Create a fake game object with a mocked run method
        fake_game = MagicMock()
        fake_game.run = MagicMock()

        # Prepare a QUIT event to exit the game loop immediately
        quit_event = pygame.event.Event(pygame.QUIT)

        # Create patches for all external calls to isolate the test
        patch_create_game = patch.object(
            self.main,
            "create_game",
            return_value=fake_game,
        )
        patch_events = patch(
            "pygame.event.get",
            return_value=[quit_event],
        )
        patch_quit = patch("pygame.quit")
        patch_exit = patch("sys.exit")

        # Apply patches in a context manager
        with (
            patch_create_game as mock_create_game,
            patch_events,
            patch_quit,
            patch_exit,
        ):
            # Run the main game function (loop will exit immediately due to QUIT event)
            self.main.run_game()

        # Verify that the game was created exactly once
        mock_create_game.assert_called_once()

        # Verify that the game's run method was called exactly once
        fake_game.run.assert_called_once()
