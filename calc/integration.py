import math

MAX_STEPS = 100_000
RATIO_LOW = 0
RATIO_HIGH = 20
ROOT_LOW = -5
ROOT_HIGH = 5

def F_ratio(x):
    """Вычисляет значение функции x / (x + 1)."""
    return x / (x + 1)


def F_root(x):
    """Вычисляет значение функции sqrt(x^2 + 1)."""
    return math.sqrt(x * x + 1)

FORMULAS = {
    "ratio": (
        F_ratio,
        "F(x) = x / (x + 1)",
        RATIO_LOW,
        RATIO_HIGH,
        False
    ),
    "root": (
        F_root,
        "F(x) = sqrt(x^2 + 1)",
        ROOT_LOW,
        ROOT_HIGH,
        True
    ),
}


def check_steps(steps):
    """Проверяет допустимое количество шагов."""
    if not 1 <= steps <= MAX_STEPS:
        raise ValueError(
            "ОШИБКА: количество шагов должно быть от 1 до 100000"
        )


def check_limits(function_data, start, end):
    """Проверяет допустимость пределов интегрирования."""
    if not math.isfinite(start) or not math.isfinite(end):
        raise ValueError(
            "ОШИБКА: пределы должны быть конечными числами"
        )

    if start >= end:
        raise ValueError(
            "ОШИБКА: нижний предел должен быть меньше верхнего"
        )

    _, _, low, high, strict = function_data

    if strict:
        if start <= low or end >= high:
            raise ValueError(
                "ОШИБКА: предел вне допустимого промежутка функции"
            )
    else:
        if start < low or end > high:
            raise ValueError(
                "ОШИБКА: предел вне допустимого промежутка функции"
            )


def integrate(function, start, end, steps):
    """Вычисляет определенный интеграл методом левых прямоугольников."""
    dx = (end - start) / steps
    result = 0

    for i in range(steps):
        x = start + i * dx
        result += function(x) * dx

    return result
