from utils import Stack, Graph


def earliest_ancestor(ancestors, starting_node):
    # initiate the graph
    graph = Graph()

    # for loop through all ancestors
    for pair in ancestors:
        # add vertices into the graph
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # add edges to make connections between vertices
        graph.add_edge(pair[1], pair[0])

    print(f'graph vertices {graph.vertices}')

    # initiate the stack
    s = Stack()
    s.push([starting_node])

    # set ancestor to -1 for test when assuming starting node has no ancestor
    ancestor = -1
    # set path_length to starting node 1
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

        # no get neighbor method in graph class instead doing a lookup of vert in graph dictionary
        for next_vertex in graph.vertices[vertex]:
            path_copy = list(path)
            path_copy.append(next_vertex)
            s.push(path_copy)

    # return ancestor
    return ancestor
