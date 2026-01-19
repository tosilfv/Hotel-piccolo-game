"""
Mediator pattern implementation for game object communication.
"""
from utils.constants import (CHANGE_TO_ENTRANCE, CHANGE_TO_YARD, CMD_JUMP,
                             CMD_MOVE_LEFT, CMD_MOVE_RIGHT, ENTRANCE, YARD)


# Mediator
class Mediator:
    """
    Central communication hub for game objects.

    Attributes:
        background: Background instance.
        running (bool): Whether player (piccolo) is running.
        current_scene (str): Current background that is displayed on screen.
        player: Player instance for character management.
        _commands (dict): Dictionary for player methods.
    """
    
    def __init__(self, background, player):
        self.background = background
        self.running = False
        self.current_scene = ENTRANCE
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
        # If player is already at entrance scene then return
        if self.current_scene == ENTRANCE:
            return

        # Set and change current scene and background
        self.current_scene = ENTRANCE
        self.background.change_background(ENTRANCE)
    
    def change_to_yard(self):
        """
        Changes background to yard scene.

        Returns:
            None
        """
        # If player is already at yard scene then return
        if self.current_scene == YARD:
            return
        
        # Set and change current scene and background
        self.current_scene = YARD
        self.background.change_background(YARD)

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
        # Get the method for the command
        action = self._commands.get(command)

        # Call the method
        if action:
            action()
        
        # Player is running
        if command == CMD_MOVE_LEFT or command == CMD_MOVE_RIGHT:
            self.running = True
        else:
            self.running = False
        
        return None
