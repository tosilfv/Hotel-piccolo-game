"""Unit tests for Commands class"""
from utils.commands import Command


class TestCommandEnum:
    """Tests for Commands class"""

    def test_commands_exist(self):
        """Test that all commands exist in Command enum"""
        assert hasattr(Command, "MOVE_LEFT")
        assert hasattr(Command, "MOVE_RIGHT")
        assert hasattr(Command, "JUMP")
        assert hasattr(Command, "STOP")
        assert hasattr(Command, "CHANGE_TO_ENTRANCE")
        assert hasattr(Command, "CHANGE_TO_YARD")

    def test_command_names(self):
        """Test that command names are correct"""
        assert Command.MOVE_LEFT.name == "MOVE_LEFT"
        assert Command.MOVE_RIGHT.name == "MOVE_RIGHT"
        assert Command.JUMP.name == "JUMP"
        assert Command.STOP.name == "STOP"
        assert Command.CHANGE_TO_ENTRANCE.name == "CHANGE_TO_ENTRANCE"
        assert Command.CHANGE_TO_YARD.name == "CHANGE_TO_YARD"

    def test_command_types(self):
        """Test that each command is a Command enum"""
        for cmd in Command:
            assert isinstance(cmd, Command)
