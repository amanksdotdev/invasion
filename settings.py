import pygame
class Settings:
    """A class to store all the settings for Invasion"""

    def __init__(self) -> None:
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (29, 41, 81)
        bg_img = pygame.image.load('images/black.png')
        self.bg_img = pygame.transform.scale(
            bg_img, (self.screen_width, self.screen_height))