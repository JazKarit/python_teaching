import pygame

import sys

from settings import Settings
from player import Player

def check_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True 
                player.orientation = 'right'
            elif event.key == pygame.K_LEFT:
                player.moving_left = True 
                player.orientation = 'left'
            elif event.key == pygame.K_DOWN:
                player.moving_down = True 
            elif event.key == pygame.K_UP:
                player.moving_up = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            elif event.key == pygame.K_LEFT:
                player.moving_left = False
            elif event.key == pygame.K_DOWN:
                player.moving_down = False
            elif event.key == pygame.K_UP:
                player.moving_up = False


        
        
    
def run_game():

    # Initialize game and create a screen object.
    
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Cyber Game")
    
    player = Player(settings,screen)
    
    # Start the main loop for the game.
    while True:
        check_events(player)
        
        # Redraw the screen during each pass through the loop.
        screen.fill(settings.bg_color)
        
        player.update()
         
        player.blitme()
        pygame.display.flip()

run_game()

