import pygame
from pygame.sprite import Sprite

from random import randint

class Baseball(Sprite):
    """A class to represent a falling baseball."""
    
    def __init__(self, ai_settings, screen):
        """Initialize the baseball and set its strting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the baseball image and get its rect attribute
        self.image = pygame.image.load('images/baseball.bmp')
        self.rect = self.image.get_rect()

        # Start each new baseball near the top of the screen.
        self.rect.x = randint(self.rect.width, 
                                ai_settings.screen_width - self.rect.width) 
        self.rect.y = self.rect.height
                
        # Store the alien's exact position.
        self.x = float(self.rect.x)
        
        self.balls_left = 3
        
        self.speed_y = self.ai_settings.initial_ball_speed
        
    def check_edges(self):
        """Return true if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True
            
    def update(self):
        """Move the alien right or left."""
        self.speed_y += .1
        self.rect.y += self.speed_y 
 

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
        
    def reset_ball(self):
        
        self.rect.x = randint(self.rect.width, 
                                self.ai_settings.screen_width - self.rect.width) 
        self.rect.y = self.rect.height
        self.speed_y = self.ai_settings.initial_ball_speed

