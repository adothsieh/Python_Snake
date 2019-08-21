import pygame
from snake_sprite import SnakeSprite


class Snake:
    """A class to manage the snake"""

    def __init__(self, ai_game):
        """Initialize the snake and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.direction = None
        self.body = pygame.sprite.Group()
        self.positions = [(ai_game.screen.get_width() /2, ai_game.screen.get_height() / 2)]
        print(self.positions[0])
        start_body = SnakeSprite(ai_game, 'head', self.positions[0])
        self.body.add(start_body)
        
    def update(self):
        # check if head has gone past left/right/top/bottom limits
        if self.direction:
            last_pos = self.positions[-1]
            new_pos = self.add_tuples(last_pos, self.direction)
            self.positions.append(new_pos)
            self.positions.pop(0)

        counter = 0

        for body in self.body:
            body.update(self.positions[counter])
            body.draw_body()
            counter += 1


    def add_tuples(self, tupleA, tupleB):
        return tuple(a + b for a, b in zip(tupleA, tupleB))