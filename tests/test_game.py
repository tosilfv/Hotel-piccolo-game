"""Unit tests for Game class"""
from unittest.mock import Mock, patch
from control.game import Game
from utils.commands import Command
from utils.constants import ENTRANCE, YARD, SCREEN_WIDTH, EDGE_MARGIN


class TestGame:
    def setup_method(self):
        # Setup mocks
        self.screen = Mock()
        self.screen.clock = Mock()
        self.screen.framerate = 60

        self.background = Mock()
        self.player = Mock()
        self.player.rect = Mock()
        self.mediator = Mock()
        self.input_handler = Mock()

        self.game = Game(
            screen=self.screen,
            background=self.background,
            player=self.player,
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
        self.player.update.assert_called_once_with(self.mediator.running)
        mock_update.assert_called_once()
        self.screen.clock.tick.assert_called_once_with(self.screen.framerate)

    def test_handle_edge_transition_left(self):
        # Setup
        self.player.rect.left = EDGE_MARGIN - 1
        self.player.rect.right = 50
        self.mediator.current_scene = ENTRANCE

        # Action
        self.game._handle_edge_transition()

        # Assert
        self.mediator.handle_command.assert_called_once_with(Command.CHANGE_TO_YARD)
        assert self.player.rect.right == SCREEN_WIDTH - EDGE_MARGIN

    def test_handle_edge_transition_right(self):
        # Setup
        self.player.rect.left = SCREEN_WIDTH - EDGE_MARGIN + 1
        self.player.rect.right = SCREEN_WIDTH
        self.mediator.current_scene = YARD

        # Action
        self.game._handle_edge_transition()

        # Assert
        self.mediator.handle_command.assert_called_once_with(Command.CHANGE_TO_ENTRANCE)
        assert self.player.rect.left == EDGE_MARGIN

    def test_handle_edge_transition_middle_no_change(self):
        # Setup
        self.player.rect.left = 100
        self.player.rect.right = 150
        self.mediator.current_scene = ENTRANCE

        # Action
        self.game._handle_edge_transition()

        # Assert
        self.mediator.handle_command.assert_not_called()

    def test_scene_transition_spawn_left(self):
        # Setup
        self.mediator.current_scene = YARD

        # Action
        self.game._scene_transition(spawn_on_left=True, screen_width=SCREEN_WIDTH, margin=EDGE_MARGIN)

        # Assert
        self.mediator.handle_command.assert_called_once_with(Command.CHANGE_TO_ENTRANCE)
        assert self.player.rect.left == EDGE_MARGIN

    def test_scene_transition_spawn_right(self):
        # Setup
        self.mediator.current_scene = ENTRANCE

        # Action
        self.game._scene_transition(spawn_on_left=False, screen_width=SCREEN_WIDTH, margin=EDGE_MARGIN)

        # Assert
        self.mediator.handle_command.assert_called_once_with(Command.CHANGE_TO_YARD)
        assert self.player.rect.right == SCREEN_WIDTH - EDGE_MARGIN
