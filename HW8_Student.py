def HW8_Student(graph):

    """
        Find the MST of the graph. Graph is given in adjacency matrix 'graph'
    """
    start_node = 0

    tree_nodes = set()

    parent = [None] * len(graph)
    distance = [float('inf')] * len(graph)


    parent[start_node] = -1
    distance[start_node] = -float('inf')

    while len(tree_nodes) < len(graph):
        min_so_far = float('inf')
        node = None

        for each in range(len(graph)):
            if each not in tree_nodes:
                if distance[each] < min_so_far:
                    min_so_far = distance[each]
                    node = each


        tree_nodes.add(node)

        for each in range(len(graph)):
            weight = graph[node][each]

            if each not in tree_nodes:
                if weight < distance[each]:
                    if weight != -1:
                        parent[each] = node
                        distance[each] = weight


    return parent
