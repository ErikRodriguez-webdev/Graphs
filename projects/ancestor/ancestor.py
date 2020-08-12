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

    print(graph.vertices)
