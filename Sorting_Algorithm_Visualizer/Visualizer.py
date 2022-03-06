# Remember this is to get the requirements

# source sorting_algorithm_visualizer/venv/bin/activate
# python3 -m venv venv
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
    BACKGROUND_COLOR = WHITE

    Shades_Grey = [
        (128,128,128),
        (160,160,160),
        (192,192,192),
    ]

    
    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self,width,height,lst):
        self.width = width
        self.height = height
        

        self.window = pygame.display.set_mode((width,height)) #This creates the window
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self,lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst)) #you have the area you can represent the number of blocks in
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val)) # tells you how many distinct numbers you have and weighs in how high and small your blocks are
        self.start_x = self.SIDE_PAD // 2 # bottom left of screen is 0,0






def draw(draw_info): # you redrawn the canvas everytime ... not the most efficient way refer to line 96 for draw info
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    draw_list(draw_info)
    pygame.display.update()



def draw_list(draw_info): #refer to line 96 for draw info
    lst = draw_info.lst

    for i, val in enumerate(lst): #enumerate gives index and value of every single item in the list
        x = draw_info.start_x + i * draw_info.block_width # blocks in python are draw from the top left down tot he bottom right this line just adds the width to the previous one before
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height # you need to draw the taller rectangles higher on the screen 29:40 time stamp tells us how much larger we need to be above minimum

        color = draw_info.Shades_Grey[i % 3] #Going to return a 0, 1, 2

        pygame.draw.rect(draw_info.window,color,(x,y,draw_info.block_width,draw_info.height)) #could calculate precise height because this is drawing off the screen 32:57




def generate_start_list(n,min_val,max_val):
    lst = []
    for _ in range(n): #do this n times
        val = random.randint(min_val,max_val)
        lst.append(val)
    return lst



def main():
    run = True
    clock = pygame.time.Clock()
        
    n = 50
    min_val = 0
    max_val = 100

    lst = generate_start_list(n,min_val,max_val)
    draw_info = DrawInformation(800,600,lst) #This is the draw info line being passed into multiple function
    sorting = False
    ascending = True

    while run:
        clock.tick(60) # amount of times it runs
        draw(draw_info)
        # pygame.display.update() thats to display if you havent draw anything

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type != pygame.KEYDOWN:
                continue
            
            if event.key == pygame.K_r: #this is saying if you press the letter R
                lst = generate_start_list(n,min_val,max_val) # pass gets random numbers between min and max val
                draw_info.set_list(lst) # have to pass back to set the list and create it
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False: #this is saying if you press the letter R
                sorting = True
            elif event.key == pygame.K_a and not sorting: #this is saying if you press the letter R
                ascending = True
            elif event.key == pygame.K_d and not sorting: #this is saying if you press the letter R
                ascending = False


    pygame.quit()




if __name__ == "__main__": #look up what this means this is at 19:30 timestamp
    main()
