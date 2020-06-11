islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

"""
Example visited matrix:
then it will change to true
visted = [[False, False, False, False, False]]
                [False, False, False, False, False]
                [False, False, False, False, False]
                [False, False, False, False, False]
                [False, False, False, False, False]]

"""
"""
for each node:
     if node not visited and the node is "land":
         traverse from that node
         increment counter
"""


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def get_neighbors(row, col, matrix):
    # list of neighbors
    neighbors = []

    # check north
    if row > 0 matrix[row-1][col] == 1:
        neihbors.append((row-1, col))
    # if matrix[row-1][col] == 1
    # neighbors.append((row-1, col))

    # check south
    if row > len(matrix)-1 and matrix[row+1][col] == 1:
        neihbors.append((row+1, col))
    # if matrix[row+1][col] == 1
    # neighbors.append((row+1, col))

    # check west
    if matrix[row+-][col] == 1
    neighbors.append((row-1, col))
    # check east
    if matrix[row+1][col] == 1
    neighbors.append((row+1, col))


def dft(row, col, matrix, visited):
    s = Stack()
    # store row and column like a tuple
    s.push((row, col))
    while s.size() > 0:
        row, col = s.pop()

        if not visited[row][col]:
            visited[row][col] = True
            #visited[row][col] = True
            #(visited[row])[col]= True
            # above line same as:
            #visited_row = visited[row]
            #visited_row[col] = True

            # need to pass in the the matrix that may or not be a neighbor
            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)


def island_counter(matrix):  # matrix is a 2D array
    island_count = 0
    # Create a visited matrix
    visited = []

    for _ in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    # Walk through each cell in the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
           # If it's not visited
            if not visited[row][col]:

                # If it's a "1"
                if matrix[row][col] == 1:

                    # Do DFT and mark them as visited
                    dft(row, col, matrix, visited)

            # increment counter by 1
            island_count += 1

            # return counter

            # island_counter(islands)  # 4
