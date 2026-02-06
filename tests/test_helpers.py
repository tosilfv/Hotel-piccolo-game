"""Unit tests for helpers.py"""
import pygame
from utils.helpers import load_image


class TestHelpers:
    """Test helpers class"""

    def test_load_image_successful(self, tmp_path):
        pygame.init()
        try:
            # Setup: create temporary image
            test_image = pygame.Surface((50, 50))
            test_image.fill((0, 0, 255))
            image_path = tmp_path / "test_img.png"
            pygame.image.save(test_image, str(image_path))

            # Action
            loaded = load_image(str(image_path))

            # Assert
            assert isinstance(loaded, pygame.Surface)
            assert loaded.get_size() == (50, 50)
        finally:
            pygame.quit()

    def test_load_image_not_found(self):
        pygame.init()
        try:
            # Action: try to load a non-existent file
            res = load_image("non_existent_file.png")

            # Assert: return placeholder surface
            assert isinstance(res, pygame.Surface)
            assert res.get_size() == (100, 100)

            # Check that placeholder text is actually drawn
            # Convert to array and check that not all pixels are the same color
            pixel_array = pygame.surfarray.array3d(res)
            assert pixel_array.min() != pixel_array.max()
        finally:
            pygame.quit()

    def test_load_image_pygame_error(self, monkeypatch):
        pygame.init()
        try:
            # Setup: force pygame.image.load to raise an error
            def mock_load(*args, **kwargs):
                raise pygame.error("Test error.")
            monkeypatch.setattr(pygame.image, "load", mock_load)

            # Action
            res = load_image("test.png")

            # Assert: return placeholder surface
            assert isinstance(res, pygame.Surface)
            assert res.get_size() == (100, 100)

            # Check that placeholder text is actually drawn
            pixel_array = pygame.surfarray.array3d(res)
            assert pixel_array.min() != pixel_array.max()
        finally:
            pygame.quit()
