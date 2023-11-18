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

#shape-1

pygame.draw.rect(screen,(255, 182, 193),(20,20,80,20))
pygame.display.update()
xb = 20
yb = 20
play = True
while play:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xb += 20
            elif event.key == pygame.K_LEFT:
                xb -= 20
            elif event.key == pygame.K_DOWN:
                yb += 20
                pygame.display.update()
    screen.fill((0,0,0))
    y = 20
    for i in range(29):
        pygame.draw.line(screen,(255, 255, 255),(0, y),(300,y)) 
        y += 20
    x = 20
    for i in range(29):
        pygame.draw.line(screen,(255, 255, 255),(x, 0),(x, 600))
        x += 20
    pygame.draw.rect(screen,(255, 182, 193),(xb,yb,80,20))
    pygame.display.update()

pygame.display.update()
pygame.quit()

  
   
