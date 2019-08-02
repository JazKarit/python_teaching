import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien


from random import randint


def check_keydown_events(event, ai_settings, screen, stats, mitt, baseball):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        mitt.moving_right = True
    elif event.key == pygame.K_LEFT:
        mitt.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, mitt, baseball)    
            
def check_keyup_events(event, mitt):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        mitt.moving_right = False
    elif event.key == pygame.K_LEFT:
        mitt.moving_left = False
        
def check_events(ai_settings, screen, stats, play_button, mitt, baseball):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, mitt, baseball)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mitt) 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, mitt, 
                baseball, mouse_x, mouse_y)
                
def check_play_button(ai_settings, screen, stats, play_button, mitt, baseball, 
        mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, mitt, baseball)
        
def start_game(ai_settings, screen, stats, mitt, baseball):
    # Hide the mouse cursor.
    pygame.mouse.set_visible(False)
    # Reset the game statistics.
    stats.reset_stats()
    stats.game_active = True
        
    # Empty the list of aliens and bullets
        
    # Center ball and mitt.
    baseball.reset_ball()
    mitt.center_mitt()
    
                
def update_screen(ai_settings, screen, mitt, baseball, play_button, stats):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens
    mitt.blitme()
    baseball.blitme()
    
    if not stats.game_active:
        play_button.draw_button()
                        
    # Make the most recently drawn screen visible.
    pygame.display.flip()

    

def check_mitt_baseball_collisions(ai_settings, screen, mitt, baseball):
    """Respond to to mitt-baseball collisions."""
    if mitt.rect.colliderect(baseball.rect):
        ai_settings.increase_speed()
        baseball.reset_ball()
        
    
def check_ball_fall(ai_settings, screen, mitt, baseball, stats):
    """Respond to a fallen ball"""
    if baseball.rect.top > ai_settings.screen_height:
        
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        
        if stats.balls_left > 0:
            stats.balls_left -= 1
            baseball.reset_ball()
            mitt.center_mitt()
            sleep(0.5)
        else:
            stats.game_active = False
            pygame.mouse.set_visible(True)


        
