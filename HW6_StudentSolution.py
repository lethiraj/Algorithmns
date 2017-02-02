def HW6_StudentSolution(rallies):
    output = []
    duration = 0
    start_time = 0
    index_dict = {}

    for i in range(0,len(rallies)):
        index_dict[rallies[i]] = i
    print(index_dict)

    for current in sorted(rallies,key=lambda x:x[1]):
        duration = duration + current[0]
        if duration <= current[1]:
            output.append((index_dict[current], start_time))
            start_time = start_time + current[0]
        else:
            return []

    return output
