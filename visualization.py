import matplotlib.pyplot as plt
import numpy as np


def graph_partitions(partition1, partition2):
    groups1 = partition1.student_groups
    groups2 = partition2.student_groups
    group_ids = list(map(lambda group: group.id, groups1))
    group1_avg_scores = list(map(lambda group: group.average_score, groups1))
    group2_avg_scores = list(map(lambda group: group.average_score, groups2))

    x_axis = np.arange(len(group_ids))

    plt.bar(x_axis - 0.2, group1_avg_scores, width=0.3, label='Partition 1', color='b')
    plt.bar(x_axis + 0.2, group2_avg_scores, width=0.3, label='Partition 2', color='g')
    plt.xticks(x_axis, group_ids)
    plt.legend()
    plt.xlabel('Group ID')
    plt.ylabel('Average score')
    plt.title('Partition comparison')
    plt.show()



