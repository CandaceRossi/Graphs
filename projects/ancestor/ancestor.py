from util import Queue
# from g import Graph


def populate_graph(ancestors):
    # convert data into an adjacency list
    # for easy look up of neighbors
    # scan through ancestors and create all the verticies
    graph = {}
    for parent_child_pair in ancestors:
        parent = parent_child_pair[0]
        child = parent_child_pair[1]
        graph[parent] = set()
        graph[child] = set()

    # scan through ancestors again and build edges
    for parent_child_pair in ancestors:
        parent = parent_child_pair[0]
        child = parent_child_pair[1]
        # instead of adding verticies, I want to make edges between child and parent
        graph[child].add(parent)
    return graph


def earliest_ancestor(ancestors, starting_node):
    graph = populate_graph(ancestors)
    # print(graph)
    # generic dfs algorithm
    queue = Queue()
    visited = set()
    queue.enqueue([starting_node])

    longest_path = 1
    earliest_ancestor = -1

    while queue.size() > 0:
        current_path = queue.dequeue()
        current_vertex = current_path[-1]
        if current_vertex not in visited:
            visited.add(current_vertex)
            # Do something cool while you traverse
            if (len(current_path) > longest_path):
                longest_path = len(current_path)
                earliest_ancestor = current_vertex
            elif (len(current_path) == longest_path and current_vertex < earliest_ancestor):
                # we have a tie for longest path, choose the vertex with smallest id
                earliest_ancestor = current_vertex
            for neighbor in graph[current_vertex]:
                path_copy = list(current_path)
                path_copy.append(neighbor)
                queue.enqueue(path_copy)

    return earliest_ancestor

    # g = Graph()
    # visited = {}
    # ancestors = []
    # result = []
    # for child, parent in ancestors:
    #     #add nodes
    #     g.add_vertex(child)
    #     g.add_vertex(parent)
    #     #add egdes
    #     g.add_edges(child, parent)
    #     if child not in visited:

    # result = g.dfs_recursive()


# def get_neighbors(nodes):
#     neighbors = set()
#     for i in range(len(nodes)):
    # a neighbor for a node is any node
    # is inside adjacency list

    # check that node exists in list
    # return all neighbors
