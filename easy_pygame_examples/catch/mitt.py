import pygame
from pygame.sprite import Sprite

class Mitt(Sprite):
    
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its strting position."""
        super().__init__()
        self.screen = screen
        
        # Load the ship image and get its starting position
        self.image = pygame.image.load('images/mitt.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store  a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the mitt's position based on the movement flags"""
        # Update the mitt's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.mitt_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.mitt_speed_factor
            
        # Update rect object from self.center.
        self.rect.centerx = self.center
        
    def blitme(self):
        """Draw the mitt at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def center_mitt(self):
        
        self.rect.centerx = self.screen_rect.centerx
        
    
