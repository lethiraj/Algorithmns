import re
import Marriage

class HW1_Utils:

    def __init__(self, file):
        """
        The constructor sets the preferences to empty dicts, and sets the file name
        :param file: name of file holding the data
        """
        self.men_preferences = {}
        self.women_preferences = {}
        self.file = file

    def men(self):
        return self.men_preferences
    def women(self):
        return self.women_preferences

    def read_file(self):
        """
        This will read the file and create the preference lists. No return
        """
        file_name = self.file
        f = open(file_name, 'r')

        self.num = int(f.readline())
        for w in range(1, self.num + 1):
            preferences = []
            line = re.split('\W+',f.readline())
            for x in range(0, self.num):
                preferences.append(int(line[x]))

            self.women_preferences[w] = preferences

        for m in range(1, self.num + 1):
            preferences = []
            line = re.split('\W+', f.readline())
            for x in range(0, self.num):
                preferences.append(int(line[x]))

            self.men_preferences[m] = preferences

    def sort_matchings(self, unsorted_list):
        """
        This takes an unsorted list of matchings and sorts it as such:
        Each matching is sorted internally by man.
        Each matching is ordered in the list by woman
        :param unsorted_list: list to be sorted
        :return: sorted version of the list
        """
        out_matchings = []
        for match in unsorted_list:
            match.sort()

        unsorted_list.sort()
        return unsorted_list 


    def compare(self, student_ans, accepted_ans):
        """
        Takes two lists of matchings, sorts them, then compares for equality.
        :param student_ans: the student's answer
        :param accepted_ans: the instructor's solution
        :return: true if they are equivalent
        """
        if student_ans == None:
            return False
        if len(student_ans) != len(accepted_ans):
            return False


        student_ans = self.sort_matchings(student_ans)
        accepted_ans = self.sort_matchings(accepted_ans)


        for m in range(0, len(student_ans)):
            for n in range(0, len(student_ans[m])):
                if not student_ans[m][n].equals(accepted_ans[m][n]):
                    return False

        return True
