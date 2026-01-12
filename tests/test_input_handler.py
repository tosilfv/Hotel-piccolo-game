import pygame
from control.input_handler import InputHandler
from utils.constants import CMD_MOVE_LEFT, CMD_MOVE_RIGHT
from unittest.mock import Mock, patch

class TestInputHandler:

    def test_left_key_triggers_left_command(self):
        mediator = Mock()
        handler = InputHandler(mediator)

        with patch('pygame.key.get_pressed') as mock_keys:
            mock_keys.return_value = {pygame.K_LEFT: True, pygame.K_RIGHT: False}
            handler.process_input()

        mediator.handle_command.assert_called_once_with(CMD_MOVE_LEFT)
