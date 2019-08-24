import pygame
from snake_sprite import SnakeSprite


class Snake:
    """A class to manage the snake"""

    def __init__(self, ai_game):
        """Initialize the snake and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.ai_game = ai_game
        self.direction = None
        self.positions = [(ai_game.screen.get_width() /2, ai_game.screen.get_height() / 2)]
        self.ai_game.grid[self.positions[0]] = True
        self.head = SnakeSprite(self.ai_game, 'head', self.positions[0])
        self.body = pygame.sprite.Group()
        
    def update(self):
        # check if head has gone past left/right/top/bottom limits
        
        if self.direction:
            new_pos = self.add_tuples(self.positions[0], self.direction)
            self.ai_game.grid[(new_pos)] = True
            self.positions.insert(0, new_pos)
            old_pos = self.positions.pop(-1)
            self.ai_game.grid[(old_pos)] = False

        self.head.update(self.positions[0])
        self.head.draw_body()

        counter = 1
        for body in self.body:
            #print(self.positions[counter])
            body.update(self.positions[counter])
            body.draw_body()
            counter += 1

    def grow_snake(self):
        new_body = SnakeSprite(self.ai_game, 'body', self.positions[0])
        self.body.add(new_body)
        new_pos = self.add_tuples(self.positions[0], self.direction)
        self.head.update(new_pos)
        self.positions.insert(0, new_pos)

    def add_tuples(self, tupleA, tupleB):
        return tuple(a + b for a, b in zip(tupleA, tupleB))