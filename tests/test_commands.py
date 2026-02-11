"""Unit tests for Commands class"""
from utils.commands import Command


class TestCommandEnum:
    """Tests Commands class"""

    def test_commands_exist(self):
        # Assert: all commands exist
        assert hasattr(Command, "CHANGE_TO_ENTRANCE")
        assert hasattr(Command, "CHANGE_TO_YARD")
        assert hasattr(Command, "JUMP")
        assert hasattr(Command, "MOVE_LEFT")
        assert hasattr(Command, "MOVE_RIGHT")
        assert hasattr(Command, "PLAY_JUMP_SOUND")
        assert hasattr(Command, "STOP")
        assert hasattr(Command, "TAKE_TROLLEY")

    def test_command_names(self):
        # Assert: all names are correct
        assert Command.CHANGE_TO_ENTRANCE.name == "CHANGE_TO_ENTRANCE"
        assert Command.CHANGE_TO_YARD.name == "CHANGE_TO_YARD"
        assert Command.JUMP.name == "JUMP"
        assert Command.MOVE_LEFT.name == "MOVE_LEFT"
        assert Command.MOVE_RIGHT.name == "MOVE_RIGHT"
        assert Command.PLAY_JUMP_SOUND.name == "PLAY_JUMP_SOUND"
        assert Command.STOP.name == "STOP"
        assert Command.TAKE_TROLLEY.name == "TAKE_TROLLEY"

    def test_command_types(self):
        # Assert: each command is of Command type
        for cmd in Command:
            assert isinstance(cmd, Command)

    def test_command_values_unique(self):
        # Assert: all enum values are unique
        values = [cmd.value for cmd in Command]
        assert len(values) == len(set(values)), "Enum values are not unique"
