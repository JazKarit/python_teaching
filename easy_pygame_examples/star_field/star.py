import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single str in a field."""
    
    def __init__(self, ai_settings, screen):
        """Initialize the star and set its strting position."""
        super().__init__()
        self.screen = screen
        
        # Load the alien image and get its rect attribute
        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
                


    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)


