"""Unit tests for utils module"""
import pygame
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


class TestHelpers:
    """Test helper functions"""

    def test_load_image_successful(self, tmp_path):
        """Test loading a valid image"""
        import pygame
        from utils.helpers import load_image

        # Ensure Pygame is initialized
        pygame.init()

        # Create a temporary image file
        test_image = pygame.Surface((50, 50))
        test_image.fill((0, 0, 255))
        image_path = tmp_path / "test_img.png"

        # Save image to temp path
        pygame.image.save(test_image, str(image_path))

        # Test the loading
        loaded = load_image(str(image_path))

        # Check that it's a surface
        assert isinstance(loaded, pygame.Surface)

        # Check that size is correct
        assert loaded.get_size() == (100, 100)

    def test_load_image_not_found(self):
        """Test load_image when file doesn't exist"""
        from utils.helpers import load_image

        # Try to load a non-existent file
        res = load_image("non_existent_file.png")

        # Should return a placeholder surface
        assert isinstance(res, pygame.Surface)
        assert res.get_size() == (100, 100)  # Default size

    def test_load_image_pygame_error(self, monkeypatch):
        """Test load_image when pygame raises an error"""
        from utils.helpers import load_image

        # Mock pygame.image.load to raise an error
        def mock_load(path):
            raise pygame.error("Test error.")

        monkeypatch.setattr(pygame.image, "load", mock_load)

        # Should return a placeholder surface
        res = load_image("test.png")
        assert isinstance(res, pygame.Surface)
        assert res.get_size() == (100, 100)
