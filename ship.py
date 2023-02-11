import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, igame) -> None:
        """Initialize the ship and set its starting position."""
        self.screen = igame.screen
        self.screen_rect = igame.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def draw(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)