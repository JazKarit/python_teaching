import pygame
from pygame.sprite import Group

from random import randint

import sys

from settings import Settings
from raindrop import Raindrop

def play_rain():
    sound = pygame.mixer.Sound("rain.wav")
    sound.play(-1)

def get_number_of_raindrops_x(ai_settings, raindrop_width):
    """Determine the number of stars that fit in a row."""
    available_space_x = ai_settings.screen_width - raindrop_width
    number_raindrops_x = int(available_space_x / (8 * raindrop_width))
    return number_raindrops_x
    
def get_number_rows(ai_settings, raindrop_height):
    """Determine the number of rows of raindrops that fit on the screen."""
    available_space_y = ai_settings.screen_height - raindrop_height
    # number_rows = int(available_space_y / (8 * raindrop_height))
    number_rows = 1
    return number_rows
    
def create_raindrop(ai_settings, screen, raindrops, raindrop_number, row_number):
    """Create an raindrop and place it in the row."""
    raindrop = Raindrop(ai_settings, screen)
    rand_factor_x = raindrop.rect.width * 4
    rand_factor_y = raindrop.rect.height * 4
    raindrop_width = raindrop.rect.width
    raindrop.x = raindrop_width + 8 * raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x + randint(int(-rand_factor_x), int(rand_factor_x))
    raindrop.y = raindrop.rect.height + 8 * raindrop.rect.height * row_number
    raindrop.rect.y = raindrop.y + randint(int(-rand_factor_y), int(rand_factor_y))
    raindrops.add(raindrop)

def create_field(ai_settings, screen, raindrops):
    """Create a full field of raindrops."""
    # Create a raindrop and find the number of raindrops in a row.
    # Spacing between each raindrop is equal to one raindrop width.
    raindrop = Raindrop(ai_settings, screen)
    number_raindrops_x = get_number_of_raindrops_x(ai_settings, raindrop.rect.width)
    number_rows = get_number_rows(ai_settings, raindrop.rect.height)
    
    # Create the field of stars.
    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
            create_raindrop(ai_settings, screen, raindrops, raindrop_number, row_number)
    
def check_rain_edge(ai_settings, screen, raindrops):
    """Respond appropriately if any raindrops have reached an edge."""
    for raindrop in raindrops.copy():
        if raindrop.check_edge():
            create_field(ai_settings, screen, raindrops)
            break
        if raindrop.rect.top >= ai_settings.screen_height:
            raindrops.remove(raindrop)
           
    
    
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Rain")
   
    
    raindrops = Group()
    
    # Create the fleet of raindrops.
    
    create_field(ai_settings, screen, raindrops)
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    play_rain()
    # Start the main loop for the game.
    while True:
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                sys.exit()
        
        raindrops.update()
        check_rain_edge(ai_settings, screen, raindrops)
        # Make the most recently drawn screen visible.
        raindrops.draw(screen)
        pygame.display.flip()
        
        # print(raindrop.check_edge())
       

run_game()


