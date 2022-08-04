import sys
import pygame
from setting import Settings

class AlienInvasion:
    """Overall class to manage game assests and behaviour"""

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
                (self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        #Set background color
        self.bg_color = (self.settings.bg_color) #light grey

    def run_game(self):
        """Start the maain loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw the screen during each pass through
            self.screen.fill(self.bg_color)

            # Make the most recent drawn screen visabile
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and runs the game
    ai = AlienInvasion()
    ai.run_game()
