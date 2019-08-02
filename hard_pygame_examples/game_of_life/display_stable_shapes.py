import pygame
import sys
import game_functions as gf
from display_shape_settings import SpecialSettings
from grid import Grid
import json

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    gl_settings = SpecialSettings()
    screen = pygame.display.set_mode(
        (gl_settings.screen_width, gl_settings.screen_height))
    pygame.display.set_caption("Conway's Game of Life")
    grid = Grid(gl_settings, screen)
    
    
    # Start the main loop for the game.
    num = 0
    while True:
        
        # Redraw the screen during each pass through the loop.
        screen.fill(gl_settings.bg_color)
    
        grid.display_stable_shapes(num % len(grid.stable_objs))
        grid.update_cells()
        grid.step_cells()
        if grid.old_grid_array != grid.grid_array:
            del(grid.stable_objs[num % len(grid.stable_objs)])        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    num += 1
                    print(num)    
                

run_game()


