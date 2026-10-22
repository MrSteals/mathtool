
"""Алгоритмы сортировки числовых массивов."""

from calc.arrays import MIN_VALUE, MAX_VALUE


def not_in_order(a, b, descending=False):
    """Проверяет, находятся ли два значения не в заданном порядке."""
    if descending:
        return a < b
    return a > b


def bubble(values, descending=False):
    """Сортирует список пузырьковым методом."""
    n = len(values)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if not_in_order(values[j], values[j + 1], descending):
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True

        if not swapped:
            break


def selection(values, descending=False):
    """Сортирует список методом выбора."""
    n = len(values)

    for i in range(n - 1):
        best = i

        for j in range(i + 1, n):
            if not_in_order(values[best], values[j], descending):
                best = j

        values[i], values[best] = values[best], values[i]


def insertion(values, descending=False):
    """Сортирует список методом вставок."""
    n = len(values)

    for i in range(1, n):
        current = values[i]
        j = i

        while (
            j > 0
            and not_in_order(values[j - 1], current, descending)
        ):
            values[j] = values[j - 1]
            j -= 1

        values[j] = current


def counting(values, descending=False):
    """Сортирует список методом подсчёта."""
    counts = [0] * (MAX_VALUE - MIN_VALUE + 1)

    # Подсчитываем количество каждого значения.
    for value in values:
        if not MIN_VALUE <= value <= MAX_VALUE:
            raise ValueError(
                f"Значение {value} вне диапазона "
                f"{MIN_VALUE}..{MAX_VALUE}"
            )

        counts[value - MIN_VALUE] += 1

    # При сортировке по убыванию обходим счётчики в обратном порядке.
    numbers = range(len(counts))
    if descending:
        numbers = range(len(counts) - 1, -1, -1)

    # Записываем значения в исходный список.
    k = 0
    for number in numbers:
        for _ in range(counts[number]):
            values[k] = number + MIN_VALUE
            k += 1


METHODS = {
    "bubble": bubble,
    "selection": selection,
    "insertion": insertion,
    "counting": counting,
}
