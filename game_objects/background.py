"""
Background for the game.
"""
import os
from utils.constants import (GRAPHICS_PATH, GROUND_X, GROUND_Y, ENTRANCE,
                             SKY_X, SKY_Y, YARD)
from utils.helpers import load_image


# Background
class Background:
    """
    Represents the background of the game.

    Attributes:
        screen: Screen instance for drawing operations.
        entrance_ground_surf: Ground surface for entrance scene.
        entrance_sky_surf: Sky surface for entrance scene.
        ground_surf: Currently active ground surface.
        sky_surf: Currently active sky surface.
    """
    
    def __init__(self, screen) -> None:
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

    def change_background(self, scene) -> None:
        """
        Change the background ground and sky sufraces.
        
        Returns:
            None
        """
        if scene == ENTRANCE:
            self.ground_surf = self.entrance_ground_surf
            self.sky_surf = self.entrance_sky_surf
        elif scene == YARD:
            self.ground_surf = self.entrance_ground_surf
            self.sky_surf = self.yard_sky_surf

        return None

    def draw(self) -> None:
        """
        Draw the background ground and sky sufraces to the screen.

        Returns:
            None
        """
        self.screen.screen.blit(self.ground_surf, (GROUND_X, GROUND_Y))
        self.screen.screen.blit(self.sky_surf, (SKY_X, SKY_Y))

        return None
