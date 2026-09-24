import argparse

def build_parser():
    parser = argparse.ArgumentParser(
        prog='mathtool',
        description=(
            'Mathtool — консольное приложение для математических вычислений.'
            'Позволяет решать уравнения, анализировать числовые последовательности,'
            'вычислять суммы рядов и определенные интегралы.'
        ),
        allow_abbrev=False
    )

    subparsers = parser.add_subparsers(dest='command')

    # Команда solve — решение уравнения
    solve_parser = subparsers.add_parser(
        'solve',
        help='решение линейных и квадратных уравнений',
        allow_abbrev=False
    )

    solve_parser.add_argument(
        '-a',
        type=int,
        help='коэффициент A при x^2 (целое число)'
    )
    solve_parser.add_argument(
        '-b',
        type=int,
        help='коэффициент B при x (целое число)'
    )
    solve_parser.add_argument(
        '-c',
        type=int,
        help='коэффициент C (целое число)'
    )

    # Команда stats — статистическая обработка чисел
    stats_parser = subparsers.add_parser(
        'stats',
        help='статистическая обработка числовой последовательности',
        allow_abbrev=False
    )

    stats_parser.add_argument(
        '--input',
        help='путь к файлу, содержащему числовую последовательность'
    )

    # Команда series — вычисление суммы ряда
    series_parser = subparsers.add_parser(
        'series',
        help='вычисление суммы числового ряда',
        allow_abbrev=False
    )

    series_parser.add_argument(
        '--func',
        required=True,
        help='название вычисляемого числового ряда'
    )

    series_group = series_parser.add_mutually_exclusive_group(
        required=True
    )

    series_group.add_argument(
        '--terms',
        type=int,
        help='количество слагаемых, используемых при вычислении суммы'
    )

    series_group.add_argument(
        '--eps',
        type=float,
        help='требуемая точность вычисления суммы ряда'
    )

    # Команда integrate — численное интегрирование
    integrate_parser = subparsers.add_parser(
        'integrate',
        help='численное вычисление определенного интеграла',
        allow_abbrev=False
    )

    integrate_parser.add_argument(
        '--func',
        required=True,
        help='название подынтегральной функции'
    )

    integrate_parser.add_argument(
        '--from',
        dest='start',
        type=float,
        required=True,
        help='нижний предел интегрирования (начало интервала)'
    )

    integrate_parser.add_argument(
        '--to',
        dest='end',
        type=float,
        required=True,
        help='верхний предел интегрирования (конец интервала)'
    )

    integrate_parser.add_argument(
        '--steps',
        type=int,
        required=True,
        help='количество шагов, на которые разбивается интервал интегрирования'
    )

    return parser
