
class Stack():
    def __init__(self):
        self.stack = []
        self.last = self.size() - 1
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph():
    def __init__(self):
        self.vertices = {}

    def add(self, v1, v2):
        if v1 not in self.vertices:
            self.vertices[v1] = set()
        if v2 not in self.vertices:
            self.vertices[v2] = set()
        self.vertices[v2].add(v1)

    def getNeighbors(self, vertex):
        return self.vertices[vertex]

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# testGraph = Graph()
# for a,b in test_ancestors:
#     testGraph.add(a,b)
# print(testGraph.vertices)

def earliest_ancestor(ancestors, starting_node):
    #depth first
    #looking for no neighbors not in queue
        #i.e. end of the line
    #we want the longest path/farthest item
        #need to attach paths to compare distance traveled
    # check for lowest value and return
    ancestor_graph = Graph()
    for a, b in ancestors:
        ancestor_graph.add(a, b)

    stack = Stack()    
    visited = set()
    stack.push([starting_node])

    oldest_ancestor = -1
    longest_path = [starting_node]
    
    

    while stack.size():
        current = stack.pop()
        vertex = current[-1]
        if (len(current) > len(longest_path)) or (len(current) == len(longest_path) and vertex < oldest_ancestor):
            longest_path = current
            oldest_ancestor = longest_path[-1]
        if vertex not in visited:
            visited.add(vertex)

            neighbors = ancestor_graph.getNeighbors(vertex)
            for neighbor in neighbors:
                newPath = current.copy()
                newPath.append(neighbor)
                stack.push(newPath)
    return oldest_ancestor

