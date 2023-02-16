import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, igame) -> None:
        """Initialize the ship and set its starting position."""
        self.screen = igame.screen
        self.screen_rect = igame.screen.get_rect()

        self.settings = igame.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y = self.rect.y - 20  # Offset from touching the bottom

        # Store a float for the ships's exact horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect object from self.x
        self.rect.x = self.x

    def draw(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
