
import pygame
import time
import os
from random import randint as RI

pygame.init()
collision_threshhold = 5
max_ball_speed = 5 
WHITE = (255,255,255)
FPS = 60
WIDTH, HEIGHT = 800 , 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()#tar in fps variabeln senare 
all_sprites = pygame.sprite.Group()#en group som håller alla sprites,
img_folder = os.path.join('assets\images')#path till image folder, sparas som variabel

def draw_window():#fills the screen with color white and updates the screen 
    screen.fill((WHITE))

class board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'breakout_piece_blue.png')).convert_alpha()
        self.rect = self.image.get_rect()#skapar en rect runt image
        self.y_pos = HEIGHT -50
        self.x_pos = WIDTH /2
        self.rect.center = (self.x_pos, self.y_pos)
        self.direction = 0
        self.speed = 10 
    def update(self):
        if self.x_pos < 32:
            self.x_pos = 32
        if self.x_pos > WIDTH -32:
            self.x_pos = WIDTH -32
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
        self.image = pygame.image.load(os.path.join(img_folder, 'ball_piece_blue.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.velocity = [RI(4,8), RI(-8, 8)]#self.velocity[0] är första random i listan och self.velocity[1] är den andra 
        self.rect.center = (self.x_pos, self.y_pos)
    def update(self):
        #4 är halva bollens storlek i pixels
        if self.x_pos < 4 or self.x_pos > WIDTH - 4: #if ball collide with left or rigth side it will reverse 
            self.velocity[0] = -self.velocity[0]
        if self.y_pos < 4: #if the ball collide with the top of the screen
            self.velocity[1] = -self.velocity[1]
        if self.velocity[0] == 0:#if the velociy reach 0 in either x or y direction
            self.velocity[0] += 1
        if self.velocity[1] == 0:
            self.velocity[1] += 1
        #sets the velocity to the current position
        self.x_pos += self.velocity[0]
        self.y_pos += self.velocity[1]
        self.rect.center = (self.x_pos, self.y_pos)
    def reset(self):
        self.velocity = [RI(4,8),RI(-8,8)]
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



board = board()
ball = ball()
all_sprites.add(board,ball)#instanser av sprite classes, läggs i en gemensam group för att enkelt kunna hantera fler sprites samtidigt
    


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
            
            ball.check_board_collision(board)
            if ball.is_out_bounds():
                ball.reset()
            all_sprites.update()#uppdaterar alla sprites som är i sprite.group()
            draw_window()#gör bakgrunden vit
            all_sprites.draw(screen)#printar/ritar ut alla sprites i sprite.group()
            pygame.display.update()       
          
    if __name__ == "__main__":
        main()