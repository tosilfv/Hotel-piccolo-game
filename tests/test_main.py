"""Unit tests for main.py"""
import pygame
import main
from unittest.mock import patch, MagicMock


class TestMain:
    """Tests for main.py run_game function"""

    def setup_method(self):
        # Setup: reference to main module
        self.main = main

    def test_main_import(self):
        # Setup: nothing to prepare
        # Action & Assert
        assert self.main is not None

    def test_main_creates_game_and_runs_loop_once(self):
        # Setup
        fake_game = MagicMock()
        fake_game.run = MagicMock()

        # Prepare a QUIT event to exit the loop immediately
        quit_event = pygame.event.Event(pygame.QUIT)

        # Patch external calls
        with patch.object(self.main, "create_game", return_value=fake_game) as mock_create_game, \
             patch("pygame.event.get", return_value=[quit_event]), \
             patch("pygame.quit") as mock_quit, \
             patch("sys.exit") as mock_exit:

            # Action: run the game
            self.main.run_game()

            # Assert: game created and run called
            mock_create_game.assert_called_once()
            fake_game.run.assert_called_once()
            mock_quit.assert_called_once()
            mock_exit.assert_called_once()
