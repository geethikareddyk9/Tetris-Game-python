import pygame
width = 300
height = 600
black = (0,0,0)
pygame.init()
screen = pygame.display.set_mode((300,600))
pygame.display.update()
y = 20
for i in range(29):
    pygame.draw.line(screen,(255, 255, 255),(0, y),(300,y)) 
    y += 20
x = 20
for i in range(29):
    pygame.draw.line(screen,(255, 255, 255),(x, 0),(x, 600))
    x += 20
                     
pygame.display.update()
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        play = False
    

    pygame.display.flip()
