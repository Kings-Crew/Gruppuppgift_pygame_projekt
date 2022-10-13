import pygame

brick_cols = 12
brick_rows = 6
brick_start = 16

bricks = [
    'assets/element_blue_rectangle_glossy.png',
    'assets/element_green_rectangle_glossy.png',
    'assets/element_grey_rectangle.png',
    'assets/element_purple_rectangle.png',
    'assets/element_red_rectangle_glossy.png',
    'assets/element_yellow_rectangle.png'
]

class Bricks:
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.all_bricks = pygame.sprite.Group()

        for r in range(brick_rows):
            for c in range(brick_cols):
                brick = Brick(r, c)
                self.all_bricks.add(brick)
                self.all_sprites.add(brick)



class Brick:
    def __init__(self, row, col):
        self.x_pos = brick_start * (col * 64) * 32
        self.y_pos = brick_start * (row * 32) * 16
        self.image = pygame.image.load(bricks[row])
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)
