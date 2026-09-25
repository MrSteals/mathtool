from math import sqrt

MAX_VALUE = 10_000

def check_coefficients(coefficients):
    """Проверяет допустимый диапазон коэффициентов."""
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"ОШИБКА: коэффициент {name} вне допустимого диапазона")

def solve(a, b, c):
    """Решает линейное или квадратное уравнение."""
    check_coefficients({"A": a, "B": b, "C": c})

    if a == 0 and b == 0:
        raise ValueError("ОШИБКА: это не уравнение, неизвестное отсутствует")

    if a != 0:
        d = b * b - 4 * a * c

        if d > 0:
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            return 'квадратное', d, [x1, x2]

        elif d == 0:
            x = -b / (2 * a)
            return 'квадратное', d, [x]

        else:
            return 'квадратное', d, []

    else:
        x = -c / b
        return 'линейное', None, [x]
