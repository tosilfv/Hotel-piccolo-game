"""Unit tests for Mediator class"""
from unittest.mock import Mock, MagicMock
from control.mediator import Mediator
from utils.commands import Command
from utils.constants import (EDGE_MARGIN, ENTRANCE, FIVE, SCREEN_WIDTH,
                             SOUND_JUMP, YARD)


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

        self.mock_trolley = Mock()
        self.mock_trolley.taken = False

        self.mock_background = MagicMock()
        self.mock_background.change_background = MagicMock()

        # Action: create Mediator instance
        self.mediator = Mediator(
            self.mock_background,
            self.mock_player,
            self.mock_trolley,
            self.mock_audio_manager
        )

    def test_change_background_calls_background(self):
        # Setup & Action: CHANGE_TO_ENTRANCE
        self.mediator.current_scene = YARD
        self.mediator.handle_command(Command.CHANGE_TO_ENTRANCE)

        # Assert
        assert self.mediator.current_scene == ENTRANCE
        self.mock_background.change_background.assert_called_with(ENTRANCE)
        self.mock_audio_manager.stop_music.assert_called_once()

        # Setup & Action: CHANGE_TO_YARD
        self.mediator.current_scene = ENTRANCE
        self.mediator.handle_command(Command.CHANGE_TO_YARD)

        # Assert
        assert self.mediator.current_scene == YARD
        self.mock_background.change_background.assert_called_with(YARD)

    def test_play_jump_sound_direct(self):
        # Action
        self.mediator.play_jump_sound()

        # Assert
        self.mock_audio_manager.play_sound.assert_called_once_with(SOUND_JUMP)


    def test_running_state_by_command_group(self):
        running_commands = (
            Command.MOVE_LEFT,
            Command.MOVE_RIGHT,
            Command.TAKE_TROLLEY
        )

        non_running_commands = (
            Command.JUMP,
            Command.STOP,
            None
        )

        for cmd in running_commands:
            self.mediator.handle_command(cmd)
            assert self.mediator.running is True

        for cmd in non_running_commands:
            self.mediator.handle_command(cmd)
            assert self.mediator.running is False

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
        # Setup
        self.mediator.current_scene = YARD

        # Action
        self.mediator.change_to_entrance()

        # Assert
        assert self.mediator.current_scene == ENTRANCE
        self.mock_background.change_background.assert_called_once_with(ENTRANCE)
        self.mock_audio_manager.stop_music.assert_called_once()

    def test_change_to_entrance_no_change_if_already_in_scene(self):
        # Setup
        self.mediator.current_scene = ENTRANCE

        # Action
        self.mediator.change_to_entrance()

        # Assert
        self.mock_background.change_background.assert_not_called()
        self.mock_audio_manager.stop_music.assert_not_called()

    def test_change_to_yard_direct(self):
        # Setup
        self.mediator.current_scene = ENTRANCE

        # Action
        self.mediator.change_to_yard()

        # Assert
        assert self.mediator.current_scene == YARD
        self.mock_background.change_background.assert_called_once_with(YARD)
        self.mock_audio_manager.play_music.assert_called_once_with("music_yard.wav")

    def test_change_to_yard_no_change_if_already_in_scene(self):
        # Setup
        self.mediator.current_scene = YARD

        # Action
        self.mediator.change_to_yard()

        # Assert
        self.mock_background.change_background.assert_not_called()
        self.mock_audio_manager.play_music.assert_not_called()

    def test_handle_command_unknown_command_sets_running_false(self):
        # Action
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
        assert self.mock_player.rect.right == SCREEN_WIDTH - EDGE_MARGIN - FIVE

    def test_handle_edge_transition_right(self):
        # Setup
        self.mock_player.rect.left = SCREEN_WIDTH - EDGE_MARGIN + 1
        self.mock_player.rect.right = SCREEN_WIDTH
        self.mediator.current_scene = YARD

        # Action
        self.mediator.handle_edge_transition()

        # Assert
        assert self.mediator.current_scene == ENTRANCE
        assert self.mock_player.rect.left == EDGE_MARGIN + FIVE

    def test_handle_edge_transition_middle_no_change(self):
        # Setup
        self.mock_player.rect.left = 100
        self.mock_player.rect.right = 150
        self.mediator.current_scene = ENTRANCE

        # Action
        self.mediator.handle_edge_transition()

        # Assert
        assert self.mediator.current_scene == ENTRANCE

    def test_handle_edge_transition_missing_rect_returns(self):
        # Setup: player without rect attribute
        self.mediator.player = Mock(spec=[])

        # Action (should not crash)
        self.mediator.handle_edge_transition()

        # Assert: scene unchanged
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
        assert self.mock_player.rect.left == EDGE_MARGIN + FIVE

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
        assert self.mock_player.rect.right == SCREEN_WIDTH - EDGE_MARGIN - FIVE

    def test_take_trolley_wrong_scene_does_not_take(self):
        # Setup
        self.mock_trolley.scene_name = ENTRANCE
        self.mediator.current_scene = YARD
        self.mock_player.rect.colliderect.return_value = True

        # Action
        self.mediator.take_trolley()

        # Assert
        assert self.mock_trolley.taken is False

    def test_take_trolley_correct_scene_takes_it(self):
        # Setup
        self.mock_trolley.scene_name = ENTRANCE
        self.mediator.current_scene = ENTRANCE
        self.mock_player.rect.colliderect.return_value = True
        self.mock_trolley.taken = False

        # Action
        self.mediator.take_trolley()

        # Assert
        assert self.mock_trolley.taken is True

    def test_take_trolley_already_taken_does_nothing(self):
        # Setup
        self.mock_trolley.scene_name = ENTRANCE
        self.mediator.current_scene = ENTRANCE
        self.mock_player.rect.colliderect.return_value = True
        self.mock_trolley.taken = True

        # Action
        self.mediator.take_trolley()

        # Assert
        assert self.mock_trolley.taken is True

    def test_move_trolley_returns_position_if_taken(self):
        # Setup
        self.mock_trolley.taken = True
        self.mock_player.rect.centerx = 100
        self.mock_player.rect.bottom = 200

        # Action
        pos = self.mediator.move_trolley()

        # Assert
        from utils.constants import TROLLEY_X
        assert pos == (100 + TROLLEY_X, 200)

    def test_move_trolley_returns_none_if_not_taken(self):
        # Setup
        self.mock_trolley.taken = False

        # Action
        pos = self.mediator.move_trolley()

        # Assert
        assert pos is None
