"""Unit tests for constants.py"""
from utils.commands import Command
from utils.constants import (BAG_X, CAPTION, 
                             DEFAULT_FONT_SIZE, DEFAULT_SURFACE_COLOR,
                             DEFAULT_SURFACE_SIZE, DEFAULT_TEXT_SURFACE_SIZE,
                             EDGE_MARGIN, ENTRANCE, DISPLAY_SIZE, FIVE,
                             FRAMERATE, GRAPHICS_PATH, GRAVITY, GROUND_LEVEL,
                             GROUND_X, GROUND_Y, JUMP_HEIGHT, JUMP_CEILING_Y,
                             MUSIC_YARD, PLAYER_X, PUSH_SPEED, RUN_ANIM_SPEED,
                             SCREEN_HEIGHT, SCREEN_LEFT, SCREEN_WIDTH,
                             SOUND_JUMP, SOUNDS_PATH, SOUND_VOLUME, SKY_X,
                             SKY_Y, TEN, TROLLEY_X, WHITE, YARD, ZERO)
import os


class TestConstants:
    """Test constants in the game"""

    def test_numeric_constants(self):
        numeric_constants = {
            FIVE: 5,
            TEN: 10,
            ZERO: 0
        }
        for const, value in numeric_constants.items():
            assert const == value, f"{const} should be {value}"

    def test_background_constants(self):
        # Assert: enum names and background constants are correct
        assert Command.CHANGE_TO_ENTRANCE.name == "CHANGE_TO_ENTRANCE"
        assert Command.CHANGE_TO_YARD.name == "CHANGE_TO_YARD"
        assert ENTRANCE == "entrance"
        assert GRAPHICS_PATH == os.path.join(
                    os.path.dirname(
                        os.path.dirname(
                            __file__)),
                                "media",
                                    "graphics")
        assert GROUND_LEVEL == 324
        assert GROUND_X == 0
        assert GROUND_Y == 320
        assert SKY_X == 0
        assert SKY_Y == -120
        assert SOUNDS_PATH == os.path.join(
                    os.path.dirname(
                        os.path.dirname(
                            __file__)),
                                "media",
                                    "audio")
        assert YARD == "yard"

    def test_configuration_constants(self):
        assert MUSIC_YARD == "music_yard.wav"
        assert RUN_ANIM_SPEED == 10
        assert SOUND_JUMP == "sound_jump.wav"
        assert SOUND_VOLUME == 0.3
        assert WHITE == (255, 255, 255)

    def test_default_constants(self):
        assert DEFAULT_FONT_SIZE == 14
        assert DEFAULT_SURFACE_COLOR == (255, 0, 0)
        assert DEFAULT_SURFACE_SIZE == (100, 100)
        assert DEFAULT_TEXT_SURFACE_SIZE == (10, 10)

    def test_display_constants(self):
        assert SCREEN_HEIGHT == 400
        assert SCREEN_WIDTH == 800
        assert CAPTION == "Piccolo"
        assert DISPLAY_SIZE == (800, 400)
        assert EDGE_MARGIN == 10
        assert FRAMERATE == 60
        assert SCREEN_LEFT == 0

    def test_player_constants(self):
        assert GRAVITY == 1
        assert JUMP_HEIGHT == -10
        assert JUMP_CEILING_Y == 200
        assert PLAYER_X == 100

    def test_trolley_constants(self):
        assert TROLLEY_X == 50
        assert PUSH_SPEED == 5

    def test_bag_constants(self):
        assert BAG_X == 200
