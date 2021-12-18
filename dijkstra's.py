import queue

def get_adjacent(x,y,world): 
    adjacent_list = []
    for x_axis in range(-1,1):
        for y_axis in range(-1,1):
            if(x + x_axis >= 0 and y + y_axis >= 0):
                if not(x+x_axis == 0 and y+y_axis == 0):
                    adjacent_list.append(world[x + x_axis][y + y_axis])
    return adjacent_list



def dijkstra(world, start, end):
    q = queue.PriorityQueue

    