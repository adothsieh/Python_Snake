import pygame
from pygame.sprite import food_sprite

class FoodSprite(Sprite):
    """Class that manages where the food appears"""
    def __init__(self, ai_game, snake, position):

        super.__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.body_colour

        self.rect = pygame.Rect(w, h, self.settings.body_width, self.settings.body_height)
        self.eaten = False