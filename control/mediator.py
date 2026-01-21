"""
Mediator pattern implementation for game object communication.
"""
from utils.commands import Command
from utils.constants import (ENTRANCE, YARD)


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
            Command.CHANGE_TO_ENTRANCE: self.change_to_entrance,
            Command.CHANGE_TO_YARD: self.change_to_yard,
            Command.JUMP: self.player.jump,
            Command.MOVE_LEFT: self.player.move_left,
            Command.MOVE_RIGHT: self.player.move_right
        }

    def change_to_entrance(self) -> None:
        """
        Changes background to entrance scene.
        """
        # If player is already at entrance scene then return
        if self.current_scene == ENTRANCE:
            return

        # Set and change current scene and background
        self.current_scene = ENTRANCE
        self.background.change_background(ENTRANCE)

    def change_to_yard(self) -> None:
        """
        Changes background to yard scene.
        """
        # If player is already at yard scene then return
        if self.current_scene == YARD:
            return
        
        # Set and change current scene and background
        self.current_scene = YARD
        self.background.change_background(YARD)

    def handle_command(self, command: Command) -> None:
        """
        Handle command communication of game objects.

        Args:
            command (Command): Enum key for _commands dictionary.
        
        Attributes:
            action: _commands dictionary value that contains a player method.
        """
        # Get the method for the command
        action = self._commands.get(command)

        # Call the method
        if action:
            action()
        
        # Player stops
        if command == Command.STOP:
            self.running = False
            return
        
        # Player is running
        if command == Command.MOVE_LEFT or command == Command.MOVE_RIGHT:
            self.running = True

        # Signature move: Piccolo's legendary two-foot boing 🐸
        else:
            self.running = False
