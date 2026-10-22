
"""Алгоритмы поиска в числовых массивах."""


def binary_search(values, target):
    """Возвращает индекс найденного значения или None.

    Массив должен быть отсортирован по возрастанию.
    При повторяющихся значениях допустимо вернуть любое вхождение.
    """
    left = 0
    right = len(values) - 1

    # Продолжаем поиск, пока границы не пересеклись.
    while left <= right:
        middle = (left + right) // 2

        if values[middle] == target:
            return middle

        # Если значение меньше искомого, ищем в правой половине.
        if values[middle] < target:
            left = middle + 1
        else:
            # Иначе продолжаем поиск в левой половине.
            right = middle - 1

    return None
