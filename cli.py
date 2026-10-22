
"""Настройка командной строки mathtool."""

import argparse

from calc import integration, series, sorting
from calc.arrays import MIN_VALUE, MAX_VALUE


def build_parser():
    """Создаёт и возвращает парсер командной строки."""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description=(
            "Mathtool — консольное приложение для математических вычислений. "
            "Позволяет решать уравнения, анализировать числовые последовательности, "
            "вычислять суммы рядов и определённые интегралы, "
            "а также обрабатывать числовые массивы."
        ),
        allow_abbrev=False,
    )

    subparsers = parser.add_subparsers(dest="command")

    # Команда solve — решение уравнения.
    solve_parser = subparsers.add_parser(
        "solve",
        help="решение линейных и квадратных уравнений",
        allow_abbrev=False,
    )

    solve_parser.add_argument(
        "-a",
        type=int,
        help="коэффициент A при x^2 (целое число)",
    )
    solve_parser.add_argument(
        "-b",
        type=int,
        help="коэффициент B при x (целое число)",
    )
    solve_parser.add_argument(
        "-c",
        type=int,
        help="коэффициент C (целое число)",
    )

    # Команда stats — статистическая обработка чисел.
    stats_parser = subparsers.add_parser(
        "stats",
        help="статистическая обработка числовой последовательности",
        allow_abbrev=False,
    )

    stats_parser.add_argument(
        "--input",
        help="путь к файлу с числовой последовательностью",
    )

    # Команда series — вычисление суммы ряда.
    series_parser = subparsers.add_parser(
        "series",
        help="вычисление суммы числового ряда",
        allow_abbrev=False,
    )

    series_parser.add_argument(
        "--func",
        choices=sorted(series.FORMULAS),
        required=True,
        help="название вычисляемого числового ряда",
    )

    series_group = series_parser.add_mutually_exclusive_group(
        required=True
    )

    series_group.add_argument(
        "--terms",
        type=int,
        help="количество слагаемых",
    )

    series_group.add_argument(
        "--eps",
        type=float,
        help="требуемая точность вычисления суммы ряда",
    )

    # Команда integrate — численное интегрирование.
    integrate_parser = subparsers.add_parser(
        "integrate",
        help="численное вычисление определённого интеграла",
        allow_abbrev=False,
    )

    integrate_parser.add_argument(
        "--func",
        choices=sorted(integration.FORMULAS),
        required=True,
        help="название подынтегральной функции",
    )

    integrate_parser.add_argument(
        "--from",
        dest="start",
        type=float,
        required=True,
        help="нижний предел интегрирования",
    )

    integrate_parser.add_argument(
        "--to",
        dest="end",
        type=float,
        required=True,
        help="верхний предел интегрирования",
    )

    integrate_parser.add_argument(
        "--steps",
        type=int,
        required=True,
        help="количество шагов интегрирования",
    )

    # Команда fill — генерация массива случайных чисел.
    fill_parser = subparsers.add_parser(
        "fill",
        help="генерация массива случайных чисел",
        allow_abbrev=False,
    )

    fill_parser.add_argument(
        "-c",
        "--count",
        type=int,
        required=True,
        help="количество элементов массива",
    )

    fill_parser.add_argument(
        "--min",
        type=int,
        default=MIN_VALUE,
        help="минимальное значение элементов",
    )

    fill_parser.add_argument(
        "--max",
        type=int,
        default=MAX_VALUE,
        help="максимальное значение элементов",
    )

    fill_parser.add_argument(
        "--seed",
        type=int,
        help="начальное значение генератора случайных чисел",
    )

    fill_parser.add_argument(
        "-o",
        "--output",
        help="файл для сохранения массива",
    )

    # Команда sort — сортировка массива.
    sort_parser = subparsers.add_parser(
        "sort",
        help="сортировка массива",
        allow_abbrev=False,
    )

    sort_parser.add_argument(
        "-m",
        "--method",
        choices=sorted(sorting.METHODS),
        required=True,
        help="метод сортировки",
    )

    sort_parser.add_argument(
        "--order",
        choices=["asc", "desc"],
        default="asc",
        help="направление сортировки",
    )

    sort_parser.add_argument(
        "-i",
        "--input",
        help="файл с исходным массивом",
    )

    sort_parser.add_argument(
        "-o",
        "--output",
        help="файл для сохранения результата",
    )

    # Команда search — двоичный поиск.
    search_parser = subparsers.add_parser(
        "search",
        help="поиск элемента в массиве",
        allow_abbrev=False,
    )

    search_parser.add_argument(
        "-v",
        "--value",
        type=int,
        required=True,
        help="искомое значение",
    )

    search_parser.add_argument(
        "-i",
        "--input",
        help="файл с исходным массивом",
    )

    return parser
