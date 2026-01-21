"""Unit tests for constants.py"""
from utils.constants import (CAPTION, CHANGE_TO_ENTRANCE, CHANGE_TO_YARD,
                             DEFAULT_FONT_SIZE, DEFAULT_SURFACE_COLOR,
                             DEFAULT_SURFACE_SIZE, DEFAULT_TEXT_SURFACE_SIZE,
                             ENTRANCE, DISPLAY_SIZE, FIVE, FRAMERATE,
                             GRAPHICS_PATH, GRAVITY, GROUND_LEVEL, GROUND_X,
                             GROUND_Y, JUMP_HEIGHT, JUMP_CEILING_Y, PLAYER_X,
                             SCREEN_HEIGHT, SCREEN_LEFT, SCREEN_WIDTH, SKY_X,
                             SKY_Y, TEN, WHITE, YARD, ZERO)


class TestConstants:
    """Test constants values"""

    def test_numeric_constants(self):
        """Test numeric constants"""
        assert FIVE == 5
        assert TEN == 10
        assert ZERO == 0

    def test_background_constants(self):
        """Test background constants"""
        import os
        assert CHANGE_TO_ENTRANCE == "CHANGE_TO_ENTRANCE"
        assert CHANGE_TO_YARD == "CHANGE_TO_YARD"
        assert ENTRANCE == "entrance"
        assert GRAPHICS_PATH == os.path.join(
                    os.path.dirname(
                        os.path.dirname(
                            __file__)),
                                "media",
                                    "graphics")
        assert GROUND_LEVEL == 240
        assert GROUND_X == 0
        assert GROUND_Y == 320
        assert SKY_X == 0
        assert SKY_Y == -120
        assert YARD == "yard"

    def test_configuration_constants(self):
        """Test configuration constants"""
        assert WHITE == (255, 255, 255)

    def test_default_constants(self):
        """Test default constants"""
        assert DEFAULT_FONT_SIZE == 14
        assert DEFAULT_SURFACE_COLOR == (255, 0, 0)
        assert DEFAULT_SURFACE_SIZE == (100, 100)
        assert DEFAULT_TEXT_SURFACE_SIZE == (10, 10)

    def test_display_constants(self):
        """Test display constants"""
        assert SCREEN_HEIGHT == 400
        assert SCREEN_WIDTH == 800
        assert CAPTION == "Piccolo"
        assert DISPLAY_SIZE == (800, 400)
        assert FRAMERATE == 60
        assert SCREEN_LEFT == 0

    def test_player_constants(self):
        """Test player constants"""
        assert GRAVITY == 1
        assert JUMP_HEIGHT == -10
        assert JUMP_CEILING_Y == 200
        assert PLAYER_X == 100
