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
        _commands (dict): Dictionary for player methods.
    """
    
    def __init__(self, player):
        self.player = player
        self._commands = {
            CMD_JUMP: self.player.jump,
            CMD_MOVE_LEFT: self.player.move_left,
            CMD_MOVE_RIGHT: self.player.move_right
        }

    def handle_command(self, command: str) -> None:
        """
        Handle command communication of game objects.

        Args:
            command (str): command key for _commands dictionary.
        
        Attributes:
            action: _commands dictionary value that contains a player method.
        
        Returns:
            None
        """
        action = self._commands.get(command)
        if action:
            action()
        
        return None
