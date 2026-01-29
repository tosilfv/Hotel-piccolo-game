"""Unit tests for media files"""
import pytest
from pathlib import Path
import pygame


class TestMediaFiles:
    """Test that all game media files exist and are loadable."""

    ROOT_DIR = Path(__file__).parent.parent
    MEDIA_DIR = Path(__file__).parent.parent / "media"
    GRAPHICS_DIR = MEDIA_DIR / "graphics"
    HOTEL_DIR = GRAPHICS_DIR / "hotel"
    PLAYER_DIR = GRAPHICS_DIR / "player"
    VIDEO_FILE = ROOT_DIR / "video_1.gif"

    @pytest.mark.parametrize("file_path", [
        HOTEL_DIR / "entrance_normal.png",
        HOTEL_DIR / "outdoor_ground_normal.png",
        HOTEL_DIR / "yard_normal.png",
        PLAYER_DIR / "piccolo_run1_normal.png",
        PLAYER_DIR / "piccolo_run2_normal.png",
        PLAYER_DIR / "piccolo_stand_normal.png",
    ])
    def test_images_exist_and_loadable(self, file_path):
        """Test that images exist and load"""
        # Check that file exists
        assert file_path.exists(), f"{file_path} is missing"

        # Check that Pygame can load the image
        pygame.init()
        surface = pygame.image.load(str(file_path))
        assert surface.get_width() > 0 and surface.get_height() > 0

    def test_video_exists(self):
        """Check that the gameplay preview video exists."""
        assert self.VIDEO_FILE.exists(), f"{self.VIDEO_FILE} is missing"
