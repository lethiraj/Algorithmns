from collections import Counter

def HW2_Student(hospitalCount, studentCount, hospPrefLists, studentPrefLists, hospOpenSlots):
    unmatchedHospital = set(range(1, hospitalCount + 1))
    studentToHospital = {}
    studentTrack = {i: 0 for i in unmatchedHospital}

    while unmatchedHospital:
        i = list(unmatchedHospital)[0]
        currentHospitalPref = hospPrefLists[i]
        preferredStudent = currentHospitalPref[studentTrack[i]]

        if preferredStudent not in studentToHospital:
            studentToHospital[preferredStudent] = i
            if list(studentToHospital.values()).count(i) == hospOpenSlots[i]:
                unmatchedHospital.remove(i)

        else:
            originalMatch = studentToHospital[preferredStudent]
            if studentPrefLists[preferredStudent].index(i) < studentPrefLists[preferredStudent].index(originalMatch):
                studentToHospital[preferredStudent] = i
                unmatchedHospital.add(originalMatch)
                if list(studentToHospital.values()).count(i) == hospOpenSlots[i]:
                    unmatchedHospital.remove(i)

        studentTrack[i] += 1

    matchedlist = [(i, j) for j, i in studentToHospital.items()]

    return matchedlist
