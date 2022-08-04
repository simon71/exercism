import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """ Init the ship[ and set start location"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load ship image and get its rect.
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom centre of the screen.
        self.rect.midbottom = self.screen_rect.midbottom


