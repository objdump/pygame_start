import pygame, sys
from pygame.locals import *

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
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLACK)
textRectObj = textSurfaceObj.get_rect()
textRectObj.top, textRectObj.centerx = 0, DISP_RECT[1]/2

while True: # main game loop
    #Update object
    textRectObj.top = textRectObj.top + 2
    if textRectObj.bottom >= DISP_RECT[0]:
        textRectObj.top = 1
    
    # Update drawing
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.display.update()
    
    # Control FPS
    fpsClock.tick(FPS)
    
    # Handle event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
