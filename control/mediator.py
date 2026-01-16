"""
Mediator pattern implementation for game object communication.
"""
from utils.constants import (CHANGE_TO_ENTRANCE, CHANGE_TO_YARD, CMD_JUMP,
                             CMD_MOVE_LEFT, CMD_MOVE_RIGHT)


# Mediator
class Mediator:
    """
    Central communication hub for game objects.

    Attributes:
        player: Player instance for character management.
        _commands (dict): Dictionary for player methods.
    """
    
    def __init__(self, background, player):
        self.background = background
        self.current_scene = "entrance"
        self.player = player
        self._commands = {
            CHANGE_TO_ENTRANCE: self.change_to_entrance,
            CHANGE_TO_YARD: self.change_to_yard,
            CMD_JUMP: self.player.jump,
            CMD_MOVE_LEFT: self.player.move_left,
            CMD_MOVE_RIGHT: self.player.move_right
        }
    
    def change_to_entrance(self) -> None:
        """
        Changes background to entrance scene.

        Returns:
            None
        """
        if self.current_scene == "entrance": return

        self.current_scene = "entrance"
        self.background.change_background("entrance")
    
    def change_to_yard(self):
        """
        Changes background to yard scene.

        Returns:
            None
        """
        if self.current_scene == "yard": return
        
        self.current_scene = "yard"
        self.background.change_background("yard")

    def handle_command(self, command: str) -> None:
        """
        Handle command communication of game objects.

        Args:
            command (str): key for _commands dictionary.
        
        Attributes:
            action: _commands dictionary value that contains a player method.
        
        Returns:
            None
        """
        action = self._commands.get(command)
        if action:
            action()
        
        return None
