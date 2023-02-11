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

        # Ship settings
        self.ship_speed = 5

    def update_screen(self, width, height):
        """Update the default dimension of screen"""
        self.screen_width = width
        self.screen_height = height

        # Adjust bg_img accordingly
        self.bg_img = pygame.transform.scale(self.bg_img, (width, height))
