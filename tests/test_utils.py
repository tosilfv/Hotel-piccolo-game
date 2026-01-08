"""Unit tests for utils module"""

class TestConstants:
    """Test constants values"""

    def test_numeric_constants(self):
        """Test numeric constants"""
        from utils.constants import (ZERO)
        assert ZERO == 0

    def test_background_constants(self):
        """Test background constants"""
        import os
        from utils.constants import (GRAPHICS_PATH, GROUND_X, GROUND_Y, SKY_X,
                                     SKY_Y)
        assert GRAPHICS_PATH == os.path.join(
                    os.path.dirname(
                        os.path.dirname(
                            __file__)),
                                "media",
                                    "graphics")
        assert GROUND_X == 0
        assert GROUND_Y == 320
        assert SKY_X == 0
        assert SKY_Y == -120

    def test_default_constants(self):
        """Test default constants"""
        from utils.constants import (DEFAULT_COLOR, DEFAULT_SIZE)
        assert DEFAULT_COLOR == (0, 255, 0)
        assert DEFAULT_SIZE == (100, 100)

    def test_display_constants(self):
        """Test display constants"""
        from utils.constants import (CAPTION, DISPLAY_SIZE, FRAMERATE)
        assert CAPTION == "Piccolo2"
        assert DISPLAY_SIZE == (800, 400)
        assert FRAMERATE == 60
