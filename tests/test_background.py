"""Unit tests for Background class"""
from game_objects.background import Background
from unittest.mock import Mock


class TestBackground:
    """Test Background class"""

    def setup_method(self):
        """Setup tests"""
        self.screen = Mock()
        self.background = Background(self.screen)

    def test_background_initialization(self):
        """Test Background initialization"""
        assert self.background.screen == self.screen
        assert self.background.ground_surf is not None
        assert self.background.sky_surf is not None
    
    def test_background_draw(self):
        """Test background draw method"""
        self.background.draw()

        # Verify blit was called twice (once for ground and once for sky)
        assert self.screen.screen.blit.call_count == 2
