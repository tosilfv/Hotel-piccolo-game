"""Unit tests for constants.py"""
from utils.constants import (CAPTION, CMD_JUMP, CMD_MOVE_LEFT, CMD_MOVE_RIGHT,
                             DEFAULT_SURFACE_COLOR, DEFAULT_SURFACE_SIZE,
                             DISPLAY_SIZE, FIVE, FRAMERATE, GRAPHICS_PATH,
                             GRAVITY, GROUND_LEVEL, GROUND_X, GROUND_Y,
                             JUMP_HEIGHT, JUMP_CEILING_Y, PLAYER_X, SKY_X,
                             SKY_Y, ZERO)


class TestConstants:
    """Test constants values"""

    def test_numeric_constants(self):
        """Test numeric constants"""
        assert FIVE == 5
        assert ZERO == 0

    def test_background_constants(self):
        """Test background constants"""
        import os
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

    def test_default_constants(self):
        """Test default constants"""
        assert DEFAULT_SURFACE_COLOR == (255, 0, 0)
        assert DEFAULT_SURFACE_SIZE == (100, 100)

    def test_display_constants(self):
        """Test display constants"""
        assert CAPTION == "Piccolo"
        assert DISPLAY_SIZE == (800, 400)
        assert FRAMERATE == 60
    
    def test_input_constants(self):
        """Test input constants"""
        assert CMD_JUMP == "JUMP"
        assert CMD_MOVE_LEFT == "MOVE_LEFT"
        assert CMD_MOVE_RIGHT == "MOVE_RIGHT"

    def test_player_constants(self):
        """Test player constants"""
        assert GRAVITY == 1
        assert JUMP_HEIGHT == -15
        assert JUMP_CEILING_Y == 200
        assert PLAYER_X == 100
