"""
Mediator pattern implementation for game object communication.
"""
from utils.commands import Command
from utils.constants import (EDGE_MARGIN, ENTRANCE, MUSIC_YARD, SCREEN_WIDTH,
                             SOUND_JUMP, YARD)


class Mediator:
    """
    Central communication hub for game objects.

    Responsibilities:
        - Route player input commands to the appropriate game object methods
        - Manage scene transitions and update the current scene
        - Updata running state of the player
        - Communicate with AudioManager to play or stop music or sound
        - Ensure decoupling of input handling from game object behavior

    Attributes:
        background: Background instance.
        running (bool): Whether player (piccolo) is running.
        current_scene (str): Current background that is displayed on screen.
        player: Player instance for character management.
        audio_manager: AudioManager instance for audio management.
        _commands (dict): Dictionary for player methods.
    """

    def __init__(self, background, player, audio_manager):
        self.background = background
        self.running = False
        self.current_scene = ENTRANCE
        self.player = player
        self.audio_manager = audio_manager
        self._commands = {
            Command.CHANGE_TO_ENTRANCE: self.change_to_entrance,
            Command.CHANGE_TO_YARD: self.change_to_yard,
            Command.JUMP: self.player.jump,
            Command.MOVE_LEFT: self.player.move_left,
            Command.MOVE_RIGHT: self.player.move_right,
            Command.PLAY_JUMP_SOUND: self.play_jump_sound
        }

    def change_to_entrance(self) -> None:
        """
        Changes background to entrance scene.
        """
        # If player is already at entrance scene then return
        if self.current_scene == ENTRANCE:
            return

        # Set and change current scene and background to entrance
        self.current_scene = ENTRANCE
        self.background.change_background(ENTRANCE)
        self.audio_manager.stop_music()

    def change_to_yard(self) -> None:
        """
        Changes background to yard scene.
        """
        # If player is already at yard scene then return
        if self.current_scene == YARD:
            return

        # Set and change current scene and background to yard
        self.current_scene = YARD
        self.background.change_background(YARD)
        self.audio_manager.play_music(MUSIC_YARD)

    def play_jump_sound(self) -> None:
        """
        Plays jump sound.
        """
        self.audio_manager.play_sound(SOUND_JUMP)

    def handle_command(self, command: Command | None) -> None:
        """
        Handle command communication of game objects.

        Args:
            command (Command): Enum key for _commands dictionary.

        Attributes:
            action: _commands dictionary value that is a player method.
        """
        # Handle unknown command
        if command is None:
            self.running = False
            return

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

    def handle_edge_transition(self) -> None:
        """
        Handle transition when player reaches screen edge.
        """
        # For tests player object can be a Mock object that doesn't have a rect attribute
        try:
            left = self.player.rect.left
            right = self.player.rect.right
        except AttributeError:
            return

        # Prevent exploding in weird circumstances
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            return
        
        # Set constants
        screen_width = SCREEN_WIDTH

        # Set left and right edge values and save current scene
        at_left_edge = (left <= EDGE_MARGIN)
        at_right_edge = (right >= screen_width - EDGE_MARGIN)

        # Handle the transition when player exits scene to left
        if at_left_edge:
            self._scene_transition(spawn_on_left=False, screen_width=screen_width, margin=EDGE_MARGIN)

        # Handle the transition when player exits scene to right
        elif at_right_edge:
            self._scene_transition(spawn_on_left=True, screen_width=screen_width, margin=EDGE_MARGIN)

    def _scene_transition(self, *, spawn_on_left: bool, screen_width: int, margin: int) -> None:
        """
        Handle scene transition and player spawning and call mediator for scene change.

        Args:
            *: Forces following attributes to be called with their name included.
            spawn_on_left (bool): Whether player is going to spawn to left.
            screen_width (int): The screen width.
            margin (int): The margin between player and screen edge.
        """
        # Change scene using mediator commands
        if self.current_scene == ENTRANCE:
            self.handle_command(Command.CHANGE_TO_YARD)
        elif self.current_scene == YARD:
            self.handle_command(Command.CHANGE_TO_ENTRANCE)
        else:
            return

        # Spawn player
        if spawn_on_left:
            self.player.rect.left = margin
        else:
            self.player.rect.right = screen_width - margin
