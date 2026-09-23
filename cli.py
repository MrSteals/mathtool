import argparse

def build_parser():
    parser = argparse.ArgumentParser(
        prog='mathtool',
        description='mathtool — расчёты над уравнениями и числовыми последовательностями',
        allow_abbrev=False
    )

    subparsers = parser.add_subparsers(dest='command')

    # Команда solve — решение уравнения
    solve_parser = subparsers.add_parser(
        'solve',
        help='решение уравнения',
        allow_abbrev=False
    )

    solve_parser.add_argument(
        '-a',
        type=int,
        help='коэффициент A'
    )
    solve_parser.add_argument(
        '-b',
        type=int,
        help='коэффициент B'
    )
    solve_parser.add_argument(
        '-c',
        type=int,
        help='коэффициент C'
    )

    # Команда stats — статистическая обработка чисел
    stats_parser = subparsers.add_parser(
        'stats',
        help='вычисление показателей числовой последовательности',
        allow_abbrev=False
    )

    stats_parser.add_argument(
        '--input',
        help='имя файла с числами'
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
        help='имя ряда'
    )

    series_group = series_parser.add_mutually_exclusive_group(
        required=True
    )

    series_group.add_argument(
        '--terms',
        type=int,
        help='количество слагаемых'
    )

    series_group.add_argument(
        '--eps',
        type=float,
        help='точность вычисления'
    )

    # Команда integrate — численное интегрирование
    integrate_parser = subparsers.add_parser(
        'integrate',
        help='вычисление определённого интеграла',
        allow_abbrev=False
    )

    integrate_parser.add_argument(
        '--func',
        required=True,
        help='имя подынтегральной функции'
    )

    integrate_parser.add_argument(
        '--from',
        dest='start',
        type=float,
        required=True,
        help='нижний предел интегрирования'
    )

    integrate_parser.add_argument(
        '--to',
        dest='end',
        type=float,
        required=True,
        help='верхний предел интегрирования'
    )

    integrate_parser.add_argument(
        '--steps',
        type=int,
        required=True,
        help='количество шагов интегрирования'
    )

    return parser
