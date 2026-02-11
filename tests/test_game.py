"""Unit tests for Game class"""
from unittest.mock import Mock, patch
from control.game import Game


class TestGame:
    def setup_method(self):
        # Setup
        self.screen = Mock()
        self.screen.clock = Mock()
        self.screen.framerate = 60

        self.background = Mock()
        self.player = Mock()
        self.player.rect = Mock()
        self.trolley = Mock()
        self.mediator = Mock()
        self.mediator.current_scene = Mock()
        self.input_handler = Mock()

        self.game = Game(
            screen=self.screen,
            background=self.background,
            player=self.player,
            trolley=self.trolley,
            mediator=self.mediator,
            input_handler=self.input_handler
        )

    def test_run_calls_all_methods(self):
        # Action
        with patch('pygame.display.update') as mock_update:
            self.game.run()

        # Assert
        self.input_handler.process_input.assert_called_once()
        self.background.draw.assert_called_once()
        self.player.draw.assert_called_once()
        self.trolley.draw.assert_called_once_with(self.mediator.current_scene)
        self.player.update.assert_called_once_with(self.mediator.running)
        self.trolley.update.assert_called_once_with(self.player)
        mock_update.assert_called_once()
        self.screen.clock.tick.assert_called_once_with(self.screen.framerate)
