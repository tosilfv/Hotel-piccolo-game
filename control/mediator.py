"""
Mediator pattern implementation for game object communication.
"""
from utils.constants import (CMD_JUMP, CMD_MOVE_LEFT, CMD_MOVE_RIGHT)

# Mediator
class Mediator:
    """
    Central communication hub for game objects.

    Attributes:
        player: Player instance for character management.
    """
    def __init__(self, player) -> None:
        self.player = player
        self._commands = {
            CMD_JUMP: self.player.jump,
            CMD_MOVE_LEFT: self.player.move_left,
            CMD_MOVE_RIGHT: self.player.move_right
        }

    def handle_command(self, command: str) -> None:
        """
        Handle command communication of game objects.
        """
        action = self._commands.get(command)
        if action:
            action()
