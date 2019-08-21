class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        #Screen settings
        self.screen_width = 400
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #Body settings
        self.body_height = 10
        self.body_width = 10
        self.body_colour = (0, 0, 0)

        #Food settings
        self.food_height = 15
        self.food_width = 15
        self.food_colour = (255, 0, 0)