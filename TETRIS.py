import pygame
import random
 
"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
 
pygame.font.init()
 
# GLOBALS VARS
window_width = 800
window_height = 700
screen_width = 300  # meaning 300 // 10 = 30 width per block
screen_height = 600  # meaning 600 // 20 = 20 height per blo ck
block_size = 30
 
top_left_x = (window_width - screen_width) // 2
top_left_y = window_height - screen_height
 
 
# SHAPE FORMATS
 
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
 
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape

class shape(object):
    rows = 20  # y
    columns = 10 
 
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

#pygame.mixer.init()
#pygame.mixer.music.load('Glassy Bell - Samsung.mp3')
#pygame.mixer.music.set_volume(0.5)
#pygame.mixer.music.play(-1)


#defining a grid 
def _grid_(dict={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in dict:
                c = dict[(j,i)]
                grid[i][j] = c
    return grid

#drawing the window and giving colors 
def draw_window(surface):
    surface.fill((0,0,0))
    # Tetris Title
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('TETRIS', 1, (255,255,255))
 
    surface.blit(label, (top_left_x + screen_width / 2 - (label.get_width() / 2), 30))#x,y(=30 beginning) cordinates to display "Tetris"
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            #to draw the grid(outer box)
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0)#x,y cordinates,width,height
 
    
    draw_grid(surface, 20, 10)
    #to draw boundary for the play area
    pygame.draw.rect(surface, (121, 254, 12), (top_left_x, top_left_y, screen_width, screen_height),5)#5-thickness of the border line
    # pygame.display.update()
    
#drawing grid 
def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + screen_width, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + screen_height))  # vertical lines
 
 
#randomly choosing shapes 
def get_shape():
    global shapes, shape_colors
 
    return shape(5, 0, random.choice(shapes))

#to check if the position in which the block is placed is in the grid(i.e valid)
def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = rotate_shape(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False

    return True

#to chk if game is over
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False



#displaying game name
def caption(text, size, color, surface):
    font = pygame.font.SysFont('italic', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + screen_width/2 - (label.get_width() / 2), top_left_y + screen_height/2 - label.get_height()/2))



def main():
    global grid
    dict = {(top_left_x,top_left_y):(255,0,0),(top_left_x,top_left_y):(0,255,0),(top_left_x,top_left_y):(0,0,255)}  
    grid = _grid_(dict)

    change_block = False
    run = True
    current_block = get_shape()
    next_block = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    while run:
        fall_speed = 0.27
        grid = _grid_(dict)
        fall_time += clock.get_rawtime()
        clock.tick()
            
        # PIECE FALLING CODE
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_block.y += 1
            if not (valid_space(current_block, grid)) and current_block.y > 0:
                current_block.y -= 1
                change_block = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_block.x -= 1
                    if not valid_space(current_block, grid):
                        current_block.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_block.x += 1
                    if not valid_space(current_block, grid):
                        current_block.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_block.rotation = current_block.rotation + 1 % len(current_block.shape)
                    if not valid_space(current_block, grid):
                        current_block.rotation = current_block.rotation - 1 % len(current_block.shape)

                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_block.y += 1
                    if not valid_space(current_block, grid):
                        current_block.y -= 1
                        shape_pos = rotate_shape(current_block)

        shape_pos = rotate_shape(current_block)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_block.color

        # IF PIECE HIT GROUND
        if change_block:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                dict[p] = current_block.color
            current_block = next_block
            next_block = get_shape()
            change_block = False


        draw_window(win)

        pygame.display.update()

        # Check if user lost
        if check_lost(dict):
            run = False
            #pygame.mixer.music.stop()
    caption("GAME OVER", 50, (255,255,255), win)
    pygame.display.update()
    pygame.time.delay(2000)



def rotate_shape(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
 
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
 
    return positions


def main_func():
    run = True
    while run:
        win.fill((0,0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
 
            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()
 
 
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Tetris')
 
main_func()  # start game

