"""Unit tests for InputHandler class"""
import pygame
from control.input_handler import InputHandler
from utils.constants import (CMD_JUMP, CMD_MOVE_LEFT, CMD_MOVE_RIGHT)
from unittest.mock import Mock, patch

class TestInputHandler:
    """Test InputHandler class"""

    def test_left_key_triggers_left_command(self):
        """Test left key triggers left command method"""
        mediator = Mock()
        handler = InputHandler(mediator)

        with patch('pygame.key.get_pressed') as mock_keys:
            mock_keys.return_value = {pygame.K_LEFT: True, pygame.K_RIGHT: False, pygame.K_SPACE: False}
            handler.process_input()

        mediator.handle_command.assert_called_once_with(CMD_MOVE_LEFT)

    def test_right_key_triggers_left_command(self):
        """Test right key triggers right command method"""
        mediator = Mock()
        handler = InputHandler(mediator)

        with patch('pygame.key.get_pressed') as mock_keys:
            mock_keys.return_value = {pygame.K_LEFT: False, pygame.K_RIGHT: True, pygame.K_SPACE: False}
            handler.process_input()
        
        mediator.handle_command.assert_called_once_with(CMD_MOVE_RIGHT)

    def test_space_key_triggers_jump_command(self):
        """Test space key triggers jump command"""
        mediator = Mock()
        handler = InputHandler(mediator)

        with patch('pygame.key.get_pressed') as mock_keys:
            mock_keys.return_value = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: True}
            handler.process_input()
        
        mediator.handle_command.assert_called_once_with(CMD_JUMP)


    def test_no_keys_triggers_no_command(self):
        """Test no keys triggers no command method"""
        mediator = Mock()
        handler = InputHandler(mediator)

        with patch('pygame.key.get_pressed') as mock_keys:
            mock_keys.return_value = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: False}
            handler.process_input()
        
        mediator.handle_command.assert_not_called()
