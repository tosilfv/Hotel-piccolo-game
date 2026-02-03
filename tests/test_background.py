"""Unit tests for Background class"""
from unittest.mock import Mock, patch
from game_objects.background import Background
from utils.constants import ENTRANCE, YARD


class TestBackground:
    """Test Background class"""

    def setup_method(self, method):
        # Setup mock screen with a screen.blit method
        self.mock_screen_inner = Mock()
        self.screen = Mock()
        self.screen.screen = self.mock_screen_inner

    @patch("game_objects.background.load_image", return_value=Mock())
    def test_background_initialization(self, mock_load):
        # Create Background instance with mocked load_image
        background = Background(self.screen)

        # Assert that background is created correctly
        assert background.screen == self.screen
        assert background.ground_surf is not None
        assert background.sky_surf is not None

    @patch("game_objects.background.load_image", return_value=Mock())
    def test_background_draw(self, mock_load):
        # Create Background instance with mocked load_image
        background = Background(self.screen)

        # Action: call draw method
        background.draw()

        # Assert: blit was called twice (once for ground and once for sky)
        assert self.mock_screen_inner.blit.call_count == 2

    @patch("game_objects.background.load_image")
    def test_change_background(self, mock_load):
        # Setup: return different mocks for each load_image call
        entrance_ground_mock = Mock()
        entrance_sky_mock = Mock()
        yard_sky_mock = Mock()
        mock_load.side_effect = [entrance_ground_mock, entrance_sky_mock, yard_sky_mock]

        # Create Background instance
        background = Background(self.screen)

        # Change to YARD scene
        background.change_background(YARD)
        # Assert: ground stays entrance, sky changes to yard
        assert background.ground_surf == entrance_ground_mock
        assert background.sky_surf == yard_sky_mock

        # Change back to ENTRANCE scene
        background.change_background(ENTRANCE)
        # Assert: both ground and sky reset to entrance surfaces
        assert background.ground_surf == entrance_ground_mock
        assert background.sky_surf == entrance_sky_mock
