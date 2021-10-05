import random

from properties import STUDENTS_AMOUNT, MAX_SCORES, MIN_SCORES, SCORE_VECTOR_LENGTH, SCORES_DATA_FILENAME

FILENAME = SCORES_DATA_FILENAME
FILE_LENGTH = STUDENTS_AMOUNT
SEPARATOR = ','


# opens and clears the file {FILENAME}, creates if it already exists
# writes {FILE_LENGTH} lines in the file
# each line consists of {SCORE_VECTOR_LENGTH} values separated by {SEPARATOR}
# ith value of any line is random number between ith value of {MIN_SCORES} and {MAX_SCORES}
def load_scores():
    scores = open(FILENAME, 'a')
    scores.truncate(0)
    for i in range(FILE_LENGTH):
        for j in range(SCORE_VECTOR_LENGTH):
            scores.write(str(random.randint(MIN_SCORES[j], MAX_SCORES[j])) + SEPARATOR)
        scores.write('\n')
    scores.close()


# gets 2D vector of scores from {FILENAME}, previously loaded by 'load_scores()'
def get_scores():
    scores_file = open(FILENAME)
    lines = scores_file.readlines()
    split = map(lambda x: x[:-2].split(SEPARATOR), lines)
    number_vectors = map(lambda x: list(map(lambda y: int(y), x)), split)
    return list(number_vectors)
