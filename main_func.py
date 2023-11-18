import pygame
import random
import time


'''def fall(x,y):
    while :        
        if y<600-height:#y<window height-blockheight
            y+=0.02
            rect = pygame.Rect(x,y,80,20)'''
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
#pygame.draw.rect(screen,(255, 182, 193),(20,20,80,20))
#img = pygame.image.load('1.png')
#img = pygame.transform.scale(img,(width,height))
pygame.display.update()

#fall(0,0)

x_pos = 120
y_pos = 0
#y_pos2 = 0
#y_pos2+=20

def fall_blocks(y_pos):
    rect = pygame.Rect(x_pos,y_pos,80,20)
    '''r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    if r!=g or r!=b:'''
    
def main(x_pos, y_pos):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    play = True
    height = 20
    while play:
        if y_pos<600-height:#y<window height-blockheight
                y_pos+=0.01
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
                '''elif event.key == pygame.K_UP:
                    y_pos -= 20'''
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
        pygame.draw.rect(screen,(255, 182, 193),(x_pos,y_pos,80,20))
        pygame.display.update()
        #if y_pos<=600-y_pos2:
        #rect = pygame.Rect(x_pos,y_pos,80,20)
        #pygame.draw.rect(screen,(r, g, b),rect)
        
        #if y_pos<600-y_pos2 :
        #    y_pos+=0.020
                
        #    fall_blocks(y_pos)
            #img = pygame.image.load('34.jpg')
            #img = pygame.transform.scale(img, (width, height))
        #    rect = pygame.Rect(x_pos,y_pos,80,20)
        #    pygame.draw.rect(screen,(r, g, b),rect)
        #    pygame.display.update()
        #else:
         #   r = random.randint(0, 255)
          #  g = random.randint(0, 255)
           # b = random.randint(0, 255)
            #y_pos = 20
    #screen.blit(img,(xb,yb))
    
        pygame.draw.rect(screen,(255, 182, 193),(x_pos,y_pos,80,20))
        pygame.display.update()
main(x_pos, y_pos)
run = True
while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
pygame.quit()
