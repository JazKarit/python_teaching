import pygame
from pygame.sprite import Group

from time import sleep

from settings import Settings
from mitt import Mitt
from baseball import Baseball
from game_stats import GameStats
from button import Button
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Catch")
    
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play")
    # Make a ship, a group of bullets, and a group of aliens.
    mitt = Mitt(ai_settings, screen)
    baseball = Baseball(ai_settings, screen)
    
    
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, mitt, baseball)
        if stats.game_active:
            mitt.update()
            baseball.update()
            gf.check_ball_fall(ai_settings, screen, mitt, baseball, stats)
            gf.check_mitt_baseball_collisions(ai_settings, screen, mitt, baseball)
            sleep(ai_settings.tick)
        
        
        gf.update_screen(ai_settings, screen, mitt, baseball, play_button, stats)    
       

run_game()
