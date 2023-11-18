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


if yb == 600 :
        yb -= 20
    if xb == 240 :
        xb -= 20
    if xb == -20 :
        xb +=20
