"""Unit tests for Screen class"""
from unittest.mock import Mock
from game_objects.screen import Screen
from utils.constants import (CAPTION, FRAMERATE)


class TestScreen:
    """Test Screen class"""

    def test_screen_initialization(self, monkeypatch):
        # Setup
        mock_display = Mock()
        mock_clock = Mock()
        mock_clock.tick = Mock()

        monkeypatch.setattr('pygame.display.set_mode', lambda size: mock_display)
        monkeypatch.setattr('pygame.display.set_caption', Mock())
        monkeypatch.setattr('pygame.time.Clock', lambda: mock_clock)

        # Action
        screen = Screen()

        # Assert
        assert screen.screen == mock_display
        assert screen.clock == mock_clock
        assert screen.framerate == FRAMERATE

    def test_screen_set_caption(self, monkeypatch):
        # Setup: track caption calls
        set_caption_called = []

        def mock_set_caption(caption):
            set_caption_called.append(caption)

        monkeypatch.setattr('pygame.display.set_mode', lambda size: Mock())
        monkeypatch.setattr('pygame.display.set_caption', mock_set_caption)
        monkeypatch.setattr('pygame.time.Clock', lambda: Mock())

        # Action: create Screen instance
        Screen()

        # Assert: caption set correctly
        assert CAPTION in set_caption_called
