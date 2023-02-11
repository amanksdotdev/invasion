import sys

import pygame

from settings import Settings


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

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Redraw the screen during each pass through the loop
                self.screen.fill(self.settings.bg_color)

                # Make the most recentrly drawn screen visible
                pygame.display.flip()

                # controlling the frame rate
                self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = Invasion()
    ai.run_game()
