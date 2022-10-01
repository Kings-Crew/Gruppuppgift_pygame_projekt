import pygame

WIDTH, HEIGHT = 800 , 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.flip()

class player:
    pass

class Main:
    pass

    def main():

   
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    if __name__ == "__main__":
        main()