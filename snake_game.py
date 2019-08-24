import sys
import pygame
import time
import random

from settings import Settings
from snake import Snake
from food_sprite import FoodSprite
from game_statistics import GameStatistics
from button import Button

class SnakeGame:
    """"Class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.game_active = False
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake")
        self.grid = self.create_grid()
        self.snake = Snake(self)
        self.stats = GameStatistics(self)
        self.bg_color = self.settings.bg_color
        food_start = self.create_food()
        self.food = FoodSprite(self, self.snake, food_start)
        self.clock = pygame.time.Clock()
        self.play_button = Button(self, "Play")
        

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.clock.tick(10)
            self._check_events()
            self._loss_condition()
            self._update_screen()

    def _check_events(self):
        # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif self.game_active and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.snake.direction != (-10,0):
                        # Move snake to the right
                        self.snake.direction = (10,0)
                    elif event.key == pygame.K_LEFT and self.snake.direction != (10,0):
                        #Move snake to the left
                        self.snake.direction = (-10,0)
                    elif event.key == pygame.K_UP and self.snake.direction != (0,10):
                        #Move snake up
                        self.snake.direction = (0,-10)
                    elif event.key == pygame.K_DOWN and self.snake.direction != (0,-10):
                        #Move snake down
                        self.snake.direction = (0,10)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        
        self.screen.fill(self.settings.bg_color)

        self.update_food()
        self.snake.update()

        if not self.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def create_grid(self):
        grid = {}
        for i in range(0, self.settings.screen_width, 10):
            for j in range(0, self.settings.screen_height, 10):
                grid[(i,j)] = False

        return grid
    
    def update_food(self):
        collisions = pygame.sprite.collide_rect(self.snake.head, self.food)
        if collisions:
            new_pos = self.create_food()
            self.food.update(new_pos)
            self.snake.grow_snake()

        self.food.draw_food()

    def create_food(self):
        return (random.randrange(0, self.settings.screen_width - 1, 10),random.randrange(0, self.settings.screen_height - 1, 10))

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            self.game_active = True
            pygame.mouse.set_visible(False)

    def _loss_condition(self):
        self_collision = pygame.sprite.spritecollide(self.snake.head, self.snake.body, False)
        out_of_bounds = self.check_limits()

        if self_collision or out_of_bounds:
            self.reset_game()
            

    def check_limits(self):
        head_x = self.snake.head.rect.x
        head_y = self.snake.head.rect.y

        return (not 0 < head_x < self.settings.screen_width or not 0 < head_y < self.settings.screen_height)

    def reset_game(self):
        self.game_active = False
        self.snake.direction = None
        pygame.mouse.set_visible(True)
        self.snake.positions = [self.settings.screen_cent]
        self.snake.body.empty()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SnakeGame()
    ai.run_game()