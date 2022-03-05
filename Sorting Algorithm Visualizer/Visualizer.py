# Remember this is to get the requirements

# pip3 freeze > requirements.txt  
# cd into sorting_algo_visualizer
# activate virtual environment through source venv/bin/activate
# pip3 install -r requirements.txt 

import pygame
import random
pygame.init()



class DrawInformation:
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    GREY = 128,128,128
    BACKGROUND_COLOR = WHITE

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self,width,height,lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width,height)) #This creates teh window
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self,lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst)) #you have the area you can represent the number of blocks in
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val)) # tells you how many distinct numbers you have and weighs in how high and small your blocks are
        self.start_x = self.SIDE_PAD // 2 # bottom left of screen is 0,0

