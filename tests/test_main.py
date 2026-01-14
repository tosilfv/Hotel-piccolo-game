"""Unit tests for main.py"""
import pygame
from unittest.mock import patch, MagicMock


class TestMain:
    """Test main.py module"""
    
    def test_main_import(self):
        """Test that main.py is imported"""
        with (patch('pygame.event.get', return_value=[]), 
                patch('pygame.quit'), 
                    patch('sys.exit')):
            import main
        
        assert main is not None

    def test_main_creates_game(self):
        """Test that main.py creates and runs a game"""
        import main

        fake_game = MagicMock()
        fake_game.run = MagicMock()

        with (patch.object(main, "create_game", return_value=fake_game) as mock_create_game,
                patch("pygame.event.get", return_value=[pygame.event.Event(pygame.QUIT)]),
                    patch("pygame.quit"),
                        patch("sys.exit")):
            main.run_game()

        mock_create_game.assert_called_once()
        fake_game.run.assert_called_once()
