import helper_functions
import main

def get_adjacent(start,world,queue): 
    x = start.x
    y = start.y
    list = []
    for x_axis in range(-1,2):
        for y_axis in range(-1,2):
            if(x + x_axis >= 0 and y + y_axis >= 0 and x+x_axis < 40 and y+y_axis < 40 and (world[x + x_axis][y + y_axis].state == 0 or world[x + x_axis][y + y_axis].state == 3)):
                if (x_axis == 0 and y_axis == 0):
                    continue
                if (world[x_axis+x][y+y_axis] in list or helper_functions.queue_contains(queue,world[x+x_axis][y+y_axis])):
                    continue
                world[x + x_axis][y + y_axis].backpointer = start
                list.append((0,world[x + x_axis][y+y_axis]))
    
    for i in range(len(list)):
        queue.put(list[i])

    return queue, world

def breadth_first(world,start):
    q = helper_functions.queue.Queue()
    q.put((0,start))

    while not q.empty():
        current = q.get()[1]
        if (world[current.x][current.y].state == 3):
            print("I found the goal")
            helper_functions.extract_path(world,current)
        if (world[current.x][current.y].state == 0):
            world[current.x][current.y].state = 1
        q, world = get_adjacent(current,world,q)
        main.draw_screen(world)
        main.get_input(world)

    print("No path found")
    while(1):
        main.get_input(world)
