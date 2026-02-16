"""Unit tests for Background class"""
from unittest.mock import Mock, patch
from game_objects.background import Background
from utils.constants import (GROUND_X, GROUND_Y, ENTRANCE, SKY_X, SKY_Y, YARD)


@patch("game_objects.background.load_image")
class TestBackground:
    """Test Background class"""

    def setup_method(self):
        # Setup: mock screen object to record blit calls
        self.mock_screen = Mock()
        self.screen = Mock()

        self.screen.screen = self.mock_screen

    def test_background_initialization(self, _):
        """
        Test that Background initializes correctly with mocked load_image.

        Args:
            _: @patch gives mock as parameter for test-function (not used here)
        """
        background = Background(self.screen)

        # Assert: attributes should be set correctly
        assert background.screen == self.screen
        assert background.ground_surf is not None
        assert background.sky_surf is not None

    def test_background_draw(self, _):
        """
        Test that draw() calls blit for ground and sky surfaces.

        Args:
            _: @patch gives mock as parameter for test-function (not used here)
        """
        background = Background(self.screen)

        # Action
        background.draw()

        # Assert: blit called twice (ground + sky)
        assert self.mock_screen.blit.call_count == 2

        # Assert: blit called with correct coordinates
        self.mock_screen.blit.assert_any_call(background.ground_surf, (GROUND_X, GROUND_Y))
        self.mock_screen.blit.assert_any_call(background.sky_surf, (SKY_X, SKY_Y))

    def test_change_background(self, mock_load):
        """
        Test that change_background correctly swaps ground and sky surfaces.

        Args:
            mock_load: patched load_image mock
        """
        # Setup: simple mock objects for surfaces
        entrance_ground = object()
        entrance_sky = object()
        yard_sky = object()
        mock_load.side_effect = [entrance_ground, entrance_sky, yard_sky]

        background = Background(self.screen)

        # Action & assert: change to YARD scene
        background.change_background(YARD)
        assert background.ground_surf == entrance_ground
        assert background.sky_surf == yard_sky

        # Action & assert: change back to ENTRANCE scene
        background.change_background(ENTRANCE)
        assert background.ground_surf == entrance_ground
        assert background.sky_surf == entrance_sky
