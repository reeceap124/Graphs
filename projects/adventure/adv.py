from room import Room
from player import Player
from world import World
from util import Stack
from util import Queue

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
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
mapped_rooms = dict() # {'0': {'n': ?, 's': ?, 'e': ?, 'w': ?}}
class Map_Graph:
    def __init__(self):
        self.rooms = {}
        self.current = player.current_room.id

    

    def get_opposite(self, direction):
        if direction == 'n':
            return 's'
        if direction == 's':
            return 'n'
        if direction == 'e':
            return 'w'
        if direction == 'w':
            return 'e'

    def update_directions(self, room, direction, destination):
            self.rooms[room][direction] = destination
            self.rooms[destination][self.get_opposite(direction)] = room

    def examine_room(self, room):
        if room not in self.rooms:
            #add room with unexplored directions
            self.rooms[room] = dict()
            for direction in player.current_room.get_exits():
                self.rooms[room][direction] = '?'
        else:
            #update adjacency arrays of previous and current room
            if len(traversal_path):
                last = traversal_path[-1]
                new_current = player.current_room.id
                self.update_directions(self.current, last, new_current)
                self.current = player.current_room.id

    def check_unexplored(self, room):
        self.examine_room(room)
        for direction in self.rooms[room]:
            if direction == '?':
                return True
            else:
                return False
    
    def bfs(self, current_room):
        pass

    def explore(self, starting_room = self.current):
        # stack = Stack()
        # stack.push(starting_room)
        room = starting_room
        visited = self.rooms
        while len(visited)< len(room_graph): #while the whole graph has not been traveled
            # self.examine_room(room)
            if self.check_unexplored(room): #if there is an unexplored route, take it
                for direction in visited[room]:
                    if direction != '?':
                        traversal_path.append(direction)
                        player.travel(direction)
                        room = player.current_room
                        print("done traveling, logging, and updating")
                        return
            else: #find the nearest unexplored route
                pass
    

# mapping = Map_Graph()
# mapping





#while loop checking if visited == rooms
#Do a DFS looking for a room with no unexplored exits.
    #Track path as I do this
#When I hit this do a BFS to get nearest unexplored exit.
    #add on path as doing this







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
