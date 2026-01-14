"""Unit tests for Game class"""
from control.game import Game
from unittest.mock import Mock, patch


class TestGame:
    """Test Game class"""

    def setup_method(self):
        """Setup tests"""
        self.screen = Mock()
        self.screen.clock = Mock()
        self.screen.framerate = 60

        self.background = Mock()
        self.player = Mock()
        self.mediator = Mock()
        self.input_handler = Mock()

        self.game = Game(
            screen=self.screen,
            background=self.background,
            player=self.player,
            mediator=self.mediator,
            input_handler=self.input_handler
        )

    def test_run_calls_input_handler(self):
        """Test input handler process_input method"""
        with patch('pygame.display.update'):
            self.game.run()

        self.input_handler.process_input.assert_called_once()

    def test_run_calls_draw_methods(self):
        """Test background and player draw methods"""
        with patch('pygame.display.update'):
            self.game.run()

        self.background.draw.assert_called_once()
        self.player.draw.assert_called_once()

    def test_run_updates_player(self):
        """Test player update method"""
        with patch('pygame.display.update'):
            self.game.run()
        
        self.player.update.assert_called_once()

    def test_run_updates_display(self):
        """Test display update method"""
        with patch('pygame.display.update') as mock_update:
            self.game.run()

        mock_update.assert_called_once()

    def test_run_ticks_clock(self):
        """Test screen clock tick method"""
        with patch('pygame.display.update'):
            self.game.run()

        self.screen.clock.tick.assert_called_once_with(self.screen.framerate)
