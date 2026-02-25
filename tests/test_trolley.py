"""Unit tests for Trolley class"""
from unittest.mock import Mock, patch
from game_objects.trolley import Trolley
from utils.constants import GROUND_LEVEL, ENTRANCE, FIVE


class TestTrolley:
    """Test Trolley class"""

    def setup_method(self):
        # Setup
        self.screen = Mock()
        self.screen.screen = Mock()
        self.mediator = Mock()

        self.mediator.current_scene = ENTRANCE

        # Patch load_image to return a mock object with get_rect method
        with patch("game_objects.trolley.load_image") as mock_load:
            mock_image = Mock()
            mock_rect = Mock()
            mock_rect.height = 40
            mock_rect.bottom = GROUND_LEVEL
            mock_image.get_rect.return_value = mock_rect
            mock_load.return_value = mock_image

            # Action: create Trolley instance
            self.trolley = Trolley(self.screen, self.mediator)

        # Fix rect height for predictable bottom calculations
        self.trolley.rect.height = 40
        self.trolley.rect.y = GROUND_LEVEL - self.trolley.rect.height
        self.trolley.rect.bottom = GROUND_LEVEL

    def test_trolley_initialization(self):
        # Assert: initial state
        assert self.trolley.screen == self.screen
        assert self.trolley.mediator == self.mediator
        assert self.trolley.speed == FIVE
        assert self.trolley.image is not None
        assert self.trolley.rect is not None
        assert self.trolley.rect.bottom == GROUND_LEVEL
        assert not self.trolley.taken

    def test_trolley_update_with_player(self):
        # Action
        player_pos = (100, GROUND_LEVEL)
        self.trolley.taken = True
        self.trolley.rect.x = 100
        self.trolley.update(player_pos)

        # Assert: trolley follows player
        assert self.trolley.rect.midbottom == player_pos

    def test_trolley_update_without_player(self):
        # Action: no player
        self.trolley.taken = False
        self.trolley.rect.x = 100
        self.trolley.update(None)

        # Assert: position unchanged
        assert self.trolley.rect.bottom == GROUND_LEVEL

    def test_trolley_draw_when_taken(self):
        # Setup: trolley is taken
        self.trolley.taken = True

        # Action
        self.trolley.draw()

        # Assert: blit called
        self.screen.screen.blit.assert_called_once_with(
            self.trolley.image,
            self.trolley.rect
        )

    def test_trolley_draw_in_current_scene(self):
        # Action
        self.trolley.taken = False
        self.trolley.scene_name = ENTRANCE

        self.trolley.draw()

        # Assert: blit called because scene matches
        self.screen.screen.blit.assert_called_once_with(
            self.trolley.image,
            self.trolley.rect
        )

    def test_trolley_draw_not_in_scene(self):
        # Action
        self.trolley.taken = False
        self.trolley.scene_name = "other_scene"

        self.trolley.draw()

        # Assert: blit not called because scene does not match and not taken
        self.screen.screen.blit.assert_not_called()
