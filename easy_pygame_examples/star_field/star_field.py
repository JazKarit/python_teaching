import pygame
from pygame.sprite import Group

from random import randint

import sys

from settings import Settings
from star import Star

def get_number_of_stars_x(ai_settings, star_width):
    """Determine the number of stars that fit in a row."""
    available_space_x = ai_settings.screen_width - star_width
    number_stars_x = int(available_space_x / (2 * star_width))
    return number_stars_x
    
def get_number_rows(ai_settings, star_height):
    """Determine the number of rows of stars that fit on the screen."""
    available_space_y = ai_settings.screen_height - star_height
    number_rows = int(available_space_y / (2 * star_height))
    return number_rows
    
def create_star(ai_settings, screen, stars, star_number, row_number):
    """Create an star and place it in the row."""
    star = Star(ai_settings, screen)
    rand_factor_x = star.rect.width / 2
    rand_factor_y = star.rect.height / 2
    star_width = star.rect.width
    star.x = star_width + 2 * star_width * star_number
    star.rect.x = star.x + randint(int(-rand_factor_x), int(rand_factor_x))
    star.y = star.rect.height + 2 * star.rect.height * row_number
    star.rect.y = star.y + randint(int(-rand_factor_y), int(rand_factor_y))
    stars.add(star)

def create_field(ai_settings, screen, stars):
    """Create a full field of stars."""
    # Create a star and find the number of stars in a row.
    # Spacing between each star is equal to one star width.
    star = Star(ai_settings, screen)
    number_stars_x = get_number_of_stars_x(ai_settings, star.rect.width)
    number_rows = get_number_rows(ai_settings, star.rect.height)
    
    # Create the field of stars.
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(ai_settings, screen, stars, star_number, row_number)
    
    
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Star Field")
   
    
    stars = Group()
    
    # Create the fleet of aliens.
    # gf.create_fleet(ai_settings, screen, ship, aliens)
    
    create_field(ai_settings, screen, stars)
    
    # Start the main loop for the game.
    while True:
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        stars.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                sys.exit()
                
        # Make the most recently drawn screen visible.
        pygame.display.flip()
                 
       

run_game()


