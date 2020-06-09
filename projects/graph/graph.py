"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

        # add verts
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # set of edges from this vert
        self.vertices[vertex_id] = set()

        # add edges
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)  # for v1 neighbors v2 got added as neighbor to v1
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)  # add v2 as a neihbor to v1
        else:
            raise IndexError("Vertex does not exist")

            # get neighbors for a vert
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

        # breadth first search traversal
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # empty queue and enqueue the starting vertex
        q = Queue()
        q.enqueue(starting_vertex)
        # store visted vertices
        visited = set()
        # While the queue is not empty...
        # repeat until queue is empty
        while q.size() > 0:
            # dequeue first vert
            v = q.dequeue()
            # If that vert had not been visited...
            # n(1) time
            # if its not visited:
            if v not in visited:
                # Lets visit it
                print(v)
                # Will add all of its neighbors to the back of our queue
                # mark as visited
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

                # depth first
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        # keep track of our visited nodes:
        visited = set()
        # will repeat until our queue is empty:
        while s.size() > 0:
            # dequeue our first vert
            v = s.pop()
            # if not visited:
            if v not in visited:
                # will mark it as visited
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, vistied=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # create our set:
       if visited is None:
            visited = set()
            # add our starting vertex to visted:
        visited.add(starting_vertex)
        print(starting_vertex)
        for next_vert in self.vertices[starting_vertex]:
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Lets create our empty queue and enqueue
        q = Queue()
        q.enqueue([starting_vertex])
        # Creating our set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Will dequeue our first path
            path = q.dequeue()
            # Now grab our last vertex from our path
            last_vertex = path[-1]
            # If that vertex has not visited:
            if last_vertex not in visited:
                # lets check if it's the target
                if last_vertex == destination_vertex:
                    # if it is, lets return our path
                    return path
                    # Marking as visited
                visited.add(last_vertex)
                # Then will add our path to its neighbors to the back of our queue
                for next_vertex in self.get_neighbors(last_vertex):
                    q.enqueue(path + [next_vert])

                for next_vertex in self.get_neighbors(last_vertex):
                    new_path = path.copy()
                    new_path.append(next_vertex)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Lets create our empty queue and enqueue
        s = Stack()
        s.push([starting_vertex])
        # lets creat our set to store our visited vertices
        visited = set()
        # While our queue is not empty
        while s.size() > 0:
            # lets dequeue our first path
            path = s.pop()
            # grab the last vertex from our path
            last_vertex = path[-1]
            # if that vertex has not been visited
            if last_vertex not in visited:
                # check target
                if last_vertex == destination_vertex:
                    # if so, will return path
                    return path
                    # Now will mark it as visited.
                visited.add(last_vertex)
                # now lets add a path to its neighbors to the back of our queue
                for next_vertex in self.get_neighbors(last_vertex):
                    s.push(path + [next_vert])

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()

        if path == None:
            path = []

        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for child in self.get_neighbors(starting_vertex):
            if child not in visited:
                new_path = self.dfs_recursive(child, destination_vertex, visted, path)

                if new_path:
                    return new_path


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
    print(graph.vertices)

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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
