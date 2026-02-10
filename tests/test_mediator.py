"""Unit tests for Mediator class"""
from unittest.mock import Mock, MagicMock
from control.game import Game
from control.mediator import Mediator
from utils.commands import Command
from utils.constants import (EDGE_MARGIN, ENTRANCE, SCREEN_WIDTH, SOUND_JUMP,
                             YARD)


class TestMediator:
    """Tests for Mediator class"""

    def setup_method(self):
        # Setup: create mocks
        self.mock_audio_manager = MagicMock()
        self.mock_player = MagicMock()
        self.mock_player.jump = MagicMock()
        self.mock_player.move_left = MagicMock()
        self.mock_player.move_right = MagicMock()
        self.mock_player.rect = Mock()
        self.mock_background = MagicMock()
        self.mock_background.change_background = MagicMock()
        self.screen = Mock()
        self.screen.clock = Mock()
        self.screen.framerate = 60
        self.player = Mock()
        self.player.rect = Mock()
        self.trolley = Mock()
        self.mediator = Mock()
        self.input_handler = Mock()

        # Action: create Mediator instance
        self.mediator = Mediator(
            self.mock_background,
            self.mock_player,
            self.mock_audio_manager
        )

        self.game = Game(
            screen=self.screen,
            background=self.mock_background,
            player=self.mock_player,
            trolley=self.trolley,
            mediator=self.mediator,
            input_handler=self.input_handler
        )

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

    def test_play_jump_sound_direct(self):
        # Action
        self.mediator.play_jump_sound()

        # Assert
        self.mock_audio_manager.play_sound.assert_called_once_with(SOUND_JUMP)
        self.mock_audio_manager.play_sound.reset_mock()

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

    def test_change_to_entrance_direct(self):
        # Setup: set current scene to YARD
        self.mediator.current_scene = YARD

        # Action
        self.mediator.change_to_entrance()

        # Assert
        assert self.mediator.current_scene == ENTRANCE
        self.mock_background.change_background.assert_called_once_with(ENTRANCE)
        self.mock_audio_manager.stop_music.assert_called_once()
        self.mock_background.change_background.reset_mock()
        self.mock_audio_manager.stop_music.reset_mock()

    def test_change_to_entrance_no_change_if_already_in_scene(self):
        # Setup: set current scene to ENTRANCE
        self.mediator.current_scene = ENTRANCE

        # Action
        self.mediator.change_to_entrance()

        # Assert
        self.mock_background.change_background.assert_not_called()
        self.mock_audio_manager.stop_music.assert_not_called()

    def test_change_to_yard_direct(self):
        # Setup: set current scene to ENTRANCE
        self.mediator.current_scene = ENTRANCE

        # Action
        self.mediator.change_to_yard()

        # Assert
        assert self.mediator.current_scene == YARD
        self.mock_background.change_background.assert_called_once_with(YARD)
        self.mock_audio_manager.play_music.assert_called_once_with("music_yard.wav")
        self.mock_background.change_background.reset_mock()
        self.mock_audio_manager.play_music.reset_mock()

    def test_change_to_yard_no_change_if_already_in_scene(self):
        # Setup: set current scene to YARD
        self.mediator.current_scene = YARD

        # Action
        self.mediator.change_to_yard()

        # Assert
        self.mock_background.change_background.assert_not_called()
        self.mock_audio_manager.play_music.assert_not_called()

    def test_handle_command_unknown_command_sets_running_false(self):
        # Setup & Action: pass None as unknown command
        self.mediator.handle_command(None)

        # Assert
        assert self.mediator.running is False

    def test_handle_edge_transition_left(self):
        # Setup
        self.mock_player.rect.left = EDGE_MARGIN - 1
        self.mock_player.rect.right = 50
        self.mediator.current_scene = ENTRANCE

        # Action
        self.mediator.handle_edge_transition()

        # Assert
        assert self.mediator.current_scene == YARD
        assert self.mock_player.rect.right == SCREEN_WIDTH - EDGE_MARGIN

    def test_handle_edge_transition_right(self):
        # Setup
        self.mock_player.rect.left = SCREEN_WIDTH - EDGE_MARGIN + 1
        self.mock_player.rect.right = SCREEN_WIDTH
        self.mediator.current_scene = YARD

        # Action
        self.mediator.handle_edge_transition()

        # Assert
        assert self.mediator.current_scene == ENTRANCE
        assert self.mock_player.rect.left == EDGE_MARGIN

    def test_handle_edge_transition_middle_no_change(self):
        # Setup
        self.mock_player.rect.left = 100
        self.mock_player.rect.right = 150
        self.mediator.current_scene = ENTRANCE

        # Action
        self.mediator.handle_edge_transition()

        # Assert
        assert self.mediator.current_scene == ENTRANCE

    def test_scene_transition_spawn_left(self):
        # Setup
        self.mediator.current_scene = YARD

        # Action
        self.mediator._scene_transition(
            spawn_on_left=True,
            screen_width=SCREEN_WIDTH,
            margin=EDGE_MARGIN
        )

        # Assert
        assert self.mediator.current_scene == ENTRANCE
        assert self.mock_player.rect.left == EDGE_MARGIN

    def test_scene_transition_spawn_right(self):
        # Setup
        self.mediator.current_scene = ENTRANCE

        # Action
        self.mediator._scene_transition(
            spawn_on_left=False,
            screen_width=SCREEN_WIDTH,
            margin=EDGE_MARGIN
        )

        # Assert
        assert self.mediator.current_scene == YARD
        assert self.mock_player.rect.right == SCREEN_WIDTH - EDGE_MARGIN
