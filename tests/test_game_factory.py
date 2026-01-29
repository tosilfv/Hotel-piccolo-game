"""Unit tests for Game factory class"""
from game_objects.screen import Screen
from game_objects.background import Background
from game_objects.player import Player
from control.mediator import Mediator
from control.input_handler import InputHandler
from control.game import Game
from control.game_factory import create_game
from unittest.mock import patch, MagicMock


class TestGameFactory:
    """Test Game factory class"""

    def setup_method(self):
        """Setup tests"""
        # Let's make mocks return mock-instances
        self.screen_instance = MagicMock()
        self.audio_manager_instance = MagicMock()
        self.background_instance = MagicMock()
        self.player_instance = MagicMock()
        self.mediator_instance = MagicMock()
        self.input_handler_instance = MagicMock()
    
    def test_create_game_returns_game_instance(self):
        """Test create_game returns game instance"""
        game = create_game()
        assert isinstance(game, Game)

    def test_create_game_has_all_components(self):
        """Test create_game has all components"""
        game = create_game()
        assert hasattr(game, "screen")
        assert hasattr(game, "background")
        assert hasattr(game, "player")
        assert hasattr(game, "mediator")
        assert hasattr(game, "input_handler")

    def test_create_game_component_types(self):
        """Test create_game component types"""
        game = create_game()
        assert isinstance(game.screen, Screen)
        assert isinstance(game.background, Background)
        assert isinstance(game.player, Player)
        assert isinstance(game.mediator, Mediator)
        assert isinstance(game.input_handler, InputHandler)
    
    # Mock all dependencies
    @patch("control.game_factory.InputHandler")
    @patch("control.game_factory.Mediator")
    @patch("control.game_factory.Player")
    @patch("control.game_factory.Background")
    @patch("control.game_factory.AudioManager")
    @patch("control.game_factory.Screen")
    def test_create_game_with_mocks(
        self,
        mock_screen,
        mock_audio_manager,
        mock_background,
        mock_player,
        mock_mediator,
        mock_input):
        """Test create_game with mocks, taking Player(mediator) into account"""
        
        # Mocks return instances
        self.screen_instance = MagicMock()
        self.audio_manager_instance = MagicMock()
        self.background_instance = MagicMock()
        self.player_instance = MagicMock()
        self.mediator_instance = MagicMock()
        self.input_handler_instance = MagicMock()

        mock_screen.return_value = self.screen_instance
        mock_audio_manager.return_value = self.audio_manager_instance
        mock_background.return_value = self.background_instance

        # Player needs a mediator argument in constructor
        mock_player.return_value = self.player_instance

        # Mediator is None at first
        self.player_instance.mediator = None

        mock_mediator.return_value = self.mediator_instance
        mock_input.return_value = self.input_handler_instance

        # Call create_game
        game = create_game()

        # Assert constructor calls
        mock_screen.assert_called_once()
        mock_audio_manager.assert_called_once()
        mock_background.assert_called_once_with(self.screen_instance)
        mock_player.assert_called_once_with(self.screen_instance, mediator=None)
        mock_mediator.assert_called_once_with(
            self.background_instance,
            self.player_instance,
            self.audio_manager_instance
        )
        mock_input.assert_called_once_with(self.mediator_instance)
