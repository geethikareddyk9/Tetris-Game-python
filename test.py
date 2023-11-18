



import pygame
import random

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
x_pos = 20
y_pos = 20
y_pos2 = 0
y_pos2+=20

def fall_blocks(y_pos):
    rect = pygame.Rect(x_pos,y_pos,80,20)
    
    
def main(x_pos, y_pos):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and x_pos<300-80:
                    x_pos += 20
                elif event.key == pygame.K_LEFT and x_pos>0:
                    x_pos -= 20
                elif event.key == pygame.K_DOWN and y_pos<600-20:
                    y_pos += 20
                
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
        
        if y_pos<600-y_pos2:
            y_pos+=0.005
                
            
            rect = pygame.Rect(x_pos,y_pos,80,20)
            pygame.draw.rect(screen,(r, g, b),rect)
            pygame.display.update()
        
    
    pygame.display.update()
    pygame.quit()

main(x_pos, y_pos)
