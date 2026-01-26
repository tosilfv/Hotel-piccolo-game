"""Unit tests for Mediator class"""
import pytest
from unittest.mock import MagicMock
from control.mediator import Mediator
from utils.commands import Command
from utils.constants import ENTRANCE, YARD


@pytest.fixture
def mock_player():
    """Mock player object with jump, move_left, move_right methods"""
    player = MagicMock()
    player.jump = MagicMock()
    player.move_left = MagicMock()
    player.move_right = MagicMock()
    return player


@pytest.fixture
def mock_background():
    """Mock background object with change_background method"""
    background = MagicMock()
    background.change_background = MagicMock()
    return background


@pytest.fixture
def mediator(mock_background, mock_player):
    """Mediator instance with mocked dependencies"""
    return Mediator(mock_background, mock_player)


def test_move_commands_call_player(mediator, mock_player):
    """Test that MOVE_LEFT, MOVE_RIGHT, JUMP call correct player methods"""
    mediator.handle_command(Command.MOVE_LEFT)
    mock_player.move_left.assert_called_once()

    mediator.handle_command(Command.MOVE_RIGHT)
    mock_player.move_right.assert_called_once()

    mediator.handle_command(Command.JUMP)
    mock_player.jump.assert_called_once()


def test_change_background_calls_background(mediator, mock_background):
    """Test that CHANGE_TO_ENTRANCE/YARD calls background change correctly"""
    # CHANGE_TO_ENTRANCE
    mediator.current_scene = YARD
    mediator.handle_command(Command.CHANGE_TO_ENTRANCE)
    mock_background.change_background.assert_called_with(ENTRANCE)
    assert mediator.current_scene == ENTRANCE

    # CHANGE_TO_YARD
    mediator.current_scene = ENTRANCE
    mediator.handle_command(Command.CHANGE_TO_YARD)
    mock_background.change_background.assert_called_with(YARD)
    assert mediator.current_scene == YARD


def test_running_state(mediator):
    """Test that running attribute is updated correctly"""
    # Moving left
    mediator.handle_command(Command.MOVE_LEFT)
    assert mediator.running is True

    # Moving right
    mediator.handle_command(Command.MOVE_RIGHT)
    assert mediator.running is True

    # Stop command
    mediator.handle_command(Command.STOP)
    assert mediator.running is False

    # Jump resets running
    mediator.handle_command(Command.JUMP)
    assert mediator.running is False

    # Unknown command also stops running
    mediator.handle_command(None)
    assert mediator.running is False


def test_no_background_change_when_already_in_scene(mediator, mock_background):
    """Test that background doesn't change if already in the scene"""
    mediator.current_scene = ENTRANCE
    mediator.handle_command(Command.CHANGE_TO_ENTRANCE)
    mock_background.change_background.assert_not_called()

    mediator.current_scene = YARD
    mediator.handle_command(Command.CHANGE_TO_YARD)
    mock_background.change_background.assert_not_called()
