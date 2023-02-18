import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a asingle alien in the fleet"""

    def __init__(self, igame):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = igame.screen
        self.settings = igame.settings

        # Load the alien image and set its rect attribute
        loaded_image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(loaded_image, (50, 50))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    
