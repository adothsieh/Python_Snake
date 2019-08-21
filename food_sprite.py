import pygame
from pygame.sprite import Sprite

class FoodSprite(Sprite):
    """Class that manages where the food appears"""
    def __init__(self, ai_game, snake, position):

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.food_colour

        w, h = position
        self.rect = pygame.Rect(w, h, self.settings.food_width, self.settings.food_height)

    def draw_food(self):
        pygame.draw.rect(self.screen, self.color, self.rect)