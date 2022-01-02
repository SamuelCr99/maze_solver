import helper_functions
import main

def get_adjacent(start,world,stack): 
    x = start.x
    y = start.y
    stack = []
    for x_axis in range(-1,2):
        for y_axis in range(-1,2):
            if(x + x_axis >= 0 and y + y_axis >= 0 and x+x_axis < 40 and y+y_axis < 40 and (world[x + x_axis][y + y_axis].state == 0 or world[x + x_axis][y + y_axis].state == 3)):
                if (x_axis == 0 and y_axis == 0):
                    continue
                if (world[x_axis+x][y+y_axis] in stack or (stack,world[x+x_axis][y+y_axis]) in stack):
                    continue
                world[x + x_axis][y + y_axis].backpointer = start
                stack.append((0,world[x + x_axis][y+y_axis]))
    
    for i in range(len(stack)):
        stack.append(stack[i])

    return stack, world

def depth_first(world,start):
    stack = []
    stack.append((0,start))

    while (len(stack) != 0):
        current = stack.pop()[1]
        if (world[current.x][current.y].state == 3):
            print("I found the goal")
            helper_functions.extract_path(world,current)
        if (world[current.x][current.y].state == 0):
            world[current.x][current.y].state = 1
        stack, world = get_adjacent(current,world,stack)
        main.draw_screen(world)
        main.get_input(world)

    print("No path found")
    while(1):
        main.get_input(world)
