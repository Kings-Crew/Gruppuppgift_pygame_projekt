
import pygame
import time
import os
import random

FPS = 30
WIDTH, HEIGHT = 800 , 600
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
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
        speed = 10 
        

class ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'ball_piece_blue.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

class player:
    pass



board = board()
ball = ball()
all_sprites.add(board,ball)#instanser av sprite classes, läggs i en gemensam group för att enkelt kunna hantera fler sprites samtidigt
    
def handle_keys():
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]and board.Right < WIDTH:
        board.Right = board.speed
    elif key[pygame.K_LEFT] and board.Left > 0:
        board.Left -= board.speed

class Main:
    pass

    def main():
        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            
            
            handle_keys()#just nu ej fungerande, håller på med att fixa det
            all_sprites.update()#uppdaterar alla sprites som är i sprite.group()
            draw_window()#gör bakgrunden vit
            all_sprites.draw(screen)#printar/ritar ut alla sprites i sprite.group()
            pygame.display.update()       
          
    if __name__ == "__main__":
        main()