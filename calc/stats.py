import math


def sum_values(values):
    """Вычисляет сумму чисел."""
    result = 0

    for value in values:
        result += value

    return result


def mean(values):
    """Вычисляет среднее арифметическое."""
    return sum_values(values) / len(values)


def sum_squares(values):
    """Вычисляет сумму квадратов чисел."""
    result = 0

    for value in values:
        result += value ** 2

    return result


def root_mean_square(values):
    """Вычисляет среднее квадратическое."""
    return math.sqrt(sum_squares(values) / len(values))


def sum_squared_deviations(values):
    """Вычисляет сумму квадратов отклонений от среднего."""
    average = mean(values)
    result = 0

    for value in values:
        difference = value - average
        result += difference ** 2

    return result


def variance(values):
    """Вычисляет дисперсию."""
    return sum_squared_deviations(values) / len(values)


def standard_deviation_population(values):
    """Вычисляет среднее квадратическое отклонение."""
    return math.sqrt(variance(values))


def standard_deviation(values):
    """Вычисляет стандартное отклонение выборки."""
    if len(values) < 2:
        return None

    return math.sqrt(sum_squared_deviations(values) / (len(values) - 1))


def minimum(values):
    """Находит минимальное значение."""
    result = values[0]

    for value in values:
        if value < result:
            result = value

    return result


def maximum(values):
    """Находит максимальное значение."""
    result = values[0]

    for value in values:
        if value > result:
            result = value

    return result


def count_positive(values):
    """Подсчитывает количество положительных чисел."""
    result = 0

    for value in values:
        if value > 0:
            result += 1

    return result


def count_negative(values):
    """Подсчитывает количество отрицательных чисел."""
    result = 0

    for value in values:
        if value < 0:
            result += 1

    return result
