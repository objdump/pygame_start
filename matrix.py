import pygame, sys
from pygame.locals import *
import random

pygame.init()
DISP_RECT = (400, 300)
DISPLAYSURF = pygame.display.set_mode(DISP_RECT)
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

fontObj = pygame.font.Font('freesansbold.ttf', 16)


class Char(pygame.sprite.Sprite):
    def __init__(self, ch, pos):
        super(Char, self).__init__()
        self.surf = fontObj.render(ch, True, GREEN, BLACK)
        self.rect = self.surf.get_rect()
        self.speed = random.randint(1, 10)
        self.rect.top, self.rect.left = 0, pos*14

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= DISP_RECT[1]:
            self.rect.top = 0


chars = pygame.sprite.Group()
for i in range(0, 26):
    ch1 = Char(chr(i+ord('A')), i)
    chars.add(ch1)

while True: # main game loop

    # Update drawing
    DISPLAYSURF.fill(BLACK)
    for entity in chars:
        DISPLAYSURF.blit(entity.surf, entity.rect)
    pygame.display.update()
    
    # Control FPS
    fpsClock.tick(FPS)
    
    # Handle event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Update Sprite
    chars.update()
