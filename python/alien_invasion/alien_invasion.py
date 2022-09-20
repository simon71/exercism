import sys
import pygame
from setting import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assests and behaviour"""

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
                (self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #Set background color
        self.bg_color = (self.settings.bg_color) #light grey

    def run_game(self):
        """Start the maain loop for the game"""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """Respond to key presses and mouse events"""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Move ship to the right
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        #Redraw the screen during each pass through
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        # Make the most recent drawn screen visabile
        pygame.display.flip()



if __name__ == '__main__':
    #Make a game instance, and runs the game
    ai = AlienInvasion()
    ai.run_game()
