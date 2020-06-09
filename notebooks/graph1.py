class Graph:

    def __init__(self):
        self.vertices = {}

        # add verts
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()  # set of edges from this vert

        # like a set in python yet you cannot have any duplicates
        # were using a set to get order one lookup like a hash table
        # order one lookup

        # add edges
    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)  # for v1 neighbors v2 got added as neighbor to v1
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)  # add v2 as a neighbor to v1
        else:
            raise IndexError("Vertex does not exist")
        # get neighbors for a vert

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
        # breadth first search traversal

    def bft(self, starting_vertex_id):
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex_id)
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty....
        while q.size() > 0:
                # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            # n(1) time
            if v not in visited:
                # Visit it
                print(v)
                # Mark it as visted...
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
        # depth first reversal ???


g = Graph()

# add edges between these:
g.add_vertex('B')
g.add_vertex('C')

g.add_edge('B',  'C')
# add the oppoite as well
g.add_edge('C',  'B')

# print(g.get_neighbors('B'))
# print(g.get_neighbors('C'))
# print('+-----------------+')
# print(g.vertices)
g.bft('A')
