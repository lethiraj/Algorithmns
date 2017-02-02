from HW10_Student import *
import sys


def readFromFile(inputFile):

    origin = 0
    incoming_edges = []
    outgoing_edges = []

    with open(inputFile, 'r') as file:

        origin = int(file.readline())

        str = file.readline()

        while str != '':
            incoming_str = str.split()
            str = file.readline()
            outgoing_str = str.split()

            incoming = {}
            outgoing = {}

            it = 0
            while it != len(incoming_str):
                node = int(incoming_str[it])
                it += 1
                weight = int(incoming_str[it])
                it += 1

                incoming[node] = weight

            it = 0
            while it != len(outgoing_str):
                node = int(outgoing_str[it])
                it += 1
                weight = int(outgoing_str[it])
                it += 1

                outgoing[node] = weight

            incoming_edges.append(incoming)
            outgoing_edges.append(outgoing)

            str = file.readline()

    return [origin, outgoing_edges, incoming_edges]

def main():
    if (len(sys.argv) < 2):
        print("Please provide the input filepath as the argument")
        sys.exit()

    input_file = sys.argv[1]

    vals = readFromFile(input_file)

    origin = vals[0]
    outgoing_edges = vals[1]
    incoming_edges = vals[2]

    print("Number of nodes:" + str(len(outgoing_edges)))

    # Get the path
    shortest_path = HW10_Student(origin, outgoing_edges, incoming_edges)

    print(str(shortest_path))


if __name__ == '__main__':
    main()
