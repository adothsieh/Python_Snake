import pygame
from pygame.sprite import Sprite

class SnakeSprite(Sprite):
    """A class to manage the individual body parts of the snake"""
    def __init__(self, ai_game, title, position):
        """Create a portion of the snake's body"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.body_colour
        self.title = title
        
        #Create a body part at the given position
        w,h = position
        self.rect = pygame.Rect(w, h, self.settings.body_width, self.settings.body_height)

    def update(self, position):
        x,y = position
        
        self.rect.y = y
        self.rect.x = x

    def draw_body(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
