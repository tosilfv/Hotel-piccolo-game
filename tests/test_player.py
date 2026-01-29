"""Unit tests for Player class"""
from game_objects.player import Player
from unittest.mock import Mock
from utils.constants import (GROUND_LEVEL)


class TestPlayer:
    """Test Player class"""

    def setup_method(self):
        """Setup tests"""
        self.screen = Mock()
        self.screen.screen = Mock()

        # Create mediator mock
        self.mediator = Mock()

        # This can be used in update-method
        self.mediator.running = False

        # Create player now with mediator
        self.player = Player(self.screen, self.mediator)


    def test_player_initialization(self):
        """Test player initialization"""
        assert self.player.screen == self.screen
        assert self.player.is_jumping is False
        assert self.player.gravity == 1
        assert self.player.jump_height == -10
        assert self.player.jump_ceiling_y == 200
        assert self.player.velocity_y == 0
        assert self.player.image is not None
        assert self.player.rect is not None
        assert self.player.rect.y == 240

    def test_player_move_left(self):
        """Test player move_left method"""
        start_x = self.player.rect.x
        self.player.move_left()

        assert self.player.rect.x == start_x - 5

    def test_player_move_right(self):
        """Test player move_right method"""
        start_x = self.player.rect.x
        self.player.move_right()

        assert self.player.rect.x == start_x + 5

    def test_player_jump_sets_state(self):
        """Test player jump method"""
        self.player.is_jumping = False
        self.player.velocity_y = 0

        self.player.jump()

        assert self.player.is_jumping is True
        assert self.player.velocity_y == self.player.jump_height

    def test_update_applies_gravity_when_jumping(self):
        """Test player update method gravity"""
        start_y = 220
        self.player.is_jumping = True
        self.player.gravity = 1
        self.player.velocity_y = -5
        self.player.rect.y = start_y
        self.player.jump_ceiling_y = 100

        self.player.update(self.mediator.running)

        assert self.player.velocity_y == -4
        assert self.player.rect.y == start_y - 4

    def test_update_caps_at_jump_ceiling_y(self):
        """Test player update method jump ceiling y"""
        self.player.is_jumping = True
        self.player.gravity = 1
        self.player.velocity_y = -10
        self.player.rect.y = 190
        self.player.jump_ceiling_y = 200

        self.player.update(self.mediator.running)

        assert self.player.velocity_y == 0
        assert self.player.rect.y == 200

    def test_update_resets_state_on_ground(self):
        """Test player update method reset"""
        self.player.is_jumping = True
        self.player.velocity_y = 5
        self.player.rect.y = 250

        self.player.update(self.mediator.running)

        assert self.player.rect.y == GROUND_LEVEL
        assert self.player.is_jumping is False
        assert self.player.velocity_y == 0

    def test_update_does_nothing_when_not_jumping(self):
        """Test player update method no action"""
        self.player.is_jumping = False
        self.player.velocity_y = 0
        self.player.rect.y = GROUND_LEVEL

        self.player.update(self.mediator.running)

        assert self.player.rect.y == GROUND_LEVEL
        assert self.player.is_jumping is False
        assert self.player.velocity_y == 0

    def test_jump_then_update_moves_player_up(self):
        """Test player update method that after jump moves player up"""
        start_y = self.player.rect.y

        self.player.jump()
        self.player.update(self.mediator.running)

        assert self.player.rect.y < start_y

    def test_player_draw(self):
        """Test player draw method"""
        self.player.draw()

        # Verify blit was called
        self.screen.screen.blit.assert_called_once_with(
            self.player.image,
            self.player.rect
        )
