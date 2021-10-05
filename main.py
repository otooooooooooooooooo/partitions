from score_file_IO import load_scores, get_scores
from partition import Partition
from student import Student
from visualization import graph_partitions

if __name__ == '__main__':
    load_scores()  # generates new data
    students = list(Student.get_students(get_scores()))  # transforms data to student objects

    print('Students:')
    for student in students:
        print(student.to_string())

    # creates 2 partitions for students
    # and prints out the statistics
    partitions = Partition(students, Partition.partition1), Partition(students, Partition.partition2)
    for p in partitions:
        print('\nPartition N' + str(partitions.index(p) + 1) + ":")
        print(p.to_string())
        print('Groups:')
        for group in p.student_groups:
            print(group.to_string())

    graph_partitions(partitions[0], partitions[1])

