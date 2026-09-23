from math import sqrt

MAX_VALUE = 10_000

def check_coefficients(a, b, c):
    if (abs(a) > MAX_VALUE) or (abs(b) > MAX_VALUE) or (abs(c) > MAX_VALUE):
        raise ValueError("ОШИБКА: значение вне допустимого диапазона")

    if a == 0 and b == 0:
        raise ValueError("ОШИБКА: это не уравнение, неизвестное отсутствует")

def solve(a, b, c):
    check_coefficients(a, b, c)

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
