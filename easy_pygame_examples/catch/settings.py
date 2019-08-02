class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the games settings."""
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        
        # Baseball settings
        self.ball_limit = 3
        
        self.speedup_scale = .5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.mitt_speed_factor = 8
        self.initial_ball_speed = 0
        self.tick = .005
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increase speed settings."""
        self.mitt_speed_factor += .4
        self.initial_ball_speed += self.speedup_scale
        
        #self.tick /= self.speedup_scale
