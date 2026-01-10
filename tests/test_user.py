"""Unit tests for User class"""
import pygame
from classes.user import User
from unittest.mock import patch

class TestUser:
    """Test User class"""

    def test_user_initialization(self):
        """Test user initialization"""
        user = User()

        assert user.left == False
        assert user.right == False

    def test_user_input_left(self):
        """Test user input to the left"""
        user = User()

        # Mock pygame.key.get_pressed to return LEFT key pressed
        with patch('pygame.key.get_pressed', return_value={pygame.K_LEFT: True, pygame.K_RIGHT: False}):
            user.user_input()
        
        assert user.left == True

    def test_user_input_right(self):
        """Test user input to the right"""
        user = User()

        # Mock pygame.key.get_pressed to return RIGHT key pressed
        with patch('pygame.key.get_pressed', return_value={pygame.K_LEFT: False, pygame.K_RIGHT: True}):
            user.user_input()
        
        assert user.right == True
