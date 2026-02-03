"""Unit tests for media files"""
import pygame
from pathlib import Path


class TestMediaFiles:
    """Test that all game media files exist and are loadable"""

    ROOT_DIR = Path(__file__).parent.parent
    MEDIA_DIR = ROOT_DIR / "media"
    GRAPHICS_DIR = MEDIA_DIR / "graphics"
    HOTEL_DIR = GRAPHICS_DIR / "hotel"
    ITEMS_DIR = GRAPHICS_DIR / "items"
    PLAYER_DIR = GRAPHICS_DIR / "player"
    VIDEO_FILE = ROOT_DIR / "video_2.gif"

    def _init_pygame(self):
        # Setup: initialize pygame modules and tiny display for image loading
        pygame.init()
        pygame.font.init()
        pygame.display.set_mode((1, 1))

    def test_images_exist_and_loadable(self):
        self._init_pygame()

        files = [
            self.HOTEL_DIR / "entrance_normal.png",
            self.HOTEL_DIR / "outdoor_ground_normal.png",
            self.HOTEL_DIR / "yard_normal.png",
            self.ITEMS_DIR / "trolley_empty_normal.png",
            self.ITEMS_DIR / "trolley_left_empty_normal.png",
            self.PLAYER_DIR / "piccolo_left_run1_normal.png",
            self.PLAYER_DIR / "piccolo_left_run2_normal.png",
            self.PLAYER_DIR / "piccolo_left_stand_normal.png",
            self.PLAYER_DIR / "piccolo_run1_normal.png",
            self.PLAYER_DIR / "piccolo_run2_normal.png",
            self.PLAYER_DIR / "piccolo_stand_normal.png",
        ]

        for file_path in files:
            # Assert file exists
            assert file_path.exists(), f"{file_path} is missing"

            # Action: load image
            surface = pygame.image.load(str(file_path))

            # Assert image is valid
            assert surface.get_width() > 0 and surface.get_height() > 0

    def test_video_exists(self):
        # Assert video exists
        assert self.VIDEO_FILE.exists(), f"{self.VIDEO_FILE} is missing"
