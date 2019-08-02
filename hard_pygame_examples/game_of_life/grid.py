import pygame
import sys
import random
import json
class Grid():
    
    def __init__(self, gl_settings, screen):
        """Initialize"""
        self.gl_settings = gl_settings
        self.screen = screen
        self.grid_array = self.gl_settings.starting_array
        self.new_grid_array = self.grid_array
        self.old_grid_array = [[0 for _ in range(self.gl_settings.cell_num)] 
                                    for _ in range(self.gl_settings.cell_num)]
        self.neihbors = [[0 for _ in range(self.gl_settings.cell_num)] 
                                for _ in range(self.gl_settings.cell_num)]
        self.stable_objs = []
        self.load_stable_objs()
        self.auto_run = False
        
    def load_stable_objs(self):
        """Loads the Json file with the 2D lists of stable shapes"""
        with open('stable_shapes.json') as f_obj:
            self.stable_objs = json.load(f_obj)
    def draw_grid(self, x, y):
        """"""
        rect = pygame.Rect(x*(self.gl_settings.block_size+1), 
                                y*(self.gl_settings.block_size+1), 
                                self.gl_settings.block_size, 
                                self.gl_settings.block_size)
        if self.grid_array[y][x] == 0:
            pygame.draw.rect(self.screen,self.gl_settings.dead_cell_color,rect)
        else:
            pygame.draw.rect(self.screen,self.gl_settings.live_cell_color,rect)

    def get_num_of_neihbors(self, x, y):
        """Get's the number of live neihbors for a given cell at coordinate (x,y)"""
        
        #Note that if the cell is on an edge, it will look at the cells on the 
        #other edge
        
        #Check to the left
        if self.grid_array[y][(x + self.gl_settings.cell_num - 1) % self.gl_settings.cell_num] == 1:
                self.neihbors [y][x] += 1
        # Check to the right.
        if self.grid_array[y][(x+1) % self.gl_settings.cell_num] == 1:
                self.neihbors [y][x] += 1
                
        # Check upwards
        if self.grid_array[(y + self.gl_settings.cell_num - 1) % self.gl_settings.cell_num][x] == 1:
                self.neihbors [y][x] += 1
        
        # Check downwards        
        if self.grid_array[(y + 1) % self.gl_settings.cell_num][x] == 1:
                self.neihbors [y][x] += 1
        
        # Check upwards and to the left 
        if self.grid_array[(y + self.gl_settings.cell_num - 1) % self.gl_settings.cell_num][(x + self.gl_settings.cell_num - 1) % self.gl_settings.cell_num] == 1:
                self.neihbors [y][x] += 1
                
        # Check upwards and to the right
        if self.grid_array[(y + self.gl_settings.cell_num - 1) % self.gl_settings.cell_num][(x+1) % self.gl_settings.cell_num] == 1:
                self.neihbors [y][x] += 1
                
        # Check downwards and to the right
        if self.grid_array[(y + 1) % self.gl_settings.cell_num][(x+1) % self.gl_settings.cell_num] == 1:
                self.neihbors [y][x] += 1
        
        # Check downwards and to the left
        if self.grid_array[(y + 1) % self.gl_settings.cell_num][(x + self.gl_settings.cell_num - 1) % self.gl_settings.cell_num] == 1:
                self.neihbors [y][x] += 1
                
    def update_cells(self):
        """Makes a 2D neihgbors list with the number of live neighbors for 
           each cell"""
        self.neihbors = [[0 for _ in range(self.gl_settings.cell_num)] 
                            for _ in range(self.gl_settings.cell_num)]
        for y in range(self.gl_settings.cell_num):
            for x in range(self.gl_settings.cell_num):
                self.draw_grid(x, y) 
                self.get_num_of_neihbors(x, y)
                
    def find_stable_shapes(self):
        checked_cells = [[0 for _ in range(self.gl_settings.cell_num)] 
                            for _ in range(self.gl_settings.cell_num)]
        #Loops through all cells going left to right, up to down
        for y in range(self.gl_settings.cell_num):
            for x in range(self.gl_settings.cell_num):
                #look for live cells that have not been checked yet
                if self.grid_array[y][x] == 1 and checked_cells[y][x] == 0:
                    #Since we are scanning left to right, up to down,
                    #when we find a new unchecked cell, we should be at
                    #the leftmost square of the top row of the shape
                    obj = [[0 for _ in range(11)] for _ in range(11)]
                    left = 0
                    down = 0
                    right = 0
                    failed = False
                    while True:
                        delta_left = 0
                        delta_right = 0
                        for y1 in range(y,y+down+1):
                            for x1 in range(x-left,x+right+1):
                                try:
                                    #Look for cells that are alive and not
                                    #yet checked
                                    if self.grid_array[y1][x1] == 1 and checked_cells[y1][x1] == 0:
                                        #If we are at either edge, then 
                                        #stop the attempt to find the 
                                        #stable shape so that no incomplete
                                        #shapes are found
                                        if x1 % self.gl_settings.cell_num == 0 or y1 % self.gl_settings.cell_num == 0:
                                            failed = True
                                            break
                                        #Broaden the search by 1 in the 
                                        #direction the cell was found in
                                        if x1 == x-left:
                                            delta_left = 1
                                        if x1 == x+right:
                                            delta_right = 1
                                        if y1 == y+down:
                                            delta_down = 1
                                        checked_cells[y1][x1] = 1
                                        #Add the cell to the 2D list
                                        obj[y1-y][(x1-x)+5] = 1
                                #the obj 2D list only has room 5 to the left
                                #and 5 to the right of the starting value
                                #so an IndexError could occur
                                except IndexError:
                                    failed = True
                                    break
                                if failed:
                                    break
                            if failed:
                                break
                        if failed:
                            break
                        left += delta_left
                        down += delta_down
                        right += delta_right
                        
                        #If all deltas are 0: no new cells were found, 
                        #so the shape is complete
                        if delta_left == 0 and delta_right == 0 and delta_left == 0:
                            break
                
                    
                    if obj not in self.stable_objs and not failed:         
                        self.stable_objs.append(obj)             
    
    def step_cells(self):
        self.new_grid_array = [[0 for _ in range(self.gl_settings.cell_num)] 
                                    for _ in range(self.gl_settings.cell_num)]
        for y in range(self.gl_settings.cell_num):
            for x in range(self.gl_settings.cell_num):
                #Each cell stays alive it has 2 or 3 neighbors and is born if 
                #it has 3 neghbors
                if (self.neihbors[y][x] == 2 and self.grid_array[y][x] == 1 
                                                or self.neihbors[y][x] == 3):
                    self.new_grid_array [y][x] = 1
        #Check if everything has stablized
        if self.old_grid_array == self.new_grid_array:
            self.find_stable_shapes();
            if self.auto_run == True:
                #reset grid
                self.old_grid_array = [[0 for _ in range(self.gl_settings.cell_num)] for _ in range(self.gl_settings.cell_num)]
                self.rand_grid()
        else:
            self.old_grid_array = self.grid_array
            self.grid_array = self.new_grid_array
    
    def init_grid(self):
        leave = 0
        self.screen.fill(self.gl_settings.bg_color)
        self.grid_array = [[0 for _ in range(self.gl_settings.cell_num)] for _ in range(self.gl_settings.cell_num)]
        for y in range(self.gl_settings.cell_num):
                for x in range(self.gl_settings.cell_num):
                    self.draw_grid(x, y)  
        pygame.display.flip()            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_pos = pygame.mouse.get_pos()
                    column = click_pos[0] / (self.gl_settings.block_size + 1)
                    row = click_pos[1] / (self.gl_settings.block_size + 1)
                    self.grid_array[int(row)][int(column)] = 1
                    self.draw_grid(int(column), int(row))
                    pygame.display.flip()
                if event.type == pygame.KEYDOWN:
                    leave = 1
                    break
            if leave == 1:
                break
    def rand_grid(self):
        self.screen.fill(self.gl_settings.bg_color)
        self.grid_array = [[0 for _ in range(self.gl_settings.cell_num)] for _ in range(self.gl_settings.cell_num)]
        for y in range(self.gl_settings.cell_num):
                for x in range(self.gl_settings.cell_num):
                    if random.random() < .07:
                        self.grid_array[y][x] = 1
                    self.draw_grid(x, y)  
        pygame.display.flip()  
    
    def display_stable_shapes(self, num):
        self.grid_array = self.stable_objs[num]
        for y in range(11):
            for x in range(11):
                self.draw_grid(x, y)
            
                        
            
              
                    
