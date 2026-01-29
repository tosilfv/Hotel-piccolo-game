"""Unit tests for Mediator class"""
import pytest
from unittest.mock import MagicMock
from control.mediator import Mediator
from utils.commands import Command
from utils.constants import ENTRANCE, YARD


class TestMediator:
    """Tests for Mediator class"""

    @pytest.fixture(autouse=True)
    def setup_mediator(self):
        """Setup mocks and mediator instance"""
        # Mock audio manager
        self.mock_audio_manager = MagicMock()

        # Mock player and its movement methods
        self.mock_player = MagicMock()
        self.mock_player.jump = MagicMock()
        self.mock_player.move_left = MagicMock()
        self.mock_player.move_right = MagicMock()

        # Mock background and its change method
        self.mock_background = MagicMock()
        self.mock_background.change_background = MagicMock()

        # Mediator instance with mocks
        self.mediator = Mediator(self.mock_background, self.mock_player, self.mock_audio_manager)

    def test_move_commands_call_player(self):
        """MOVE_LEFT, MOVE_RIGHT, JUMP call correct player methods"""
        # MOVE_LEFT
        self.mediator.handle_command(Command.MOVE_LEFT)
        self.mock_player.move_left.assert_called_once()
        self.mock_player.move_left.reset_mock()

        # MOVE_RIGHT
        self.mediator.handle_command(Command.MOVE_RIGHT)
        self.mock_player.move_right.assert_called_once()
        self.mock_player.move_right.reset_mock()

        # JUMP
        self.mediator.handle_command(Command.JUMP)
        self.mock_player.jump.assert_called_once()
        self.mock_player.jump.reset_mock()

    def test_change_background_calls_background(self):
        """CHANGE_TO_ENTRANCE/YARD call background change correctly"""
        # CHANGE_TO_ENTRANCE
        self.mediator.current_scene = YARD
        self.mediator.handle_command(Command.CHANGE_TO_ENTRANCE)
        self.mock_background.change_background.assert_called_with(ENTRANCE)
        self.mock_audio_manager.stop_music.assert_called_once()  # AudioManager should stop music
        assert self.mediator.current_scene == ENTRANCE
        self.mock_background.change_background.reset_mock()
        self.mock_audio_manager.stop_music.reset_mock()

        # CHANGE_TO_YARD
        self.mediator.current_scene = ENTRANCE
        self.mediator.handle_command(Command.CHANGE_TO_YARD)
        self.mock_background.change_background.assert_called_with(YARD)
        self.mock_audio_manager.play_music.assert_called_once_with("music_yard.wav")  # AudioManager should play yard music
        assert self.mediator.current_scene == YARD
        self.mock_background.change_background.reset_mock()
        self.mock_audio_manager.play_music.reset_mock()

    def test_running_state(self):
        """Check running attribute is updated correctly"""
        # Moving left
        self.mediator.handle_command(Command.MOVE_LEFT)
        assert self.mediator.running is True

        # Moving right
        self.mediator.handle_command(Command.MOVE_RIGHT)
        assert self.mediator.running is True

        # Stop command
        self.mediator.handle_command(Command.STOP)
        assert self.mediator.running is False

        # Jump resets running
        self.mediator.handle_command(Command.JUMP)
        assert self.mediator.running is False

        # Unknown command also stops running
        self.mediator.handle_command(None)
        assert self.mediator.running is False

    def test_no_background_change_when_already_in_scene(self):
        """Background should not change if already in the scene"""
        # Entrance scene
        self.mediator.current_scene = ENTRANCE
        self.mediator.handle_command(Command.CHANGE_TO_ENTRANCE)
        self.mock_background.change_background.assert_not_called()
        self.mock_audio_manager.stop_music.assert_not_called()

        # Yard scene
        self.mediator.current_scene = YARD
        self.mediator.handle_command(Command.CHANGE_TO_YARD)
        self.mock_background.change_background.assert_not_called()
        self.mock_audio_manager.play_music.assert_not_called()
