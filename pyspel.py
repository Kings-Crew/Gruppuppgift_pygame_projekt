import pygame
from pygame.locals import *

pygame.init()

screen_width = 1300
screen_height = 1300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout')

#define colours
bg = (0, 0, 0)
#block colours
block_tan = (230, 220, 170)
block_coffee_brown = (200, 190, 140)
block_rust = (210, 150, 75)


#define game variables
cols = 6
rows = 6



#brick wall class
class wall():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 50

    def create_wall(self):
        self.blocks = []
        #define an empty list for an individual block
        block_individual = []
        for row in range(rows):
            #reset the block row list
            block_row = []
            #iterate through each column in that row
            for col in range(cols):
                #generate x and y positions for each block and create a rectangle from that
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                #assign block strength based on row
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1
                #create a list at this point to store the rect and colour data
                block_individual = [rect, strength]
                #append that individual block to the block row
                block_row.append(block_individual)
            #append the row to the full list of blocks
            self.blocks.append(block_row)


    def draw_wall(self):
        for row in self.blocks:
            for block in row:
                #assign a colour based on block strength
                if block[1] == 3:
                    block_col = block_rust
                elif block[1] == 2:
                    block_col = block_coffee_brown
                elif block[1] == 1:
                    block_col = block_tan
                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen, bg, (block[0]), 2)



#create a wall
wall = wall()
wall.create_wall()



run = True
while run:

    screen.fill(bg)

    #draw wall
    wall.draw_wall()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()