"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices: #keeps us from overwriting a vertex unintentionally
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #use a queue
        #visited hash table
        #stop when queue is empty
        #add to queue (if not in visited)
        #queue all neighbors
        #dequeue, and add to visited
        visited = set()
        btf_queue = Queue()
        btf_queue.enqueue(starting_vertex)
        while btf_queue.size() > 0:
            print(btf_queue.queue[0])
            neighbors = self.get_neighbors(btf_queue.queue[0])
            visited.add(btf_queue.queue[0])
            btf_queue.dequeue()
            for neighbor in neighbors:
                if neighbor not in visited:
                    btf_queue.enqueue(neighbor)
            


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # print(f'Graph: {self.vertices}')
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    stack.push(neighbor)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        def inner_recursive(vertex):
            print(vertex)
            visited.add(vertex)
            neighbors = self.get_neighbors(vertex)
            if len(neighbors) > 0:
                for n in neighbors: 
                    if n not in visited:
                        inner_recursive(n)
        inner_recursive(starting_vertex)
        

            

        

        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        q = Queue()
        q.enqueue([starting_vertex])
        while q.size() > 0:
            current = q.dequeue()
            v = current[-1]
            if v not in visited:
                if v == destination_vertex:
                    return current
                visited.add(v)
                for n in self.get_neighbors(v):
                    path = current.copy()
                    path.append(n)
                    q.enqueue(path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            current = s.pop()
            v = current[-1]
            if v not in visited:
                if v == destination_vertex:
                    return current
                visited.add(v)
                for n in self.get_neighbors(v):
                    path = current.copy()
                    path.append(n)
                    s.push(path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        
        def inner_recursive(vertex, destination, path=list()):
            
            visited.add(vertex)
            path.append(vertex)
            if vertex == destination:
                return path
            for n in self.get_neighbors(vertex):
                if n not in visited:
                    new_path = inner_recursive(n, destination, path)
                    if new_path:
                        return new_path

        return inner_recursive(starting_vertex, destination_vertex, [])

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
