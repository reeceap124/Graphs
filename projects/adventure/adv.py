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
class Map_Graph:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        if room == None:
            breakpoint()
        if room not in self.rooms:
            #add room with unexplored directions
            self.rooms[room] = {}
            for direction in player.current_room.get_exits():
                self.rooms[room][direction] = '?'

    def get_opposite(self, direction):
        if direction == 'n':
            return 's'
        if direction == 's':
            return 'n'
        if direction == 'e':
            return 'w'
        if direction == 'w':
            return 'e'

    def update_directions(self, room,  direction):
        opposite = self.get_opposite(direction)
        self.rooms[room][direction] = player.current_room.id
        if player.current_room.id not in self.rooms:
            self.add_room(player.current_room.id)
        self.rooms[player.current_room.id][opposite] = room
        room = player.current_room.id

    def check_unexplored(self, room):
        if room not in self.rooms:
            self.add_room(room)
            return True
        for direction in self.rooms[room]:
            if self.rooms[room][direction] == '?':
                return True
        return False
    
    def find_nearest_unexplored(self, current_room):
        visited_set = set()
        queue = Queue() #for tracking steps
        queue.enqueue([])
        pathway = Queue() #for tracking the route taken while searching for route
        pathway.enqueue([current_room])
        start_room = player.current_room
        while pathway.size():
            
            path = queue.dequeue()
            cur_route = pathway.dequeue()
            cur_room = cur_route[-1]
            if cur_room not in visited_set:
                for route in self.rooms[cur_room]:
                    #resets the player location as we test out different routes
                    player.current_room = start_room
                    #Check to see if there's an unexplored route
                    if self.rooms[cur_room][route] == '?':
                        newPath = path.copy()
                        newPath.append(route)
                        return newPath
                    #Otherwise add it to visited and check if there's any unvisited neighbors
                    visited_set.add(cur_room)
                    if self.rooms[cur_room][route] not in visited_set:
                         newPath = path.copy()
                         newPath.append(route)
                         #traveling like this helped to clean up path and route issues
                         for p in newPath:
                             player.travel(p)
                         queue.enqueue(newPath)
                         newRoute = cur_route.copy()
                         newRoute.append(player.current_room.id)
                         pathway.enqueue(newRoute)



                


    def explore(self, starting_room): 
        room = starting_room
        # while the whole graph has not been traveled
        while len(self.rooms)< len(room_graph): 
            # if there is an unexplored route, take it
            if self.check_unexplored(room): 
                for direction in self.rooms[room]:
                    if self.rooms[room][direction] == '?':
                        traversal_path.append(direction)
                        player.travel(direction)
                        self.update_directions(room, direction)
                        room = player.current_room.id
                        break
                #find the nearest unexplored route none found in current room    
            else: 
                start_at = player.current_room
                travel_along=self.find_nearest_unexplored(player.current_room.id)
                #make sure we reset after testing out the different routes
                player.current_room = start_at 
                for direction in travel_along:
                    traversal_path.append(direction)
                    player.travel(direction)
                    self.update_directions(room, direction)
                    room = player.current_room.id

    

mapping = Map_Graph()
mapping.explore(player.current_room.id)







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