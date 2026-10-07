"""
Mediator pattern implementation for game object communication.
"""
from utils.commands import Command
from utils.constants import (BALLROOM, BAR, CENTER, CONCIERGE, EDGE_MARGIN,
                             ELEVATOR, ENTRANCE, FIVE, GARAGE, INSIDE_GARAGE,
                             INSIDE_LUGGAGE, INSIDE_STAFF, LUGGAGE, MUSIC_YARD,
                             PUSH_SPEED, RECEPTION, RESTAURANT, SCREEN_WIDTH,
                             SERVICES, SOFAS, SOUND_JUMP, TROLLEY_X, YARD)


class Mediator:
    """
    Central communication hub for game objects.

    Responsibilities:
        - Route player input commands to the appropriate game object methods
        - Manage scene transitions and update the current scene
        - Update running state of the player
        - Communicate with AudioManager to play or stop music or sound
        - Ensure decoupling of input handling from game object behavior
        - Manage trolley actions

    Attributes:
        _current_scene (str): Current scene.
        background: Background instance.
        running (bool): Whether player (piccolo) is running.
        player: Player instance for character management.
        trolley: Trolley instance for trolley item management.
        bag: Bag instance for bag item management.
        audio_manager: AudioManager instance for audio management.
        _commands (dict): Dictionary for command actions.
    """

    def __init__(self, background, player, trolley, bag, audio_manager):
        self._current_scene = ENTRANCE
        self.background = background
        self.running = False
        self.player = player
        self.trolley = trolley
        self.bag = bag
        self.audio_manager = audio_manager
        self._commands = {
            Command.CHANGE_TO_BALLROOM: (self.change_to_ballroom, False),
            Command.CHANGE_TO_BAR: (self.change_to_bar, False),
            Command.CHANGE_TO_CONCIERGE: (self.change_to_concierge, False),
            Command.CHANGE_TO_ELEVATOR: (self.change_to_elevator, False),
            Command.CHANGE_TO_ENTRANCE: (self.change_to_entrance, False),
            Command.CHANGE_TO_GARAGE: (self.change_to_garage, False),
            Command.CHANGE_TO_INSIDE_GARAGE: (self.change_to_inside_garage, False),
            Command.CHANGE_TO_INSIDE_LUGGAGE: (self.change_to_inside_luggage, False),
            Command.CHANGE_TO_INSIDE_STAFF: (self.change_to_inside_staff, False),
            Command.CHANGE_TO_LUGGAGE: (self.change_to_luggage, False),
            Command.CHANGE_TO_RECEPTION: (self.change_to_reception, False),
            Command.CHANGE_TO_RESTAURANT: (self.change_to_restaurant, False),
            Command.CHANGE_TO_SERVICES: (self.change_to_services, False),
            Command.CHANGE_TO_SOFAS: (self.change_to_sofas, False),
            Command.CHANGE_TO_YARD: (self.change_to_yard, False),
            Command.ENTER_DOOR: (self.enter_door, False),
            Command.EXIT_DOOR: (self.exit_door, False),
            Command.JUMP: (self.player.jump, False),
            Command.MOVE_LEFT: (self.player.move_left, True),
            Command.MOVE_RIGHT: (self.player.move_right, True),
            Command.PLAY_JUMP_SOUND: (self.play_jump_sound, False),
            Command.RELEASE_TROLLEY: (self.release_trolley, False),
            Command.TAKE_TROLLEY: (self.take_trolley, True)
        }

    @property
    def current_scene(self) -> str:
        return self._current_scene

    def _change_scene(self, scene: str, music: str | None = None) -> None:
        # Return if already in the target scene
        if self._current_scene == scene:
            return

        # Update current scene and background
        self._current_scene = scene
        self.background.change_background(scene)

        # Update scene music
        if music is not None:
            self.audio_manager.play_music(music)
        else:
            self.audio_manager.stop_music()

        # Update trolley scene if trolley is being pushed
        if self.trolley.taken:
            self.trolley.scene_name = scene

    def change_to_ballroom(self) -> None:
        """
        Changes to ballroom scene.
        """
        self._change_scene(BALLROOM)

    def change_to_bar(self) -> None:
        """
        Changes to bar scene.
        """
        self._change_scene(BAR)

    def change_to_concierge(self) -> None:
        """
        Changes to concierge scene.
        """
        self._change_scene(CONCIERGE)

    def change_to_elevator(self) -> None:
        """
        Changes to elevator scene.
        """
        self._change_scene(ELEVATOR)

    def change_to_entrance(self) -> None:
        """
        Changes to entrance scene.
        """
        self._change_scene(ENTRANCE)

    def change_to_garage(self) -> None:
        """
        Changes to garage scene.
        """
        self._change_scene(GARAGE)

    def change_to_inside_garage(self) -> None:
        """
        Changes to inside garage scene.
        """
        self._change_scene(INSIDE_GARAGE)

    def change_to_inside_luggage(self) -> None:
        """
        Changes to inside luggage scene.
        """
        self._change_scene(INSIDE_LUGGAGE)

    def change_to_inside_staff(self) -> None:
        """
        Changes to inside staff scene.
        """
        self._change_scene(INSIDE_STAFF)

    def change_to_luggage(self) -> None:
        """
        Changes to luggage scene.
        """
        self._change_scene(LUGGAGE)

    def change_to_reception(self) -> None:
        """
        Changes to reception scene.
        """
        self._change_scene(RECEPTION)

    def change_to_restaurant(self) -> None:
        """
        Changes to restaurant scene.
        """
        self._change_scene(RESTAURANT)

    def change_to_services(self) -> None:
        """
        Changes to services scene.
        """
        self._change_scene(SERVICES)

    def change_to_sofas(self) -> None:
        """
        Changes to sofas scene.
        """
        self._change_scene(SOFAS)

    def change_to_yard(self) -> None:
        """
        Changes to yard scene.
        """
        self._change_scene(YARD, MUSIC_YARD)

    def play_jump_sound(self) -> None:
        """
        Play jump sound.
        """
        self.audio_manager.play_sound(SOUND_JUMP)

    def handle_command(self, command: Command | None) -> None:
        """
        Handle command communication of game objects.

        Args:
            command (Command | None): Enum key for _commands dictionary.
        """
        # Handle unknown command
        if command is None:
            self.running = False
            return

        # Get command_data
        command_data = self._commands.get(command)
        if command_data is None:
            self.running = False
            return

        action, running_state = command_data
        action()
        self.running = running_state

    def handle_edge_transition(self) -> None:
        """
        Handle transition when player reaches screen edge.
        """
        # Get player's horizontal position
        left = self.player.rect.left
        right = self.player.rect.right

        # Check if player is at the left or right edge
        at_left_edge = left <= EDGE_MARGIN
        at_right_edge = right >= SCREEN_WIDTH - EDGE_MARGIN

        # Handle the transition when player exits scene to left
        if at_left_edge:
            self._scene_transition(spawn_on_left=False)

        # Handle the transition when player exits scene to right
        elif at_right_edge:
            self._scene_transition(spawn_on_left=True)

    def _scene_transition(self, *, spawn_on_left: bool) -> None:
        """
        Handle scene transition and move player to the opposite edge.

        Args:
            spawn_on_left (bool): Whether player is going to spawn to left.
        """
        # Exit BALLROOM from Left to SERVICES
        if self._current_scene == BALLROOM and not spawn_on_left:
            self.handle_command(Command.CHANGE_TO_SERVICES)
        # Exit BALLROOM from Right to GARAGE
        elif self._current_scene == BALLROOM and spawn_on_left:
            self.handle_command(Command.CHANGE_TO_GARAGE)
        # Exit BAR from Left to ELEVATOR
        elif self._current_scene == BAR and not spawn_on_left:
            self.handle_command(Command.CHANGE_TO_ELEVATOR)
        # Exit BAR from Right to RESTAURANT
        elif self._current_scene == BAR and spawn_on_left:
            self.handle_command(Command.CHANGE_TO_RESTAURANT)
        # Exit CONCIERGE from Left to RESTAURANT
        elif self._current_scene == CONCIERGE and not spawn_on_left:
            self.handle_command(Command.CHANGE_TO_RESTAURANT)
        # Exit CONCIERGE from Right to SERVICES
        elif self._current_scene == CONCIERGE and spawn_on_left:
            self.handle_command(Command.CHANGE_TO_SERVICES)
        # Exit ELEVATOR from Left to RECEPTION
        elif self._current_scene == ELEVATOR and not spawn_on_left:
            self.handle_command(Command.CHANGE_TO_RECEPTION)
        # Exit ELEVATOR from Right to BAR
        elif self._current_scene == ELEVATOR and spawn_on_left:
            self.handle_command(Command.CHANGE_TO_BAR)
        # Exit ENTRANCE from Left or Right to YARD
        elif self._current_scene == ENTRANCE:
            self.handle_command(Command.CHANGE_TO_YARD)
        # Exit GARAGE from Left to BALLROOM
        elif self._current_scene == GARAGE and not spawn_on_left:
            self.handle_command(Command.CHANGE_TO_BALLROOM)
        # Exit GARAGE from Right to LUGGAGE
        elif self._current_scene == GARAGE and spawn_on_left:
            self.handle_command(Command.CHANGE_TO_LUGGAGE)
        # Exit LUGGAGE from Left to GARAGE
        elif self._current_scene == LUGGAGE and not spawn_on_left:
            self.handle_command(Command.CHANGE_TO_GARAGE)
        # Exit LUGGAGE from Right to SOFAS
        elif self._current_scene == LUGGAGE and spawn_on_left:
            self.handle_command(Command.CHANGE_TO_SOFAS)
        # Exit RECEPTION from Left to SOFAS
        elif self._current_scene == RECEPTION and not spawn_on_left:
            self.handle_command(Command.CHANGE_TO_SOFAS)
        # Exit RECEPTION from Right to ELEVATOR
        elif self._current_scene == RECEPTION and spawn_on_left:
            self.handle_command(Command.CHANGE_TO_ELEVATOR)
        # Exit RESTAURANT from Left to BAR
        elif self._current_scene == RESTAURANT and not spawn_on_left:
            self.handle_command(Command.CHANGE_TO_BAR)
        # Exit RESTAURANT from Right to CONCIERGE
        elif self._current_scene == RESTAURANT and spawn_on_left:
            self.handle_command(Command.CHANGE_TO_CONCIERGE)
        # Exit SERVICES from Left to CONCIERGE
        elif self._current_scene == SERVICES and not spawn_on_left:
            self.handle_command(Command.CHANGE_TO_CONCIERGE)
        # Exit SERVICES from Right to BALLROOM
        elif self._current_scene == SERVICES and spawn_on_left:
            self.handle_command(Command.CHANGE_TO_BALLROOM)
        # Exit SOFAS from Left to LUGGAGE
        elif self._current_scene == SOFAS and not spawn_on_left:
            self.handle_command(Command.CHANGE_TO_LUGGAGE)
        # Exit SOFAS from Right to RECEPTION
        elif self._current_scene == SOFAS and spawn_on_left:
            self.handle_command(Command.CHANGE_TO_RECEPTION)
        # Exit YARD from Left or Right to ENTRANCE
        elif self._current_scene == YARD:
            self.handle_command(Command.CHANGE_TO_ENTRANCE)
        else:
            return

        # Move player to the opposite edge
        if spawn_on_left:
            self.player.rect.left = EDGE_MARGIN + FIVE
        else:
            self.player.rect.right = SCREEN_WIDTH - EDGE_MARGIN - FIVE

    def enter_door(self) -> None:
        """
        Enter the room when player is at the door and presses up.
        """
        if self._current_scene not in (
            GARAGE,
            ENTRANCE,
            LUGGAGE
        ):
            return

        # Get player's horizontal position
        left = self.player.rect.left

        # Check if player is within the door interaction area
        door_min_x = 230
        door_max_x = 460
        within_door_range = door_min_x <= left <= door_max_x

        if not within_door_range:
            return

        if self._current_scene == ENTRANCE:
            self.handle_command(Command.CHANGE_TO_RECEPTION)
        elif self._current_scene == GARAGE:
            self.handle_command(Command.CHANGE_TO_INSIDE_GARAGE)
        elif self._current_scene == LUGGAGE:
            self.handle_command(Command.CHANGE_TO_INSIDE_LUGGAGE)

        # Move player to the center of the room
        self.player.rect.left = CENTER

    def exit_door(self) -> None:
        """
        Exit the room when player is at the door and presses down.
        """
        if self._current_scene not in (
            INSIDE_GARAGE,
            INSIDE_LUGGAGE,
            RECEPTION
        ):
            return

        # Get player's horizontal position
        left = self.player.rect.left

        # Check if player is within the door interaction area
        door_min_x = 230
        door_max_x = 460
        within_door_range = door_min_x <= left <= door_max_x

        if not within_door_range:
            return

        if self._current_scene == INSIDE_GARAGE:
            self.handle_command(Command.CHANGE_TO_GARAGE)
        elif self._current_scene == INSIDE_LUGGAGE:
            self.handle_command(Command.CHANGE_TO_LUGGAGE)
        elif self._current_scene == RECEPTION:
            self.handle_command(Command.CHANGE_TO_ENTRANCE)

        # Move player to the center of the room
        self.player.rect.left = CENTER

    def take_trolley(self) -> None:
        """
        Handle player taking the trolley.
        """
        # Trolley must be in the same scene as the player
        if self._current_scene != self.trolley.scene_name:
            return

        # Take trolley when player touches it
        if self.player.rect.colliderect(self.trolley.rect):
            self.trolley.taken = True

    def move_trolley(self) -> tuple[int, int] | None:
        """
        Handle player moving the trolley.
        """
        if self.trolley.taken:
            return self.player.rect.centerx + TROLLEY_X, self.player.rect.bottom

    def release_trolley(self) -> None:
        """
        Release trolley and give it a small push based on player's facing direction.
        """
        # Can only release if player has it
        if not self.trolley.taken:
            return

        # Trolley must be in the same scene as the player
        if self._current_scene != self.trolley.scene_name:
            return

        # Release trolley
        self.trolley.taken = False

        # Push trolley in the direction the player is facing
        is_left = self.player.is_left

        # Set push direction based on player facing direction
        direction = -1 if is_left else 1

        self.trolley.speed = direction * PUSH_SPEED
