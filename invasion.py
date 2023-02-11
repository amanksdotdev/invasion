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
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        screen_width = self.screen.get_rect().width
        screen_height = self.screen.get_rect().height
        self.settings.update_screen(screen_width, screen_height)
        pygame.display.set_caption('Invasion')

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        bg_img_y = 0  # for background vertical motion
        while True:
            self._check_events()
            self.ship.update()

            # Update screen with a vertical background motion
            self._update_screen(bg_img_y)
            bg_img_y += 1
            # Rest y axis to 0 when the bg_img crosses the screen_height to motion loop
            if bg_img_y == self.settings.screen_height:
                bg_img_y = 0

            # Control the frame rate
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypress"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

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
