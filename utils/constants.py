"""
Game constants and configuration values.
"""
import os

# Numeric
FIVE = 5
ZERO = 0

# Background
GRAPHICS_PATH = os.path.join(
                    os.path.dirname(
                        os.path.dirname(
                            __file__)),
                                "media",
                                    "graphics")
GROUND_LEVEL = 240
GROUND_X = ZERO
GROUND_Y = 320
SKY_X = ZERO
SKY_Y = -120

# Default
DEFAULT_FONT_SIZE = 14
DEFAULT_SURFACE_COLOR = (255, 0, 0)  # Red
DEFAULT_SURFACE_SIZE = (100, 100)
DEFAULT_TEXT_SURFACE_SIZE = (10, 10)

# Display
CAPTION = "Piccolo"
DISPLAY_SIZE = (800, 400)
FRAMERATE = 60

# Input
CMD_JUMP = "JUMP"
CMD_MOVE_LEFT = "MOVE_LEFT"
CMD_MOVE_RIGHT = "MOVE_RIGHT"

# Player
GRAVITY = 1
JUMP_HEIGHT = -15
JUMP_CEILING_Y = 200
PLAYER_X = 100

# Utils
WHITE = (255, 255, 255)
