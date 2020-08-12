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


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("You can't do that, bud.")


def earliest_ancestor(ancestors, starting_node):
    # initiate the g
    g = Graph()

    # for loop through all ancestors
    for pair in ancestors:
        # add vertices into the g
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        # add edges to make connections between vertices
        g.add_edge(pair[1], pair[0])

    print(f'g vertices {g.vertices}')

    # initiate the stack
    s = Stack()
    s.push([starting_node])

    print(f'stack list {s.stack}')

    # set ancestor to -1 for test when starting node has no ancestor
    ancestor = -1
    # set path_length to 0
    path_max_length = 1

    # while loop through size of stack > 0
    while s.size() > 0:
        # grab path from back of stack list
        path = s.pop()
        # grab last vertex in path
        vertex = path[-1]

        if (len(path) >= path_max_length and vertex < ancestor) or (len(path) > path_max_length):
            ancestor = vertex
            path_max_length = len(path)

        for next_vertex in g.vertices[vertex]:
            path_copy = list(path)
            path_copy.append(next_vertex)
            s.push(path_copy)

    # return ancestor
    return ancestor
