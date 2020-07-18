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
class Map_Graph:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        if room not in self.rooms:
            #add room with unexplored directions
            self.rooms[room] = dict()
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

    # def examine_room(self, room):
        
            
    #     if len(traversal_path):
    #         last = traversal_path[-1]
    #         new_current = player.current_room.id
    #         self.update_directions(self.current, last, new_current)
    #         self.current = player.current_room.id
            # breakpoint()q

    def check_unexplored(self, room):
        if room not in self.rooms:
            self.add_room(room)
            return True
        for direction in self.rooms[room]:
            if self.rooms[room][direction] == '?':
                return True
        return False
    
    def find_nearest_unexplored(self, current_room): #passing in player room id
        # print('Starting the BFS\n', 'Room:', current_room)
        # # breakpoint()
        # visited_set = set()
        # queue = Queue()
        # queue.enqueue([])
        # pathway = Queue()
        # pathway.enqueue([current_room])
        # # breakpoint()
        # while pathway.size():
        #     path = queue.dequeue()
        #     cur_route = pathway.dequeue()
        #     cur_room = cur_route[-1]
        #     print('CURRENT ROOM: ', cur_room, '\n\nROOMIES: ', self.rooms)
        #     if cur_room not in visited_set:
        #         if self.check_unexplored(cur_room):
        #             traversal_path.extend(path)
        #             visited_set = set()
        #             print('found one', cur_room)
        #             return cur_room
        #         visited_set.add(cur_room)
        #         for route in self.rooms[cur_room]:
        #             print(cur_room, route)
        #             newPath = path.copy()
        #             newRoute = cur_route.copy()
        #             newPath.append(route)
        #             queue.enqueue(newPath)
        #             if player.current_room.get_room_in_direction(route).id not in visited_set:
        #                 player.travel(route)
        #                 newRoute.append(player.current_room.id)
        #                 pathway.enqueue(newRoute)
        #         print("THIS IS A BREAK 2")
                # breakpoint()
        visited = set()
        queue = Queue()
        queue.enqueue([current_room])
        while queue.size():
            path = queue.dequeue()
            room = path[-1]
            if room not in visited:
                if self.check_unexplored(room):
                    return path[-1]
                visited.add(room)
                for route in self.rooms[room]:
                    newPath = path.copy()
                    faker = player.deepcopy()
                    faker.travel(route)
                    newPath.append(faker.current_room.id)
                print('EXITING THE IF STATEMENT')
            print('EXITING THE WHILE LOOP')
        print('EXITING THE BFS')
        breakpoint()



                


    def explore(self, starting_room): ##?? Do You want a default Starging Room?
        # stack = Stack()
        # stack.push(starting_room)
        room = starting_room
        print("STARTING: ", room)
        while len(self.rooms)< len(room_graph): # while the whole graph has not been traveled
            if self.check_unexplored(room): # if there is an unexplored route, take it
                print("There are rooms to explore here", len(self.rooms))
                for direction in self.rooms[room]:
                    if self.rooms[room][direction] == '?':
                        traversal_path.append(direction)
                        player.travel(direction)
                        self.update_directions(room, direction)
                        room = player.current_room.id
                        break
                    print("THIS IS A BREAK")
                    # breakpoint()
            
            else: #find the nearest unexplored route none found in current room
                print('LENGTH IN ELSE', len(self.rooms))
                print('ELSE')
                print('ELSE')
                room = self.find_nearest_unexplored(player.current_room.id)
        print('Finished Exploring')
                
    

mapping = Map_Graph()
mapping.explore(player.current_room.id)





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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
