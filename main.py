import pygame
import a_star
import dijkstra
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
YELLOW = (255,255,0)
BLUE = (0,0,255)

creating_phase = True

class Square():
    def __init__(self, backpointer, state, cost_to_here,x, y):
        self.backpointer = backpointer
        self.state = state
        self.cost_to_here = cost_to_here
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        return (self.cost_to_here < other.cost_to_here)

    def __gt__(self, other):
        return (self.cost_to_here > other.cost_to_here)


def draw_screen (world):
    WIN.fill(WHITE)

    for i in range(1,BLOCK_PER_LINE):
        line_y = pygame.Rect(i * BLOCK_SIZE,0,1,SIZE)
        pygame.draw.rect(WIN,BLACK,line_y)
        
        line_x = pygame.Rect(0, i * BLOCK_SIZE,SIZE,1)
        pygame.draw.rect(WIN,BLACK,line_x)
    
    for i in range (BLOCK_PER_LINE):
        for k in range (BLOCK_PER_LINE):
            if (world[i][k] != 0):
                block = pygame.Rect(i*BLOCK_SIZE,k*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
                if (world[i][k].state == -1):
                    pygame.draw.rect(WIN,BLACK,block)
                if (world[i][k].state == 1):
                    pygame.draw.rect(WIN,YELLOW, block)
                if (world[i][k].state == 2):
                    pygame.draw.rect(WIN,GREEN,block)
                if (world[i][k].state == 3):
                    pygame.draw.rect(WIN,RED,block)
                if (world[i][k].state == 4):
                    pygame.draw.rect(WIN,BLUE,block)


    pygame.display.update()


def get_input (world):
    global creating_phase
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if (creating_phase):
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_pos = pygame.mouse.get_pos()
                x_val = int(cursor_pos[0] / BLOCK_SIZE)
                y_val = int(cursor_pos[1] / BLOCK_SIZE)
                world[x_val][y_val].state = -1  
            if event.type == pygame.KEYDOWN:
                creating_phase = False
    return world


def build_square_array():
    world = [[0]*BLOCK_PER_LINE for i in range(BLOCK_PER_LINE)]
    for i in range(BLOCK_PER_LINE):
        for k in range(BLOCK_PER_LINE):
            world[i][k] = Square(0,0, 0,i,k)
    return world

# STATES:
# -1 - blocked spaces
# 0 - not visited
# 1 - visited
# 2 - goal
# 3 - end
# 4 - Path back


def main(win):
    world = build_square_array()
    world[0][0].state = 2
    start = world[0][0]
    world[39][39].state = 3 #End
    while(creating_phase):
        world = get_input(world)
        draw_screen(world)
    
    #dijkstra.dijkstra(world,start)
    a_star.a_star(world,start)



if __name__ == '__main__':
    main(WIN) 





















