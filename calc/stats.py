import math


def sum_values(values):
    result = 0

    for value in values:
        result += value

    return result


def mean(values):
    return sum_values(values) / len(values)


def sum_squares(values):
    result = 0

    for value in values:
        result += value ** 2

    return result


def root_mean_square(values):
    return math.sqrt(sum_squares(values) / len(values))


def sum_squared_deviations(values):
    average = mean(values)
    result = 0

    for value in values:
        difference = value - average
        result += difference ** 2

    return result


def variance(values):
    return sum_squared_deviations(values) / len(values)


def standard_deviation_population(values):
    return math.sqrt(variance(values))


def standard_deviation(values):
    if len(values) < 2:
        return None

    return math.sqrt(sum_squared_deviations(values) / (len(values) - 1))


def minimum(values):
    result = values[0]

    for value in values:
        if value < result:
            result = value

    return result


def maximum(values):
    result = values[0]

    for value in values:
        if value > result:
            result = value

    return result


def count_positive(values):
    result = 0

    for value in values:
        if value > 0:
            result += 1

    return result


def count_negative(values):
    result = 0

    for value in values:
        if value < 0:
            result += 1

    return result