from room import Room
from player import Player
from world import World
from util import Stack, Queue

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
traversal_path = []
stack = Stack()
visited = set()
exits_visited = set()
queue = Queue()
directions = ["n", "s", "e", "w"]
reverse = {"n":"s", "s":"n", "e":"w", "w":"e"}
current_room_id = player.current_room.id
current_room = world.starting_room

visited.add(current_room_id)
while len(visited) != len(room_graph):
    exits = current_room.get_exits()
    exits_visited.add(current_room)
    if current_room.id not in visited:
        visited.add(current_room.id)

    if "n" in exits and current_room.get_room_in_direction("n") not in exits_visited:
        #add path
        traversal_path.append("n")
        stack.push("n")
        #update current room
        current_room = current_room.get_room_in_direction("n")
    #do for all directions
    elif "s" in exits and current_room.get_room_in_direction("s") not in exits_visited:
        traversal_path.append("s")
        stack.push("s")
        current_room = current_room.get_room_in_direction("s")
    elif "e" in exits and current_room.get_room_in_direction("e") not in exits_visited:
        traversal_path.append("e")
        stack.push("e")
        current_room = current_room.get_room_in_direction("e")
    elif "w" in exits and current_room.get_room_in_direction("w") not in exits_visited:
        traversal_path.append("w")
        stack.push("w")
        current_room = current_room.get_room_in_direction("w")
    
    else:
    # remove the last valid direction from the stack
        current_path = stack.pop()
    # get the reverse direction from the reverse dictionary
        reverse_path = reverse.get(current_path)
    # add the reverse direction to the traversal path
        traversal_path.append(reverse_path)
    # sets current room in reverse direction
        current_room = current_room.get_room_in_direction(reverse_path)
        
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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
