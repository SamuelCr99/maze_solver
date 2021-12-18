from numpy.core.fromnumeric import size
import pygame
import numpy as np


SIZE = 800

WIN = pygame.display.set_mode((SIZE, SIZE))

BLOCK_PER_LINE = 40

BLOCK_SIZE = SIZE/BLOCK_PER_LINE
#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

class Square():
    def __init__(self, backpointer, state):
        self.backpointer = backpointer
        self.state = state


def draw_screen (win, world):
    win.fill(WHITE)

    for i in range(1,BLOCK_PER_LINE):
        line_y = pygame.Rect(i * BLOCK_SIZE,0,1,SIZE)
        pygame.draw.rect(win,BLACK,line_y)
        
        line_x = pygame.Rect(0, i * BLOCK_SIZE,SIZE,1)
        pygame.draw.rect(win,BLACK,line_x)
    
    for i in range (BLOCK_PER_LINE):
        for k in range (BLOCK_PER_LINE):
            if (world[i][k] != 0):
                block = pygame.Rect(i*BLOCK_SIZE,k*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
                if (world[i][k].state == -1):
                    pygame.draw.rect(win,BLACK,block)
                if (world[i][k].state == 2):
                    pygame.draw.rect(win,GREEN,block)
                if (world[i][k].state == 3):
                    pygame.draw.rect(win,RED,block)


    pygame.display.update()


def get_input (world):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursor_pos = pygame.mouse.get_pos()
            x_val = int(cursor_pos[0] / BLOCK_SIZE)
            y_val = int(cursor_pos[1] / BLOCK_SIZE)
            world[x_val][y_val].state = -1
    return world


def build_square_array():
    world = [[0]*BLOCK_PER_LINE for i in range(BLOCK_PER_LINE)]
    for i in range(BLOCK_PER_LINE):
        for k in range(BLOCK_PER_LINE):
            world[i][k] = Square(0,1)
    return world

# STATES:
# -1 - blocked spaces
# 0 - not visited
# 1 - visited
# 2 - goal
# 3 - end


def main(win):
    world = build_square_array()
    world[1][1].state = 2
    world[38][38].state = 3 #End
    while(1):
        world = get_input(world)
        draw_screen(win, world)




if __name__ == '__main__':
    main(WIN) 





















