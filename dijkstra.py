import queue

import pygame
from main import draw_screen
from main import get_input

def get_adjacent(start,world,queue): 
    x = start.x
    y = start.y
    list = []
    for x_axis in range(-1,2):
        for y_axis in range(-1,2):
            if(x + x_axis >= 0 and y + y_axis >= 0 and x+x_axis < 40 and y+y_axis < 40 and (world[x + x_axis][y + y_axis].state == 0 or world[x + x_axis][y + y_axis].state == 3)):
                if (x_axis == 0 and y_axis == 0):
                    continue
                if (world[x_axis+x][y+y_axis] in list or queue_contains(queue,world[x+x_axis][y+y_axis])):
                    continue
                world[x + x_axis][y + y_axis].backpointer = start
                world[x + x_axis][y + y_axis].cost_to_here = start.cost_to_here + 1 
                list.append((world[x + x_axis][y + y_axis].cost_to_here,world[x + x_axis][y+y_axis]))
    
    for i in range(len(list)):
        queue.put(list[i])

    return queue, world

def queue_contains(q, searched_for):
    return any((searched_for) in item for item in q.queue)

def extract_path(world,b):
    while(world[b.x][b.y].state != 2):
        if (world[b.x][b.y].state != 3):
            world[b.x][b.y].state = 4
        draw_screen(world)
        b = b.backpointer
    while(1):
        get_input(world)

        


def dijkstra(world,start):
    q = queue.PriorityQueue()
    q.put((0,start))

    while not q.empty():
        current = q.get()[1]
        if (world[current.x][current.y].state == 3):
            print("I found the goal")
            extract_path(world,current)
        if (world[current.x][current.y].state == 0):
            world[current.x][current.y].state = 1
        q, world = get_adjacent(current,world,q)
        draw_screen(world)
        get_input(world)

    print("No path found")
    while(1):
        get_input(world)
