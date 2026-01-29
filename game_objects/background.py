"""
Background for the game.
"""
import os
from game_objects.screen import Screen
from utils.constants import (GRAPHICS_PATH, GROUND_X, GROUND_Y, ENTRANCE,
                             SKY_X, SKY_Y, YARD)
from utils.helpers import load_image


class Background:
    """
    Represents the background of the game.

    Responsibilities:
        - Manage and draw the current background on the screen
        - Provide a method to change scenes (entrance, yard, etc.)
        - Serve as a communication point for Mediator to update visuals
        - Keep track of current scene state to prevent unnecessary redraws

    Attributes:
        screen: Screen instance for drawing operations.
        entrance_ground_surf: Ground surface for entrance scene.
        entrance_sky_surf: Sky surface for entrance scene.
        ground_surf: Currently active ground surface.
        sky_surf: Currently active sky surface.
    """
    
    def __init__(self, screen: Screen):
        self.screen = screen

        # Initial background ground and sky surfaces (hotel entrance)
        self.entrance_ground_surf = load_image(
            os.path.join(GRAPHICS_PATH,
                "hotel",
                "outdoor_ground_normal.png"))
        self.entrance_sky_surf = load_image(
            os.path.join(GRAPHICS_PATH,
                "hotel",
                "entrance_normal.png"))
        
        # Other surfaces
        self.yard_sky_surf = load_image(
            os.path.join(GRAPHICS_PATH,
                "hotel",
                "yard_normal.png"))

        # Set initial surfaces
        self.ground_surf = self.entrance_ground_surf
        self.sky_surf = self.entrance_sky_surf

    def change_background(self, scene: str) -> None:
        """
        Change the background ground and sky sufraces.

        Args:
            scene (str): Scene string representing background surface.
        """
        if scene == ENTRANCE:
            self.ground_surf = self.entrance_ground_surf
            self.sky_surf = self.entrance_sky_surf
        elif scene == YARD:
            self.ground_surf = self.entrance_ground_surf
            self.sky_surf = self.yard_sky_surf

    def draw(self) -> None:
        """
        Draw the background ground and sky sufraces to the screen.
        """
        self.screen.screen.blit(self.ground_surf, (GROUND_X, GROUND_Y))
        self.screen.screen.blit(self.sky_surf, (SKY_X, SKY_Y))
