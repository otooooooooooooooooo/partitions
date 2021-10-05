from properties import SCORE_VECTOR_LENGTH, MIN_SCORES, MAX_SCORES, PRIORITY_COEFFICIENTS


def is_score_vector(vector):
    if not len(vector) == SCORE_VECTOR_LENGTH:
        return False
    for i in range(SCORE_VECTOR_LENGTH):
        if not (MIN_SCORES[i] <= vector[i] <= MAX_SCORES[i]):
            return False
    return True


def validate_score_vector(vector):
    if not is_score_vector(vector):
        raise "Illegal score vector format"


def get_scaled(scores):
    validate_score_vector(scores)
    scaled = []
    for i in range(SCORE_VECTOR_LENGTH):
        scaled.append(scores[i] / MAX_SCORES[i] * PRIORITY_COEFFICIENTS[i])
    return scaled


def unified_score(scores):
    return sum(get_scaled(scores))
