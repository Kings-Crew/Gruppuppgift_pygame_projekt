import pygame
import time
import os
#from pygame.locals import *
pygame.init()
FPS = 30
WIDTH, HEIGHT = 1300, 1300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
GREY = (90, 90, 90)

clock = pygame.time.Clock()


def draw_window():  # fills the screen with color white and updates the screen
    screen.fill((GREY))


class board(object):
    def __init__(self):
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

board = board()


class Main:
    pass

    def main():
        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            board.handle_keys()
            draw_window()
            board.draw(screen)
            pygame.display.update()


