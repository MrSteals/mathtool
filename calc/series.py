import math


MAX_TERMS = 10_000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100_000

DIGITS = math.ceil(-math.log10(MAX_EPS))


def sign(n):
    """Возвращает знак очередного слагаемого ряда."""
    if n % 2 == 0:
        return -1

    return 1


def term_sqplus(n):
    """Вычисляет n-е слагаемое ряда 1/(n^2 + 1)."""
    return sign(n) / (n * n + 1)


def term_third(n):
    """Вычисляет n-е слагаемое ряда 1/(3n)."""
    return sign(n) / (3 * n)


FORMULAS = {
    "sqplus": (
        term_sqplus,
        "S = 1/(1^2+1) - 1/(2^2+1) + ..."
    ),
    "third": (
        term_third,
        "S = 1/3 - 1/6 + 1/9 - ..."
    ),
}

def check_terms(count):
    """Проверяет допустимое количество слагаемых."""
    if not 1 <= count <= MAX_TERMS:
        raise ValueError(
            "ОШИБКА: количество слагаемых должно быть от 1 до 10000"
        )


def check_eps(eps):
    """Проверяет допустимую точность вычисления."""
    if not math.isfinite(eps) or not 0 < eps <= MAX_EPS:
        raise ValueError(
            "ОШИБКА: точность должна быть больше 0 и не больше 0.0001"
        )

def sum_by_terms(term, count):
    """Вычисляет сумму ряда по заданному количеству слагаемых."""
    result = 0

    for n in range(1, count + 1):
        result += term(n)

    return result


def sum_by_eps(term, eps):
    """Вычисляет сумму ряда до достижения заданной точности."""
    result = 0
    n = 0

    while True:
        n += 1
        value = term(n)
        result += value

        if abs(value) < eps:
            return result, n

        if n >= MAX_ITERATIONS:
            raise ValueError("ОШИБКА: точность не достигнута")