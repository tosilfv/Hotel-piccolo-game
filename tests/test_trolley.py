"""Unit tests for Trolley class"""
from unittest.mock import Mock
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

        # Action: create Trolley instance
        self.trolley = Trolley(self.screen)

        # Fix rect height for predictable bottom calculations
        self.trolley.rect.height = 40
        self.trolley.rect.y = GROUND_LEVEL - self.trolley.rect.height
        self.trolley.rect.bottom = GROUND_LEVEL

    def test_trolley_initialization(self):
        # Assert: initial state
        assert self.trolley.screen == self.screen
        assert self.trolley.speed == FIVE
        assert self.trolley.image is not None
        assert self.trolley.rect is not None
        assert self.trolley.rect.bottom == GROUND_LEVEL

    def test_trolley_draw(self):
        # Action
        self.trolley.draw(self.mediator.current_scene)

        # Assert
        self.screen.screen.blit.assert_called_once_with(
            self.trolley.image,
            self.trolley.rect
        )
