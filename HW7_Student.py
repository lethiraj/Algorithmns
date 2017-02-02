import queue


def HW7_Student(start_node, end_node, graph):
    """
        Find the smallest weighted path between start_node and end_node
        The first number of graph's adjacency list is the weight of it's node
    """

    distance = {i: float('inf') for i in graph}
    parent = {i: None for i in distance}
    distance[start_node] = 0
    heap = queue.PriorityQueue()
    heap.put((distance.get(start_node), start_node))

    for vertex, cost in distance.items():
        heap.put((cost, vertex))

    while not heap.empty():

        current = heap.get()
        adjacent = graph[current[1]][1:]

        for next in adjacent:
            temp_distance = distance[current[1]] + graph[next][0]

            if distance[next] > temp_distance:
                heap.put((temp_distance, next))
                parent[next] = current[1]
                distance[next] = temp_distance

    if parent[end_node] is None:
        return []

    path = list()
    last_node = int(end_node)

    while True:

        addition = parent[end_node]
        path.append(addition)
        if addition == start_node:
            break
        else:
            end_node = addition

    path = list(reversed(path))
    path.append(last_node)
    print(sum(graph[i][0] for i in path))
    return path
