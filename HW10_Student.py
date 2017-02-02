def HW10_Student(origin, outgoing_edges, incoming_edges):
    ######## YOUR SOLUTION GOES HERE ###########

    no_of_vertex = len(incoming_edges)

    distance = {i: float('inf') for i in range(no_of_vertex)}
    distance[origin] = 0

    for iterate in range(no_of_vertex - 1):
        for count in range(no_of_vertex):
            for vertex in outgoing_edges[count]:
                temp = distance[count] + outgoing_edges[count][vertex]

                if distance[vertex] > temp:
                    distance[vertex] = temp

    final = list(distance.values())

    return final


def optimal_value(low_stress, high_stress):

    optimal = 0

    current = len(low_stress) - 1

    while current >= 0:

        if current ==0:
            optimal = optimal + max(low_stress[0] + high_stress[0])
        else:
            low_current = low_stress[current]
            high_current = high_stress[current]
            low_prev = low_stress[current - 1]
            high_prev = high_stress[current - 1]

        #checking the optimal value for each week

            if high_current > low_current:
                if low_current + low_prev < high_current and low_current+ high_prev <= high_current:
                    optimal = optimal + high_current
                    current = current - 1

            else:
                optimal = optimal + low_current

        current = current - 1

    return optimal

# def optimal(low_stress,high_stress):
#     # the optimal value to be returned
#     optimal = 0
#
#     # starting from the last week
#     week_index = len(low_stress) - 1
#
#     #looping over all weeks
#     while week_index >=0:
#         if week_index ==0:
#             update optimal to maximum value between high_stress and low_stress (as there is no previous week value)
#
#         else:
#
#             if high_stress > low_stress:
#                 if low_stress of current+low_stress of previous week > high_stress of current week or high_stress_previous week + low_stress of current week > high_stress of current week
#                     update optimal to high_stress value of current week
#             else:
#                 automatically update optimal to low_stress value
#
#
#     return optimal value