import math
from operator import itemgetter
import itertools


def distance(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))



def closest_pair(Px,Py):

    strip = []

    if len(Px) < 4:
        minimum = float('inf')
        for i in range(0, len(Px)):
            for j in range(i + 1, len(Px)):
                temp = distance(Px[i], Px[j])
                if temp < minimum:
                    minimum = temp

        return minimum

    mid = len(Px) / 2
    first_x = Px[:int(mid)]
    second_x = Px[int(mid):]

    first_y = sorted(first_x, key=itemgetter(1))
    second_y = sorted(second_x, key=itemgetter(1))

    min_distance = min(closest_pair(first_x,first_y),closest_pair(second_x,second_y))

    mid_coordinate = Px[int(mid)][0]

    for i in Py:
        if math.fabs(i[0]-mid_coordinate) < min_distance:
            strip.append(i)

    closest_strip = float('inf')
    for i in range(len(strip)):
        for j in range(i+1,i+16):
            if j >=len(strip):
                break
            temp = distance(strip[i],strip[j])
            if temp < closest_strip:
                closest_strip = temp


    return min(closest_strip,min_distance)






def HW9_Student(points):
    ######## YOUR SOLUTION GOES HERE ###########


    sorted_xcoordinate = sorted(points, key=itemgetter(0))
    sorted_ycoordinate = sorted(points, key=itemgetter(1))


    return closest_pair(sorted_xcoordinate,sorted_ycoordinate)













