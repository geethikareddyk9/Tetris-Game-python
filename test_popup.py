import pygame

pygame.init()
screen = pygame.display.set_mode((300,600))
width = 80
height = 20
I = pygame.image.load("shape.png")
I = pygame.transform.scale(I,(width,height))
#display_image = pygame.display.set_mode((
screen.blit(I,(0,580))
screen.blit(I,(80,580))
screen.blit(I,(160,580))
screen.blit(I,(240,580))
screen.blit(I,(40,560))
pygame.display.update()
#row = grid[i]
#if (0,0,0) not in row 


