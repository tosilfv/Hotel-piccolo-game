from unittest.mock import MagicMock
import pytest
from control.mediator import Mediator
from utils.commands import Command
from utils.constants import ENTRANCE, YARD

@pytest.fixture
def mock_player():
    return MagicMock()

@pytest.fixture
def mock_background():
    return MagicMock()

@pytest.fixture
def mediator(mock_background, mock_player):
    return Mediator(mock_background, mock_player)

def test_move_commands_call_player(mediator, mock_player):
    mediator.handle_command(Command.MOVE_LEFT)
    mock_player.move_left.assert_called_once()
    
    mediator.handle_command(Command.MOVE_RIGHT)
    mock_player.move_right.assert_called_once()
    
    mediator.handle_command(Command.JUMP)
    mock_player.jump.assert_called_once()

def test_change_background_calls_background(mediator, mock_background):
    mediator.current_scene = YARD
    mediator.handle_command(Command.CHANGE_TO_ENTRANCE)
    mock_background.change_background.assert_called_once_with(ENTRANCE)

    mediator.current_scene = ENTRANCE
    mediator.handle_command(Command.CHANGE_TO_YARD)
    mock_background.change_background.assert_called_with(YARD)

def test_running_state(mediator):
    mediator.handle_command(Command.MOVE_LEFT)
    assert mediator.running is True

    mediator.handle_command(Command.MOVE_RIGHT)
    assert mediator.running is True

    mediator.handle_command(Command.STOP)
    assert mediator.running is False

    mediator.handle_command(Command.JUMP)  # should reset running
    assert mediator.running is False
