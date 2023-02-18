import pygame


class Settings:
    """A class to store all the settings for Invasion"""

    def __init__(self) -> None:
        """Initialize the game's settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (29, 41, 81)
        bg_img = pygame.image.load('images/bg.png')
        self.bg_img = pygame.transform.scale(
            bg_img, (self.screen_width, self.screen_height))

        # Ship settings
        self.ship_speed = 5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (63, 94, 249) # lazer blue color 
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def update_dimensions(self, width: int, height: int):
        """Update the default dimensions of screen"""
        self.screen_width = width
        self.screen_height = height

        # Adjust bg_img accordingly
        self.bg_img = pygame.transform.scale(self.bg_img, (width, height))
