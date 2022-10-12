import pygame
from pygame.locals import *

pygame.init()

screen_width = 1300
screen_height = 1300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout')


for event in pygame.event.get():
    if event.type == pygame.QUIT:
            run = False

#definierea färger
background = (0, 0, 0)
#block färger
block_tan = (230, 220, 170)
block_coffee_brown = (200, 190, 140)
block_rust = (210, 150, 75)


#definiera spel variabler
cols = 6
rows = 6



#brick wall class
class wall():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 50

    def create_wall(self):
        self.blocks = []
        #definiera en tom lista för individuella block
        block_individual = []
        for row in range(rows):
            #reset the block row list
            block_row = []
            #iterate through each column in that row
            for col in range(cols):
                #generear c och y positioner för varje block och skapa en rektangel
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


    pygame.display.update()

pygame.quit()