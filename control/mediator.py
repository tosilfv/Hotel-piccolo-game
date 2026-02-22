"""
Mediator pattern implementation for game object communication.
"""
from typing import Tuple
from utils.commands import Command
from utils.constants import (EDGE_MARGIN, ENTRANCE, FIVE, MUSIC_YARD,
                             PUSH_SPEED, SCREEN_WIDTH, SOUND_JUMP, TROLLEY_X,
                             YARD)


class Mediator:
    """
    Central communication hub for game objects.

    Responsibilities:
        - Route player input commands to the appropriate game object methods
        - Manage scene transitions and update the current scene
        - Update running state of the player
        - Communicate with AudioManager to play or stop music or sound
        - Ensure decoupling of input handling from game object behavior

    Attributes:
        background: Background instance.
        running (bool): Whether player (piccolo) is running.
        current_scene (str): Current background that is displayed on screen.
        player: Player instance for character management.
        trolley: Trolley instance for trolley item management.
        audio_manager: AudioManager instance for audio management.
        _commands (dict): Dictionary for player methods.
    """

    def __init__(self, background, player, trolley, audio_manager):
        self.background = background
        self.running = False
        self.current_scene = ENTRANCE
        self.player = player
        self.trolley = trolley
        self.audio_manager = audio_manager
        self._commands = {
            Command.CHANGE_TO_ENTRANCE: (self.change_to_entrance, False),
            Command.CHANGE_TO_YARD: (self.change_to_yard, False),
            Command.JUMP: (self.player.jump, False),
            Command.MOVE_LEFT: (self.player.move_left, True),
            Command.MOVE_RIGHT: (self.player.move_right, True),
            Command.PLAY_JUMP_SOUND: (self.play_jump_sound, False),
            Command.RELEASE_TROLLEY: (self.release_trolley, False),
            Command.TAKE_TROLLEY: (self.take_trolley, True)
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

        # Tell trolley its current scene
        if self.trolley.taken:
            self.trolley.scene_name = self.current_scene

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

        # Tell trolley its current scene
        if self.trolley.taken:
            self.trolley.scene_name = self.current_scene

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

        # Get command_data for action and running_state and return if it evaluates to False
        command_data = self._commands.get(command)
        if not command_data:
            self.running = False
            return

        # Unpack command_data
        action, running_state = command_data

        # Call the action
        action()

        # Update self.running
        self.running = running_state

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
            self.player.rect.left = margin + FIVE
        else:
            self.player.rect.right = screen_width - margin - FIVE

    def take_trolley(self) -> None:
        """
        Handle player taking the trolley.
        """
        if not self._can_interact():
            return

        if not self.trolley:
            return

        # When trolley is not on the same scene where player is, don't take trolley
        if self.current_scene != self.trolley.scene_name:
            return

        # When trolley is not yet taken but player's proximity is close enough to take it
        if self.player.rect.colliderect(self.trolley.rect):
            self.trolley.taken = True

    def move_trolley(self) -> Tuple[int, int] | None:
        """
        Handle player moving the trolley.
        """
        if self.trolley.taken:
            return (self.player.rect.centerx + TROLLEY_X, self.player.rect.bottom)

    def release_trolley(self) -> None:
        """
        Release trolley and give it a small push based on player's facing direction.
        """
        if not self._can_interact():
            return

        if not self.trolley:
            return

        # Can only release if player has it
        if not self.trolley.taken:
            return

        # When trolley is not on the same scene where player is, don't release trolley
        if self.current_scene != self.trolley.scene_name:
            return

        # Release trolley
        self.trolley.taken = False

        # Give push
        is_left = getattr(self.player, "is_left", False)

        # Convert bool to int for trolley speed calculation
        direction = -1 if is_left else 1

        # Add speed to trolley
        self.trolley.speed = direction * PUSH_SPEED

        # DEBUG
        # print(f"Current scene: {self.current_scene}")
        # print(f"Trolley scene: {self.trolley.scene_name}")

    def _can_interact(self) -> bool:
        """
        Guard pattern - Global interaction guard (with expansion example):

        return (
            self.player is not None
            and not getattr(self.player, "is_unable_to_interact_case1", False)
            and not getattr(self.player, "is_unable_to_interact_case2", False)
            and not getattr(self.player, "is_unable_to_interact_case3", False)
            etc...
        )
        """
        return self.player is not None
