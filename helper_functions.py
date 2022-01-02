import main
import queue

def queue_contains(q, searched_for):
    return any((searched_for) in item for item in q.queue)

def extract_path(world,b):
    while(world[b.x][b.y].state != 2):
        if (world[b.x][b.y].state != 3):
            world[b.x][b.y].state = 4
        main.draw_screen(world)
        b = b.backpointer
    while(1):
        main.get_input(world)
