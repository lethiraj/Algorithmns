class HW3_Student_Solution:
    def __init__(self, in_vector):
        """
        The constructor exists only to initialize variables. You do not need to change it.
        :param in_vector: The vector given from the file, as a list
        """
        self.in_vector = in_vector

    def output_vector(self):
        """
        This method must be filled in by you. You may add other methods and subclasses as you see fit,
        but they must remain within the HW3_Student_Solution class.
        :return: a correct output vector, as a Python list
        """
        final = []
        current = sum(self.in_vector)
        print(len(self.in_vector))
        final.append(current)
        for i in range(0, len(self.in_vector) - 1):
            current = current - self.in_vector[i]

            final.append(current)
        # <---  Question 2 --->
        # current = sum(self.in_vector)
        # final.append(current)
        #
        # for i in range(0,len(self.in_vector)-1):
        #     current = current - self.in_vector[i]
        #     newc = current * (i+2)
        #     print(newc)
        #     final.append(newc)

        return final