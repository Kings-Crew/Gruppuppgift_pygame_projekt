import pygame
import time
import os
from random import randint as RI

pygame.init()
collision_threshhold = 25
max_ball_speed = 5 
WHITE = (255,255,255)
FPS = 60
WIDTH, HEIGHT = 1280 , 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()#a group that holds all sprites,
#img_folder = os.path.join('assets\images')#path to image folder, saved as a variabel


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
<<<<<<< HEAD
        self.image = pygame.image.load(os.path.join(
            'assets', 'breakout_piece_blue.png'))
        self.y = 560
        self.x = 350

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 10
        """ if key[pygame.K_DOWN]:
            self.y += dist
        elif key[pygame.K_UP]:
            self.y -= dist """
        if key[pygame.K_RIGHT]:
            self.x += dist
        elif key[pygame.K_LEFT]:
            self.x -= dist

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


""" class player:
    pass """
=======
        self.width = WIDTH // cols
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
                pygame.draw.rect(screen, WHITE, (block[0]), 2)


def draw_window():#fills the screen with color white and updates the screen 
    screen.fill((WHITE))

class board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets','breakout_piece_blue.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (120,40))
        self.rect = self.image.get_rect()#creates a rect around image
        self.y_pos = HEIGHT -50
        self.x_pos = WIDTH /2
        self.rect.center = (self.x_pos, self.y_pos)
        self.direction = 0
        self.speed = 10 
    def update(self):
        if self.x_pos < 60:#32 is halv of board length in pixels
            self.x_pos = 60
        if self.x_pos > WIDTH -60:
            self.x_pos = WIDTH -60
        self.rect.center = (self.x_pos,self.y_pos)
    def move_left(self):
        self.x_pos -= self.speed
        self.direction = -1
    def move_right(self):
        self.x_pos += self.speed
        self.direction = 1
    
        
class ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = WIDTH / 2
        self.y_pos = HEIGHT / 2
        self.image = pygame.image.load(os.path.join('assets','ball_piece_blue.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (24,24))
        self.rect = self.image.get_rect()
        self.velocity = [RI(5,5), RI(5,5)]#self.velocity[0] is the first random for x pos and self.velocity[1] is the other random for y 
        self.rect.center = (self.x_pos, self.y_pos)
    def update(self):
        # 6 is halv of the ball's size in pixels 
        if self.x_pos < 6 or self.x_pos > WIDTH - 6: #if ball collide with left or rigth side it will reverse 
            self.velocity[0] = -self.velocity[0]
        if self.y_pos < 6: #if the ball collide with the top of the screen set the velocity to negative
            self.velocity[1] = -self.velocity[1]
        if self.velocity[0] == 0:#if the velociy reach 0 in either x or y direction, add velocity 
            self.velocity[0] += 1
        if self.velocity[1] == 0:
            self.velocity[1] += 1
        #sets the velocity to the current position so de ball will move acordingly 
        self.x_pos += self.velocity[0] 
        self.y_pos += self.velocity[1]
        self.rect.center = (self.x_pos, self.y_pos)
    def reset(self):# when the bal resets it will spawn in the center of the screen and have random direction(velocity)
        self.velocity = [RI(5,5), RI(5,5)]
        self.x_pos = WIDTH / 2
        self.y_pos = HEIGHT / 2
        self.rect.center = (self.x_pos, self.y_pos) 

    def check_board_collision(self,board):
         if self.rect.colliderect(board.rect):
            if abs(self.rect.bottom - board.rect.top) < collision_threshhold and self.velocity[1]>0:
                self.velocity[1] = -self.velocity[1]
                self.velocity[0] += board.direction
                if self.velocity[0] > max_ball_speed:
                    self.velocity[0] = max_ball_speed
                if self.velocity[0] < -max_ball_speed:
                    self.velocity[0] = -max_ball_speed
                else:
                    self.velocity[0] *= -1
            
    def is_out_bounds(self):
        return self.y_pos > HEIGHT


class player:
    pass
>>>>>>> 406c122d5804ce48c7955b413bc272b6dbaec27b

board = board()
ball = ball()
all_sprites.add(board,ball)
    
#create a wall
wall = wall()
wall.create_wall()



class Main:
    pass

    def main():
        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                board.move_left()
            if key[pygame.K_RIGHT]:
                board.move_right()            
            
            
            
            

<<<<<<< HEAD
            board.handle_keys()
            draw_window()
            board.draw(screen)
            pygame.display.update()


=======
            ball.check_board_collision(board)
            if ball.is_out_bounds():
                ball.reset()
            all_sprites.update()#uppdates all sprites that is inside sprite.group()
            draw_window()#makes the bakground white
            #draw wall
            wall.draw_wall()
            all_sprites.draw(screen)#prints/drwas out all sprites in sprite.group()
            pygame.display.update()       
          
    if __name__ == "__main__":
        main()
>>>>>>> 406c122d5804ce48c7955b413bc272b6dbaec27b
