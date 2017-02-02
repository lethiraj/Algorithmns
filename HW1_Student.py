from Marriage import Marriage
import itertools
import collections
import ctypes


class HW1_Student:
    def __init__(self, number, men, women):
        """
        The constructor exists only to initialize variables. You do not need to change it.
        :param number: The number of members
        :param men: The preference list of men, as a dictionary.
        :param women: The preference list of the women, as a dictionary.
        """
        self.num = number
        self.men = men
        self.women = women
        self.stable_matchings = []

    def perfect_match(self):

        women = [i for i in range(1, self.num + 1)]
        men = [i for i in range(1, self.num + 1)]

        perfect_natch = [list(zip(men, p)) for p in itertools.permutations(women)]

        return perfect_natch

    def stable_check(self, match):

        isStable = True

        for i in range(0, self.num):
            for j in range(0, self.num):

                # checking proiority list of men

                menpref = self.men[match[i][0]]

                # if priority of woman matched to him is lesser than another women

                if (menpref.index(match[i][1]) > menpref.index(match[j][1])):

                    # to check priority of woman who is better liked
                    womenpref = self.women[match[j][1]]

                    # checking if she likes original man better

                    if (womenpref.index(match[i][0]) < womenpref.index(match[j][0])):
                        isStable = False

                        break

                    else:
                        continue

            if (isStable == False):
                break

        return isStable

    def output_stable_matchings(self):
        """
        We are expecting the output to be a list containing stable matchings.
         - each matching is a list of marriages
        This does not have to be ordered in any specific way.
        :return: a list of stable matching instances
        """

        perfect_matches = HW1_Student.perfect_match(self)

        for i in perfect_matches:

            if (HW1_Student.stable_check(self, i)):
                self.stable_matchings.append(i)

        return self.stable_matchings
