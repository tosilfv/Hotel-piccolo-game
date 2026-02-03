"""Unit tests for Mediator class"""
from unittest.mock import MagicMock
from control.mediator import Mediator
from utils.commands import Command
from utils.constants import ENTRANCE, YARD


class TestMediator:
    """Tests for Mediator class"""

    def setup_method(self):
        # Setup: create mocks for player, background, and audio manager
        self.mock_audio_manager = MagicMock()
        self.mock_player = MagicMock()
        self.mock_player.jump = MagicMock()
        self.mock_player.move_left = MagicMock()
        self.mock_player.move_right = MagicMock()
        self.mock_background = MagicMock()
        self.mock_background.change_background = MagicMock()

        # Action: create Mediator instance
        self.mediator = Mediator(
            self.mock_background,
            self.mock_player,
            self.mock_audio_manager
        )

    def test_move_commands_call_player(self):
        # Action & Assert: MOVE_LEFT
        self.mediator.handle_command(Command.MOVE_LEFT)
        assert self.mediator.running is True
        self.mock_player.move_left.assert_called_once()
        self.mock_player.move_left.reset_mock()

        # Action & Assert: MOVE_RIGHT
        self.mediator.handle_command(Command.MOVE_RIGHT)
        assert self.mediator.running is True
        self.mock_player.move_right.assert_called_once()
        self.mock_player.move_right.reset_mock()

        # Action & Assert: JUMP
        self.mediator.handle_command(Command.JUMP)
        assert self.mediator.running is False
        self.mock_player.jump.assert_called_once()
        self.mock_player.jump.reset_mock()

    def test_change_background_calls_background(self):
        # Setup & Action: CHANGE_TO_ENTRANCE
        self.mediator.current_scene = YARD
        self.mediator.handle_command(Command.CHANGE_TO_ENTRANCE)
        # Assert
        assert self.mediator.current_scene == ENTRANCE
        self.mock_background.change_background.assert_called_with(ENTRANCE)
        self.mock_audio_manager.stop_music.assert_called_once()
        self.mock_background.change_background.reset_mock()
        self.mock_audio_manager.stop_music.reset_mock()

        # Setup & Action: CHANGE_TO_YARD
        self.mediator.current_scene = ENTRANCE
        self.mediator.handle_command(Command.CHANGE_TO_YARD)
        # Assert
        assert self.mediator.current_scene == YARD
        self.mock_background.change_background.assert_called_with(YARD)
        self.mock_audio_manager.play_music.assert_called_once_with("music_yard.wav")
        self.mock_background.change_background.reset_mock()
        self.mock_audio_manager.play_music.reset_mock()

    def test_running_state(self):
        # Action & Assert: MOVE_LEFT sets running
        self.mediator.handle_command(Command.MOVE_LEFT)
        assert self.mediator.running is True

        # Action & Assert: MOVE_RIGHT sets running
        self.mediator.handle_command(Command.MOVE_RIGHT)
        assert self.mediator.running is True

        # Action & Assert: STOP sets not running
        self.mediator.handle_command(Command.STOP)
        assert self.mediator.running is False

        # Action & Assert: JUMP sets not running
        self.mediator.handle_command(Command.JUMP)
        assert self.mediator.running is False

        # Action & Assert: unknown command sets not running
        self.mediator.handle_command(None)
        assert self.mediator.running is False

    def test_no_background_change_when_already_in_scene(self):
        # Setup & Action: already in ENTRANCE
        self.mediator.current_scene = ENTRANCE
        self.mediator.handle_command(Command.CHANGE_TO_ENTRANCE)
        # Assert
        self.mock_background.change_background.assert_not_called()
        self.mock_audio_manager.stop_music.assert_not_called()

        # Setup & Action: already in YARD
        self.mediator.current_scene = YARD
        self.mediator.handle_command(Command.CHANGE_TO_YARD)
        # Assert
        self.mock_background.change_background.assert_not_called()
        self.mock_audio_manager.play_music.assert_not_called()
