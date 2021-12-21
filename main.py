import pygame
from pygame.constants import K_SPACE, K_r
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
BLUE = (0,100,255)

#Phases for different part of the program
creating_phase = True
goal_phase = True
end_phase = True
start = 0
end = 0

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
    global goal_phase
    global end_phase
    global start 
    global end
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if (creating_phase):
            if event.type == pygame.MOUSEBUTTONUP:
                cursor_pos = pygame.mouse.get_pos()
                x_val = int(cursor_pos[0] / BLOCK_SIZE)
                y_val = int(cursor_pos[1] / BLOCK_SIZE)
                if (goal_phase):
                    world[x_val][y_val].state = 2
                    start = world[x_val][y_val]
                    goal_phase = False
                elif (end_phase):
                    world[x_val][y_val].state = 3
                    end = world[x_val][y_val]
                    end_phase = False
                else:
                    world[x_val][y_val].state = -1
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                creating_phase = False
            elif event.key == K_r:
                creating_phase = True
                goal_phase = True
                end_phase = True
                start = 0
                end = 0
                main()
    return world


def build_square_array(): #Creates a matrix of squares 
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


def main():
    world = build_square_array() #Creates our array of squares
    while(creating_phase): #Waits for us to place the blocks 
        world = get_input(world)
        draw_screen(world)
    
    #dijkstra.dijkstra(world,start)
    a_star.a_star(world,start, end)



if __name__ == '__main__':
    main() 





















