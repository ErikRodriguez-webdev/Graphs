from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
traversal_path = []

# YOUR CODE HERE------------------------------------


def store_unexplored_exits():
    # stores and creates dictionary in dictionary with directions as keys and room ids as values
    for new_exit in player.current_room.get_exits():
        rooms[player.current_room.id][new_exit] = '?'


def random_direction(room_id):
    # find unexplored room to travel to and returns direction
    for direction in rooms[room_id]:
        if rooms[room_id][direction] == '?':
            return direction

    # if we reach here it means we did not find an unexplored room
    # remove last room visited
    visited.pop()

    # for loop through last room id in visited and move away from room_id
    for new_direction, room_num in rooms[visited[-1]].items():
        if room_num == room_id:
            return inverse(new_direction)


def inverse(direction):
    # walk backwards by flipping direction
    reverse = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
    return reverse[direction]


def room_traversal():
    # visit all rooms with room traversal
    visited.append(player.current_room.id)
    path.append(player.current_room.id)

    # store in dictionary and fill room exits with unexplored '?'
    # ex: { 0: { n:? e:? s:? w:? } }
    rooms[player.current_room.id] = dict()
    store_unexplored_exits()

    while len(rooms) < len(room_graph):
        print(player.current_room.id)
        # move towards unexplored room returning direction
        # ex: { 0: { n:? e:? s:? w:? } } so n
        move = random_direction(player.current_room.id)

        # player travel forward in direction and append to traversal path
        player.travel(move)
        traversal_path.append(move)

        # check if room id is not the same as previous room
        if player.current_room.id is not visited[-1]:
            # then append room to visited and path
            visited.append(player.current_room.id)
            # add new unexplored rooms
            path.append(player.current_room.id)

        # check if room id not in rooms dictionary
        if player.current_room.id not in rooms:
            # then add to dictionary of rooms and set value as an empty dictionary
            rooms[player.current_room.id] = dict()
            store_unexplored_exits()

        # check if current room direction value and room have not been stored
        # ex: { 0: { n:2 ... }
        #       2: { s:0 ... } }
        if rooms[player.current_room.id][inverse(move)] == '?':
            # then store with previous room id and direction to current room
            rooms[visited[-2]][move] = player.current_room.id
            # also store with current room id and inverse direction to last room
            rooms[player.current_room.id][inverse(move)] = visited[-2]


rooms = dict()
visited = list()
path = list()

# initialize traversal
room_traversal()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
