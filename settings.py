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

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (63, 94, 249) # lazer blue color 
        self.bullets_allowed = 3

    def update_dimensions(self, width: int, height: int):
        """Update the default dimensions of screen"""
        self.screen_width = width
        self.screen_height = height

        # Adjust bg_img accordingly
        self.bg_img = pygame.transform.scale(self.bg_img, (width, height))
