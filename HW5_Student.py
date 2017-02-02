def HW5_Student(graph):
    start = 0
    visited_dict = {i: False for i in graph}

    dfs = [start]

    while dfs:
        current = dfs[-1]
        visited_dict[current] = True

        current_adj = graph[current]

        for i in current_adj:

            if visited_dict[i] is False:

                dfs.append(i)
                break
            else:
                if dfs[dfs.index(current) - 1] == i:
                    continue
                else:

                    if i in dfs:

                        cycle = dfs[dfs.index(i):]
                        if (len(cycle) > 2):
                            return cycle

        if current == dfs[-1]:
            dfs.pop()

    return []
