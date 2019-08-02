class SpecialSettings():
    """A class to store all settings for Conway's Game of Life."""
    
    def __init__(self):
        """Initialize the games settings."""
        
        # Cell settings.
        self.cell_num = 11
        self.block_size = 9
        self.dead_cell_color = (255, 255, 255)
        self.live_cell_color = (0, 0, 0)        
        
        # Screen settings.
        self.screen_width = self.cell_num * 10
        self.screen_height = self.cell_num * 10
        self.bg_color = (127, 127, 127)
        
        
        self.starting_array = [[0 for _ in range(self.cell_num)] for _ in range(self .cell_num)]

