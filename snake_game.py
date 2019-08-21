import sys
import pygame
import time

from settings import Settings
from snake import Snake

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
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.snake.update()
            self._update_screen()
            time.sleep(250.0/1000.0)

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
            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SnakeGame()
    ai.run_game()