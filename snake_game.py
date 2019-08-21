import sys
import pygame
import time
import random

from settings import Settings
from snake import Snake
from food_sprite import FoodSprite

class SnakeGame:
    """"Class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake")
        self.snake = Snake(self)
        # Set the background colour.
        self.bg_color = self.settings.bg_color
        self.grid = self.create_grid()
        self.food = pygame.sprite.Group()
        self.create_food()
        

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.snake.update()
            self._update_screen()
            time.sleep(150.0/1000.0)

    def _check_events(self):
        # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # Move snake to the right
                        self.snake.direction = (5,0)
                    elif event.key == pygame.K_LEFT:
                        #Move snake to the left
                        self.snake.direction = (-5,0)
                    elif event.key == pygame.K_UP:
                        #Move snake up
                        self.snake.direction = (0,-5)
                    elif event.key == pygame.K_DOWN:
                        #Move snake down
                        self.snake.direction = (0,5)

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.snake.update()
            self.direction = (0,1)
            self.update_food()
            
            # Make the most recently drawn screen visible
            pygame.display.flip()

    def create_grid(self):
        grid = []
        for i in range(0, self.settings.screen_width, 10):
            for j in range(0, self.settings.screen_height, 10):
                grid.append((i, j))

        return grid
    
    def update_food(self):
        collisions = pygame.sprite.groupcollide(self.snake.body, self.food, False, True)
        if collisions:
            self.create_food()
            self.snake.grow_snake()
        
        for food in self.food.sprites():
                food.draw_food()

    def create_food(self):
        valid_positions = list(set(self.grid) - set(self.snake.positions))
        position = random.choice(valid_positions)
        new_food = FoodSprite(self, self.snake, position)
        self.food.add(new_food)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SnakeGame()
    ai.run_game()