from calc.arrays import MIN_VALUE, MAX_VALUE

def not_in_order(a, b, descending):
    """Проверяет, нарушен ли порядок двух элементов."""
    if descending:
        return a < b
    else:
        return a > b


def bubble(values, descending=False):
    """Сортирует массив методом пузырька."""
    n = len(values)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if not_in_order(values[j], values[j + 1], descending):
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True

        if not swapped:
            break


METHODS = {
    "bubble": bubble,
}