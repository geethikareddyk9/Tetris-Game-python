
import pygame

pygame.init()
screen = pygame.display.set_mode((300, 600))

#pygame.display.set_caption("Falling Block!")

x =280
y = 0

width = 20 
height = 20
img = pygame.image.load('34.jpg')
img = pygame.transform.scale(img, (width, height))#transforms image to our required dimensions

speed = 0.02

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if y<600-height:#y<window height-blockheight
        y+=speed#to increase y with given speed to fall the block
    screen.fill((0, 0, 0))	
    screen.blit(img, (x, y))#block transfer,to copy contents of one surface to another surface
    pygame.display.update()

pygame.quit()
