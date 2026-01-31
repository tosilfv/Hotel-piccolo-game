"""
Player character implementation for the Piccolo game.
"""
import os
from control.mediator import Mediator
from game_objects.screen import Screen
from utils.commands import Command
from utils.constants import (FIVE, GRAPHICS_PATH, GRAVITY, GROUND_LEVEL,
                            JUMP_CEILING_Y, JUMP_HEIGHT, PLAYER_X,
                            RUN_ANIM_SPEED, ZERO)
from utils.helpers import load_image


class Player:
    """
    Represents the player character (piccolo) in the game.

    Responsibilities:
        - Handle player movement (left, right, jump) within the game world
        - Apply physics, like gravity and jump ceilings
        - Update internal state based on movement and game rules
        - Draw itself on the screen at the correct position
        - Provide an interface for Mediator to control player actions

    Attributes:
        screen: Screen instance for drawing operations.
        is_jumping (bool): Whether the player is jumping.
        is_left (bool): Whether the player is facing left.
        gravity (int): Current gravity of the game.
        jump_height (int): Current Y jump height of the player.
        jump_ceiling_y (int): Maximum height of the player jump.
        velocity_y (int): Current Y velocity of the player.
        left_stand_image_normal: Surface for standing animation (left-facing) normal size.
        left_running_images (list): List of piccolo running images for animation (left-facing) normal size.
        stand_image_normal: Surface for standing animation (right-facing) normal size.
        running_images (list): List of piccolo running images for animation (right-facing) normal size.
        running_frame (int): The frame which is either 0 or 1 for running_images list.
        image: Currently active image surface.
        rect: Pygame rect object for collision detection and determining where the image will be drawn.
    """

    def __init__(self, screen: Screen, mediator: Mediator | None):
        self.screen = screen
        self.mediator = mediator
        self.is_jumping = False
        self.is_left = False
        self.gravity = GRAVITY
        self.jump_height = JUMP_HEIGHT
        self.jump_ceiling_y = JUMP_CEILING_Y
        self.velocity_y = ZERO

        # Normal (left-facing) images
        self.left_stand_image_normal = load_image(
            os.path.join(GRAPHICS_PATH,
                "player",
                "piccolo_left_stand_normal.png"))
        self.left_running_images = [
            load_image(
                os.path.join(GRAPHICS_PATH,
                    "player",
                    "piccolo_left_run1_normal.png")),
            load_image(
                os.path.join(GRAPHICS_PATH,
                    "player",
                    "piccolo_left_run2_normal.png"))
        ]

        # Normal (right-facing) images
        self.stand_image_normal = load_image(
            os.path.join(GRAPHICS_PATH,
                "player",
                "piccolo_stand_normal.png"))
        self.running_images = [
            load_image(
                os.path.join(GRAPHICS_PATH,
                    "player",
                    "piccolo_run1_normal.png")),
            load_image(
                os.path.join(GRAPHICS_PATH,
                    "player",
                    "piccolo_run2_normal.png"))
        ]

        # Set running frame
        self.running_frame = 0

        # Set initial surface (using normal size by default)
        self.image = self.stand_image_normal

        # Set initial rectangle object over surface and place it from midbottom
        self.rect = self.image.get_rect(midbottom = (PLAYER_X, GROUND_LEVEL))

        # Make sure piccolo stands initially at ground level
        self.rect.y = GROUND_LEVEL

    def move_left(self) -> None:
        """
        Set is_left to True.
        Move the player to the left.
        """
        self.is_left = True
        self.rect.x -= FIVE

    def move_right(self) -> None:
        """
        Set is_left to False.        
        Move the player to the right.
        """
        self.is_left = False
        self.rect.x += FIVE

    def jump(self) -> None:
        """
        Start player jump.
        """
        if not self.is_jumping:
            self.is_jumping = True

            # Start jump
            self.velocity_y = self.jump_height

            # Request mediator to play jump sound, only if mediator exists
            if self.mediator is not None:
                self.mediator.handle_command(Command.PLAY_JUMP_SOUND)

    def update(self, running: bool) -> None:
        """
        Update player physics on every frame.
        """
        # Jumping
        if self.is_jumping:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y

            # Prevent piccolo from going over maximum height
            if self.rect.y <= self.jump_ceiling_y:
                self.rect.y = self.jump_ceiling_y
                self.velocity_y = 0

        # Descending
        if self.rect.y >= GROUND_LEVEL:
            self.rect.y = GROUND_LEVEL
            self.is_jumping = False
            self.velocity_y = 0

        # Running
        if running:
            # Update running frame
            self.running_frame += 1
            # If left
            if self.is_left:
                # Slow down image change frequency by multiplying
                if self.running_frame >= len(self.left_running_images) * RUN_ANIM_SPEED:
                    # Reset running frame when all images have been cycled through
                    self.running_frame = 0
                # Avoid list index out of range by dividing the frame index
                self.image = self.left_running_images[self.running_frame // RUN_ANIM_SPEED]
            else:
                if self.running_frame >= len(self.running_images) * RUN_ANIM_SPEED:
                    self.running_frame = 0
                self.image = self.running_images[self.running_frame // RUN_ANIM_SPEED]

        # Standing
        else:
            # If left
            if self.is_left:
                # Use standing image when not running
                self.image = self.left_stand_image_normal
            else:
                self.image = self.stand_image_normal

        # DEBUG
        # print(f"Position: {self.rect.y}, Velocity: {self.velocity_y}, Jumping: {self.is_jumping}, , Running: {running}")

    def draw(self) -> None:
        """
        Draw the player to the screen.
        """
        self.screen.screen.blit(self.image, self.rect)
