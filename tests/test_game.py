"""Unit tests for Game class"""
from control.input_handler import InputHandler
from control.mediator import Mediator
from classes.background import Background
from classes.player import Player
from control.game import Game
from unittest.mock import Mock, patch

class TestGame:
    """Test Game class"""

    def setup_method(self):
        """Setup tests"""
        self.screen = Mock()
        self.screen.clock = Mock()
        self.screen.framerate = 60

        self.background = Mock()
        self.player = Mock()
        self.mediator = Mock()
        self.input_handler = Mock()

        self.game = Game(
            screen=self.screen,
            background=self.background,
            player=self.player,
            mediator=self.mediator,
            input_handler=self.input_handler
        )

    def test_run_calls_input_handler(self):
        with patch('pygame.display.update'):
            self.game.run()

        self.input_handler.process_input.assert_called_once()

    def test_run_calls_draw_methods(self):
        with patch('pygame.display.update'):
            self.game.run()

        self.background.draw.assert_called_once()
        self.player.draw.assert_called_once()

    def test_run_updates_display(self):
        with patch('pygame.display.update') as mock_update:
            self.game.run()

        mock_update.assert_called_once()

    def test_run_ticks_clock(self):
        with patch('pygame.display.update'):
            self.game.run()

        self.screen.clock.tick.assert_called_once_with(self.screen.framerate)

    # def test_game_initialization(self):
    #     """Test Game initialization"""
    #     mock_screen = Mock()
    #     background = Background(mock_screen)
    #     player = Player(mock_screen)
    #     mediator = Mediator(player)
    #     input_handler = InputHandler(mediator)
    #     game = Game(mock_screen, background, player, mediator, input_handler)

    #     assert game.screen == mock_screen
    #     assert game.background == background
    #     assert game.player == player
    #     assert game.mediator == mediator
    #     assert game.input_handler == input_handler

    # def test_game_run(self, monkeypatch):
    #     """Test Game run method"""
    #     mock_screen = Mock()
    #     background = Background(mock_screen)
    #     player = Player(mock_screen)
    #     mediator = Mediator(player)
    #     input_handler = InputHandler(mediator)
    #     game = Game(mock_screen, background, player, mediator, input_handler)


    #     # Mock pygame.display.update
    #     mock_update = Mock()
    #     monkeypatch.setattr('pygame.display.update', mock_update)

    #     # Reset mocks
    #     mock_screen.screen.blit.reset_mock()
    #     mock_screen.clock.tick.reset_mock()

    #     # Call run
    #     game.run()

    #     # Verify draw methods were called
    #     assert mock_screen.screen.blit.called  # Background draw

    #     # Verify update was called
    #     assert mock_update.called

    # def test_game_run_calls_input_handler_process_input(self, monkeypatch):
    #     """Test that game.run calls input_handler.process_input"""
    #     mock_screen = Mock()
    #     background = Background(mock_screen)
    #     player = Player(mock_screen)
    #     mediator = Mediator(player)
    #     input_handler = InputHandler(mediator)
    #     game = Game(mock_screen, background, player, mediator, input_handler)

    #     # Mock pygame.display.update
    #     mock_update = Mock()
    #     monkeypatch.setattr('pygame.display.update', mock_update)

    #     # Mock input_handler.process_input to track calls
    #     with patch.object(input_handler, 'process_input') as mock_process_input:
    #         game.run()
    #         mock_process_input.assert_called_once()

    # def test_game_run_calls_player_draw(self, monkeypatch):
    #     """Test that game.run calls player.draw"""
    #     mock_screen = Mock()
    #     background = Background(mock_screen)
    #     player = Player(mock_screen)
    #     mediator = Mediator(player)
    #     input_handler = InputHandler(mediator)
    #     game = Game(mock_screen, background, player, mediator, input_handler)

    #     # Mock pygame.display.update
    #     mock_update = Mock()
    #     monkeypatch.setattr('pygame.display.update', mock_update)

    #     # Mock player.draw to track calls
    #     with patch.object(player, 'draw') as mock_draw:
    #         game.run()
    #         mock_draw.assert_called_once()

    # def test_game_run_calls_background_draw(self, monkeypatch):
    #     """Test that game.run calls background.draw"""
    #     mock_screen = Mock()
    #     background = Background(mock_screen)
    #     player = Player(mock_screen)
    #     mediator = Mediator(player)
    #     input_handler = InputHandler(mediator)
    #     game = Game(mock_screen, background, player, mediator, input_handler)

    #     # Mock pygame.display.update
    #     mock_update = Mock()
    #     monkeypatch.setattr('pygame.display.update', mock_update)

    #     # Mock background.draw to track calls
    #     with patch.object(background, 'draw') as mock_draw:
    #         game.run()
    #         mock_draw.assert_called_once()
