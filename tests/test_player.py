"""Unit tests for Player class"""
from unittest.mock import Mock
from game_objects.player import Player
from utils.constants import GROUND_LEVEL


class TestPlayer:
    """Test Player class"""

    def setup_method(self):
        # Setup
        self.screen = Mock()
        self.screen.screen = Mock()
        self.mediator = Mock()
        self.mediator.running = False

        # Action: create Player instance
        self.player = Player(self.screen, self.mediator)

    def test_player_initialization(self):
        # Assert initial state
        assert self.player.screen == self.screen
        assert self.player.is_jumping is False
        assert self.player.gravity == 1
        assert self.player.jump_height == -10
        assert self.player.jump_ceiling_y == 200
        assert self.player.velocity_y == 0
        assert self.player.image is not None
        assert self.player.rect is not None
        assert self.player.rect.bottom == GROUND_LEVEL

    def test_player_move_left(self):
        # Setup: record initial x
        start_x = self.player.rect.x

        # Action
        self.player.move_left()

        # Assert
        assert self.player.rect.x == start_x - 5
        assert self.player.is_left is True

    def test_player_move_right(self):
        # Setup: record initial x
        start_x = self.player.rect.x

        # Action
        self.player.move_right()

        # Assert
        assert self.player.rect.x == start_x + 5
        assert self.player.is_left is False

    def test_player_jump_sets_state(self):
        # Setup
        self.player.is_jumping = False
        self.player.velocity_y = 0

        # Action
        self.player.jump()

        # Assert
        assert self.player.is_jumping is True
        assert self.player.velocity_y == self.player.jump_height

    def test_update_applies_gravity_when_jumping(self):
        # Setup
        start_y = 220
        self.player.is_jumping = True
        self.player.gravity = 1
        self.player.velocity_y = -5
        self.player.rect.y = start_y
        self.player.jump_ceiling_y = 100

        # Action
        self.player.update(self.mediator.running)

        # Assert
        assert self.player.velocity_y == -4
        assert self.player.rect.y == start_y - 4

    def test_update_caps_at_jump_ceiling_y(self):
        # Setup
        self.player.is_jumping = True
        self.player.gravity = 1
        self.player.velocity_y = -10
        self.player.rect.y = 190
        self.player.jump_ceiling_y = 200

        # Action
        self.player.update(self.mediator.running)

        # Assert
        assert self.player.velocity_y == 0
        assert self.player.rect.y == 200

    def test_update_resets_state_on_ground(self):
        # Setup
        self.player.is_jumping = True
        self.player.velocity_y = 5
        self.player.rect.y = GROUND_LEVEL - self.player.rect.height

        # Action
        self.player.update(self.mediator.running)

        # Assert
        assert self.player.rect.bottom == GROUND_LEVEL
        assert self.player.is_jumping is False
        assert self.player.velocity_y == 0

    def test_update_does_nothing_when_not_jumping(self):
        # Setup
        self.player.is_jumping = False
        self.player.velocity_y = 0
        self.player.rect.bottom = GROUND_LEVEL

        # Action
        self.player.update(self.mediator.running)

        # Assert
        assert self.player.rect.bottom == GROUND_LEVEL
        assert self.player.is_jumping is False
        assert self.player.velocity_y == 0

    def test_jump_then_update_moves_player_up(self):
        # Setup
        start_y = self.player.rect.bottom
        self.player.jump()

        # Action
        self.player.update(self.mediator.running)

        # Assert
        assert self.player.rect.bottom < start_y

    def test_player_draw(self):
        # Action
        self.player.draw()

        # Assert
        self.screen.screen.blit.assert_called_once_with(
            self.player.image,
            self.player.rect
        )
