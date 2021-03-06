from room import Room
from player import Player
from world import World
from util import Queue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_graph = {}
traversal_path = []
visited = set()

def traverse(player):
    visited.add(player.current_room)
    while len(visited) < len(room_graph):
        x = bfs(player.current_room)
        for room , direction in x:
            if direction == None:
                continue
            traversal_path.append(direction)
            player.travel(direction)
            visited.add(room)


def bfs(starting_room):
    to_visit = Queue()

    to_visit.enqueue([(starting_room,None)])

    attempted_rooms = set()

    while to_visit.size() > 0:

        path = to_visit.dequeue()

        room = path[-1][0]

        if room not in attempted_rooms:

            if room not in visited:

                return path
            
            attempted_rooms.add(room)

            for exit in room.get_exits():
                connected_room = room.get_room_in_direction(exit)
                to_visit.enqueue(path+[(connected_room,exit)])

            
traverse(player)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:

#         print("I did not understand that command.")
