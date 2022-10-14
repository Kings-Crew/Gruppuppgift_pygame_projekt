import pygame
from pygame.locals import *
import os


pygame.init()


screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dashlaks Breakout!')

#define font
#define font
font = pygame.font.SysFont('Constantia', 30)

#define colours
background = (0, 0, 0)
#block colours
block_tan = (230, 220, 170)
block_coffee_brown = (200, 190, 140)
block_rust = (210, 150, 75)
#paddle colours
board_color = (142, 135, 123)
board_outline = (100, 100, 100)
# text color
text_color = (255, 255, 255)


#define game variables
cols = 6
rows = 6
clock = pygame.time.Clock()
fps = 60
live_ball = False
game_over_global = 0

#function for putting text on the screen
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))



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
                    block_col = block_tan
                elif block[1] == 2:
                    block_col = block_coffee_brown
                elif block[1] == 1:
                    block_col = block_rust
                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen, background, (block[0]), 2)



#paddle class
class paddle():
    def __init__(self):
        self.image = pygame.image.load(os.path.join('assets','breakout_piece_blue.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (120,40))
        self.rect = self.image.get_rect()#creates a rect around image
        #define paddle variables
        self.height = 20
        self.width = int(screen_width / cols)
        self.x = int((screen_width / 2) - (self.width / 2))
        self.y = screen_height - (self.height * 2)
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0


    def move(self):
        #reset movement direction
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1

    def draw(self):
        pygame.draw.rect(screen, board_color, self.rect)
        pygame.draw.rect(screen, board_outline, self.rect, 3)

    def reset(self):
       #define paddle variables
       self.height = 20
       self.width = int(screen_width / cols)
       self.x = int((screen_width / 2) - (self.width / 2))
       self.y = screen_height - (self.height * 2)
       self.speed = 10
       self.rect = Rect(self.x, self.y, self.width, self.height)
       self.direction = 0



#ball class
class game_ball():
    def __init__(self, x, y):
        self.ball_rad = 20
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 8
        self.speed_y = -8
        self.speed_max = 10
        self.game_over = 0


    def move(self):

        #collision threshold
        collision_thresh = 10

        #start off with the assumption that the wall has been destroyed completely
        wall_destroyed = 1
        row_count = 0
        for row in wall.blocks:
            item_count = 0
            for item in row:
                #check collision
                if self.rect.colliderect(item[0]):
                    #check if collision was from above
                    if abs(self.rect.bottom - item[0].top) < collision_thresh and self.speed_y > 0:
                        self.speed_y *= -1
                    #check if collision was from below
                    if abs(self.rect.top - item[0].bottom) < collision_thresh and self.speed_y < 0:
                        self.speed_y *= -1                      
                    #check if collision was from left
                    if abs(self.rect.right - item[0].left) < collision_thresh and self.speed_x > 0:
                        self.speed_x *= -1
                    #check if collision was from right
                    if abs(self.rect.left - item[0].right) < collision_thresh and self.speed_x < 0:
                        self.speed_x *= -1
                    #reduce the block's strength by doing damage to it
                    if wall.blocks[row_count][item_count][1] > 1:
                        wall.blocks[row_count][item_count][1] -= 1
                    else:
                        wall.blocks[row_count][item_count][0] = (0, 0, 0, 0)

                #check if block still exists, in whcih case the wall is not destroyed
                if wall.blocks[row_count][item_count][0] != (0, 0, 0, 0):
                    wall_destroyed = 0
                #increase item counter
                item_count += 1
            #increase row counter
            row_count += 1
        #after iterating through all the blocks, check if the wall is destroyed
        if wall_destroyed == 1:
            self.game_over = 1

        




        #check for collision with walls
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1

        #check for collision with top and bottom of the screen
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > screen_height:
            self.game_over = -1


        #look for collission with board
        if self.rect.colliderect(board):
            #check if colliding from the top
            if abs(self.rect.bottom - board.rect.top) < collision_thresh and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += board.direction
                if self.speed_x > self.speed_max:
                    self.speed_x = self.speed_max
                elif self.speed_x < 0 and self.speed_x < -self.speed_max:
                    self.speed_x = -self.speed_max
            else:
                self.speed_x *= -1



        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over


    def draw(self):
        pygame.draw.circle(screen, board_color, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
        pygame.draw.circle(screen, board_outline, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad, 3)

    def reset(self, x, y):
        self.ball_rad = 20
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 8
        self.speed_y = -8
        self.speed_max = 10
        self.game_over = 0
    
wall = wall()
wall.create_wall()
board = paddle()
def main_game():
    global wall
    global live_ball
    
    
    #create a wall
    #create paddle


#create ball
    ball = game_ball(board.x + (board.width // 2), board.y - board.height)

    run = True
    while run:

        clock.tick(fps)
    
        screen.fill(background)

        #draw wall
        wall.draw_wall()


    #draw paddle
        board.draw()
        board.move()

    #draw ball
        ball.draw()
        ball.move()

        if live_ball:
        #draw board
            board.move()
        #draw ball
            if game_over_global != 0:
                live_ball = False

    #print players instructions
        if not live_ball:
            if game_over_global == 0:
                draw_text("KINGS CREWS 'BETA v2'", font, text_color, 100, screen_height // 2 + 100)
            elif game_over_global == 1:
                draw_text('Winner!', font, text_color, 240, screen_height // 2 + 50)
                draw_text('Click somwhere to START', font, text_color, 100, screen_height // 2 + 100)
            elif game_over_global == -1:
                draw_text('LOSER!', font, text_color, 240, screen_height // 2 + 50)
                draw_text('Click somwhere to START', font, text_color, 100, screen_height // 2 + 100)

    


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
                live_ball = True
                ball.reset(board.x + (board.width // 2), board.y - board.height)
                board.reset()
                wall.create_wall()
            


        pygame.display.update()

    #pygame.quit()

main_game()