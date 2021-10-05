from properties import GROUP_SIZE, GROUP_AMOUNT
from student import StudentGroup, Student


class Partition:
    def __init__(self, students, partition):
        self.__student_groups = partition(students)
        self.__range = Partition.get_average_score_range(self.__student_groups)

    @property
    def student_groups(self):
        return self.__student_groups

    @property
    def score_range(self):
        return self.__range

    def to_string(self):
        return "Groups amount: " + str(len(self.student_groups)) + ", Range of average scores: " + str(self.score_range)

    @staticmethod
    def get_average_score_range(student_groups):
        averages = list(map(lambda student_group: student_group.average_score, student_groups))
        return max(averages) - min(averages)

    @staticmethod
    def partition1(students):
        students = Student.sorted_by_points(students)
        student_lists = []
        for i in range(GROUP_AMOUNT):
            student_lists.append([])
        for i in range(GROUP_SIZE):
            for j in range(GROUP_AMOUNT):
                student_lists[j].append(students[i * GROUP_AMOUNT + j])
        StudentGroup.restart_id_counter()
        return list(map(StudentGroup, student_lists))

    @staticmethod
    def partition2(students):
        students = Student.sorted_by_points(students)
        student_lists = []
        for i in range(GROUP_AMOUNT):
            student_lists.append([])
        for i in range(GROUP_SIZE):
            for j in range(GROUP_AMOUNT):
                student_lists[j].append(students[i * GROUP_AMOUNT + j])
            student_lists = list(reversed(student_lists))
        StudentGroup.restart_id_counter()
        return list(map(StudentGroup, student_lists))
