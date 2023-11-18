import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((300, 600))
clock = pygame.time.Clock()
block_rect1 = Rect(100,580,80,20)
block_rect2 = Rect(80,0,40,40)
gravity = 4

run = True
while run:
    clock.tick(6)
    block_rect2.bottom += gravity
    collide = pygame.Rect.colliderect(block_rect1,block_rect2)
    if collide:
        block_rect2.bottom = block_rect1.top
    pygame.draw.rect(screen, (255,255,255),block_rect1)
    pygame.draw.rect(screen, (255,255,255),block_rect2)
    pygame.display.update()
    screen.fill((0,0,0))

