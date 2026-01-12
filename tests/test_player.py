"""Unit tests for Player class"""
from classes.player import Player
from unittest.mock import Mock

class TestPlayer:
    """Test Player class"""

    def test_player_initialization(self):
        """Test player initialization"""
        mock_screen = Mock()
        player = Player(mock_screen)

        assert player.screen == mock_screen
        assert player.image is not None
        assert player.rect is not None

    def test_player_move_left(self):
        """Test player move_left method"""
        mock_screen = Mock()
        mock_screen.screen = Mock()
        player = Player(mock_screen)
        start_x = player.rect.x
        player.move_left()

        assert player.rect.x == start_x - 5

    def test_player_move_right(self):
        """Test player move_right method"""
        mock_screen = Mock()
        mock_screen.screen = Mock()
        player = Player(mock_screen)
        start_x = player.rect.x
        player.move_right()

        assert player.rect.x == start_x + 5

    def test_player_draw(self):
        """Test player draw method"""
        mock_screen = Mock()
        mock_screen.screen = Mock()
        player = Player(mock_screen)
        player.draw()

        # Verify blit was called
        mock_screen.screen.blit.assert_called_once_with(
            player.image,
            player.rect
        )
