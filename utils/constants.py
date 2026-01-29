"""
Game constants and configuration values.
"""
import os

# Numeric
FIVE = 5
TEN = 10
ZERO = 0

# Background
ENTRANCE = "entrance"
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
SOUNDS_PATH = os.path.join(
                os.path.dirname(
                    os.path.dirname(
                        __file__)),
                            "media",
                                "audio")
YARD = "yard"

# Configuration
MUSIC_YARD = "music_yard.wav"
SOUND_JUMP = "sound_jump.wav"
WHITE = (255, 255, 255)

# Default
DEFAULT_FONT_SIZE = 14
DEFAULT_SURFACE_COLOR = (255, 0, 0)  # Red
DEFAULT_SURFACE_SIZE = (100, 100)
DEFAULT_TEXT_SURFACE_SIZE = (10, 10)

# Display
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 800
CAPTION = "Piccolo"
DISPLAY_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
EDGE_MARGIN = TEN
FRAMERATE = 60
SCREEN_LEFT = 0

# Player
GRAVITY = 1
JUMP_HEIGHT = -10
JUMP_CEILING_Y = 200
PLAYER_X = 100
