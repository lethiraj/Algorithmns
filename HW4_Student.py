from collections import deque
import math
import queue


def HW4_Student(start_node, graph):
    ################# YOUR CODE GOES HERE ##################

    visited_node = {i : False for i in graph}
    distance_node = {i: -1 for i in graph}
    visited_node[start_node] = True
    distance_node[start_node] = 0

    bfsq = deque()
    bfsq.append(start_node)
    while bfsq:
        current_node = bfsq.popleft()
        current_adjacent = graph[current_node]
        for i in current_adjacent:
            if visited_node[i] == False:
                visited_node[i] = True
                bfsq.append(i)
                distance_node[i] = distance_node[current_node] + 1

    return list(distance_node.values())
