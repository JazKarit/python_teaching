import pygame
import sys
import game_functions as gf
from settings import Settings
from grid import Grid
import json

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    gl_settings = Settings()
    screen = pygame.display.set_mode(
        (gl_settings.screen_width, gl_settings.screen_height))
    pygame.display.set_caption("Conway's Game of Life")
    grid = Grid(gl_settings, screen)
    grid.rand_grid()
    grid.auto_run = True
    
    # Start the main loop for the game.
    while True:
        # Redraw the screen during each pass through the loop.
        screen.fill(gl_settings.bg_color)
        grid.update_cells()
        grid.step_cells()
                
        # Make the most recently drawn screen visible.
        pygame.display.flip()
       
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    grid.rand_grid()
                elif event.key == pygame.K_s:
                    
                    with open('stable_shapes.json', 'w') as f_obj:
                        json.dump(grid.stable_objs, f_obj)
                    print(len(grid.stable_objs) )

run_game()


