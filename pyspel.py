from email.mime import image
import pygame
import time


pygame.init() # 

 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
 


screen_width = 1300 # Detta är skärmstorleken i högd och bredd
screen_height = 1300
screen = pygame.display.set_mode((screen_width, screen_height))



pygame.display.update() # Sätter rubriken på fönstret(Dashlak)
pygame.display.set_caption("Dashlak")

#define block colours
bg = (234, 218, 184)
#block colours
block_red = (242, 85, 96)
block_green = (86, 174, 87)
block_blue = (69, 177, 232)

#define game variables
cols = 6
rows = 6

#brick wall class
class wall():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 50
           
   

        


done = False
x = 5
y = 5
while not done:
    for event in pygame.event.get():
        if event.type == pygame:
            done = True
    pygame.draw.rect(screen, (0,128,255), pygame.Rect(x, y, 10, 10))



    pressed = pygame.key.get_pressed() # Sätter användning av pilarna för rörelse.
    if pressed[pygame.K_UP]: y -= 5
    if pressed[pygame.K_DOWN]: y+= 5
    if pressed[pygame.K_RIGHT]: x += 5
    if pressed[pygame.K_LEFT]: x -= 5




    pygame.display.flip()