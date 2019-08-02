import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop."""
    
    def __init__(self, ai_settings, screen):
        """Initialize the raindrop and set its strting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the raindrop image and get its rect attribute
        self.image = pygame.image.load('raindrops.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
                
    def check_edge(self):
        """Return true if raindrop is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top == 3 * self.rect.height:
            return True
    
    def lift(self):
        self.rect.y += self.ai_settings.screen_height
        print("up")
            
    def update(self):
        """Make the raindrop fall."""
        self.y += self.ai_settings.rain_speed_factor
        self.rect.y = self.y

    def blitme(self):
        """Draw the raindrop at its current location."""
        self.screen.blit(self.image, self.rect)


