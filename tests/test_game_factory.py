"""Unit tests for Game factory creation"""
from unittest.mock import patch, MagicMock
from game_objects.background import Background
from game_objects.player import Player
from game_objects.screen import Screen
from game_objects.trolley import Trolley
from control.game import Game
from control.game_factory import create_game
from control.input_handler import InputHandler
from control.mediator import Mediator


class TestGameFactory:
    def setup_method(self):
        # Setup: mock instances
        self.screen_instance = MagicMock()
        self.audio_manager_instance = MagicMock()
        self.background_instance = MagicMock()
        self.player_instance = MagicMock()
        self.mediator_instance = MagicMock()
        self.input_handler_instance = MagicMock()
        self.trolley_instance = MagicMock()

    def test_create_game_returns_game_instance(self):
        # Action
        game = create_game()

        # Assert
        assert isinstance(game, Game)

    def test_create_game_has_all_components(self):
        # Action
        game = create_game()

        # Assert
        assert hasattr(game, "screen")
        assert hasattr(game, "background")
        assert hasattr(game, "player")
        assert hasattr(game, "trolley")
        assert hasattr(game, "mediator")
        assert hasattr(game, "input_handler")

    def test_create_game_component_types(self):
        # Action
        game = create_game()

        # Assert
        assert isinstance(game.screen, Screen)
        assert isinstance(game.background, Background)
        assert isinstance(game.player, Player)
        assert isinstance(game.trolley, Trolley)
        assert isinstance(game.mediator, Mediator)
        assert isinstance(game.input_handler, InputHandler)

    @patch("control.game_factory.InputHandler")
    @patch("control.game_factory.Mediator")
    @patch("control.game_factory.Player")
    @patch("control.game_factory.Trolley")
    @patch("control.game_factory.Background")
    @patch("control.game_factory.AudioManager")
    @patch("control.game_factory.Screen")
    def test_create_game_with_mocks(
        self,
        mock_screen,
        mock_audio_manager,
        mock_background,
        mock_trolley,
        mock_player,
        mock_mediator,
        mock_input
    ):
        # Setup: patch returns
        mock_screen.return_value = self.screen_instance
        mock_audio_manager.return_value = self.audio_manager_instance
        mock_background.return_value = self.background_instance
        mock_player.return_value = self.player_instance
        mock_mediator.return_value = self.mediator_instance
        mock_input.return_value = self.input_handler_instance
        mock_trolley.return_value = self.trolley_instance

        # Player needs mediator argument
        self.player_instance.mediator = None

        # Action
        game = create_game()

        # Assert: constructor calls
        mock_screen.assert_called_once()
        mock_audio_manager.assert_called_once()
        mock_background.assert_called_once_with(self.screen_instance)
        mock_player.assert_called_once_with(self.screen_instance, mediator=None)
        mock_trolley.assert_called_once_with(self.screen_instance)
        mock_mediator.assert_called_once_with(
            self.background_instance,
            self.player_instance,
            self.trolley_instance,
            self.audio_manager_instance
        )
        mock_input.assert_called_once_with(self.mediator_instance)

        # Assert: returned game has correct mocked components
        assert game.screen == self.screen_instance
        assert game.background == self.background_instance
        assert game.player == self.player_instance
        assert game.trolley == self.trolley_instance
        assert game.mediator == self.mediator_instance
        assert game.input_handler == self.input_handler_instance

        # Assert: player.mediator is correctly linked
        assert self.player_instance.mediator == self.mediator_instance
