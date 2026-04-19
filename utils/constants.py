"""
Game constants and configuration values.
"""
import os

# Numeric
FIVE = 5
TEN = 10
ZERO = 0

# Background
GRAPHICS_PATH = os.path.join(
                    os.path.dirname(
                        os.path.dirname(
                            __file__)),
                                "media",
                                    "graphics")
GROUND_LEVEL = 324
GROUND_X = ZERO
GROUND_Y = GROUND_LEVEL - 4
SKY_X = ZERO
SKY_Y = -110

# Configuration
RUN_ANIM_SPEED = TEN
SOUND_VOLUME = 0.3
WHITE = (255, 255, 255)

# Default
DEFAULT_FONT_SIZE = 14
DEFAULT_SURFACE_COLOR = (255, 0, 0)  # Red
DEFAULT_SURFACE_SIZE = (100, 100)
DEFAULT_TEXT_SURFACE_SIZE = (TEN, TEN)

# Display
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 800
CAPTION = "Piccolo"
DISPLAY_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
EDGE_MARGIN = TEN
FRAMERATE = 60
SCREEN_LEFT = 0

# Sound
MUSIC_YARD = "music_yard.wav"
SOUND_JUMP = "sound_jump.wav"
SOUNDS_PATH = os.path.join(
                os.path.dirname(
                    os.path.dirname(
                        __file__)),
                            "media",
                                "audio")

# Scene
ENTRANCE = "entrance"
RECEPTION = "reception"
YARD = "yard"

# Player
GRAVITY = 1
JUMP_HEIGHT = -TEN
JUMP_CEILING_Y = 200
PLAYER_X = 100

# Trolley
TROLLEY_X = 50
PUSH_SPEED = FIVE

# Bag
BAG_X = 700
