"""Unit tests for InputHandler class"""
import pygame
from unittest.mock import Mock, patch
from control.input_handler import InputHandler
from utils.commands import Command


class TestInputHandler:
    """Test InputHandler class"""

    def setup_method(self):
        # Setup
        self.mediator = Mock()
        self.input_handler = InputHandler(self.mediator)

    def test_left_key_triggers_left_command(self):
        # Setup
        with patch('pygame.key.get_pressed') as mock_keys:
            mock_keys.return_value = {pygame.K_LEFT: True, pygame.K_RIGHT: False, pygame.K_SPACE: False, pygame.K_RETURN: False}

            # Action
            self.input_handler.process_input()

            # Assert
            self.mediator.handle_command.assert_called_once_with(Command.MOVE_LEFT)

    def test_right_key_triggers_right_command(self):
        # Setup
        with patch('pygame.key.get_pressed') as mock_keys:
            mock_keys.return_value = {pygame.K_LEFT: False, pygame.K_RIGHT: True, pygame.K_SPACE: False, pygame.K_RETURN: False}

            # Action
            self.input_handler.process_input()

            # Assert
            self.mediator.handle_command.assert_called_once_with(Command.MOVE_RIGHT)

    def test_space_key_triggers_jump_command(self):
        # Setup
        with patch('pygame.key.get_pressed') as mock_keys:
            mock_keys.return_value = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: True, pygame.K_RETURN: False}

            # Action
            self.input_handler.process_input()

            # Assert
            self.mediator.handle_command.assert_called_once_with(Command.JUMP)

    def test_return_key_triggers_take_trolley_command(self):
        # Setup
        with patch('pygame.key.get_pressed') as mock_keys:
            mock_keys.return_value = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: False, pygame.K_RETURN: True}

            # Action
            self.input_handler.process_input()

            # Assert
            self.mediator.handle_command.assert_called_once_with(Command.TAKE_TROLLEY)

    def test_no_keys_triggers_no_command(self):
        # Setup
        with patch('pygame.key.get_pressed') as mock_keys:
            mock_keys.return_value = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: False, pygame.K_RETURN: False}

            # Action
            self.input_handler.process_input()

            # Assert
            self.mediator.handle_command.assert_not_called()
