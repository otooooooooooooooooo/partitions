from scaling import unified_score


class Student:
    id_counter = 0

    def __init__(self, scores):
        Student.id_counter += 1
        self.__id = Student.id_counter
        self.__scores = scores
        self.__unified_score = unified_score(scores)

    @property
    def id(self):
        return self.__id

    @property
    def scores(self):
        return self.__scores

    @property
    def unified_score(self):
        return self.__unified_score

    def to_string(self):
        return 'ID: ' + str(self.id) + ', Scores: ' + str(self.scores) + ', Unified score: ' + str(self.unified_score)

    @staticmethod
    def get_students(score_vectors):
        return list(map(lambda score_vector: Student(score_vector), score_vectors))

    @staticmethod
    def sorted_by_points(students):
        return list(sorted(students, key=lambda student: student.unified_score))


class StudentGroup:
    id_counter = 0

    def __init__(self, students):
        StudentGroup.id_counter += 1
        self.__id = StudentGroup.id_counter
        self.__students = students
        self.__average_score = StudentGroup.get_average(students)
        self.__score_range = StudentGroup.get_score_range(students)

    @property
    def id(self):
        return self.__id

    @property
    def students(self):
        return self.__students

    @property
    def average_score(self):
        return self.__average_score

    def to_string(self):
        return "Group N" + str(self.id) + ": Amount of students: " + str(len(self.students)) + ", Average score: " + str(self.average_score) + ", Score range: " + str(self.score_range)

    @property
    def score_range(self):
        return self.__score_range

    @classmethod
    def restart_id_counter(cls):
        cls.id_counter = 0

    @staticmethod
    def get_average(students):
        return sum(map(lambda student: student.unified_score, students)) / len(students)

    @staticmethod
    def get_score_range(students):
        scores = list(map(lambda student: student.unified_score, students))
        return max(scores) - min(scores)
