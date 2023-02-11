import sys

import pygame

from settings import Settings
from ship import Ship


class Invasion:
    """Class to manage game asets and behaviour"""

    def __init__(self) -> None:
        """Initialize the game, and create game resources"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Set the display size
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Invasion')

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        bg_img_y = 0
        while True:
            self._check_events()
            self._update_screen(bg_img_y)
            bg_img_y += 1
            if bg_img_y == self.settings.screen_height:
                bg_img_y = 0
            # Control the frame rate
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self, bg_img_y):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.bg_img, (0, bg_img_y))
        self.screen.blit(self.settings.bg_img,
                         (0, -self.settings.screen_height + bg_img_y))
        self.ship.draw()

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    igame = Invasion()
    igame.run_game()
