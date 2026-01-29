"""Unit tests for helpers.py"""
import pygame


class TestHelpers:
    """Test helpers class"""

    def test_load_image_successful(self, tmp_path):
        """Test loading a valid image"""
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
        assert loaded.get_size() == (50, 50)

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
