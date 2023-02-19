import pygame


class Settings:
    """A class to store all the settings for Invasion"""

    def __init__(self) -> None:
        """Initialize the game's static settings"""
        self.high_score_path = '.game_stats.txt'

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (29, 41, 81)
        bg_img = pygame.image.load('images/bg.png')
        self.bg_img = pygame.transform.scale(
            bg_img, (self.screen_width, self.screen_height))

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (63, 94, 249)  # lazer blue color
        self.bullets_allowed = float('inf')

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def update_dimensions(self, width: int, height: int):
        """Update the default dimensions of screen"""
        self.screen_width = width
        self.screen_height = height

        # Adjust bg_img accordingly
        self.bg_img = pygame.transform.scale(self.bg_img, (width, height))
