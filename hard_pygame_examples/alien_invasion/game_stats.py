import json

class GameStats():
    """Track statistics forAlien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialze statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        # High scores should never be reset
        
        self.high_score = 0
        self.get_highscore()
        
    def reset_stats(self):
        """Initialize sttistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0 
        self.level = 1
    
    def get_highscore(self): 
        with open('highscore.json') as f_obj:
            self.high_score = json.load(f_obj)
