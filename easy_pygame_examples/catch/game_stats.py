class GameStats():
    """Track statistics for Catch."""
    
    def __init__(self, ai_settings):
        """Initialze statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        
    def reset_stats(self):
        """Initialize sttistics that can change during the game."""
        self.balls_left = self.ai_settings.ball_limit
