import math
import sys
import time
from cli import build_parser
from calc import equation, stats, series, integration, sorting
from calc.search import binary_search
from calc.arrays import (
    MIN_VALUE,
    MAX_VALUE,
    MAX_COUNT,
    MAX_SEARCH,
    read_array,
    write_array,
    generate_array,
)


def measure_time(name, operation, parameters):
    """Измеряет время выполнения операции и возвращает её результат."""
    start = time.perf_counter()
    result = operation(*parameters)
    elapsed = time.perf_counter() - start

    print(
        f"Время операции {name}: {elapsed:.6f} с",
        file=sys.stderr,
    )

    return result


def handle_solve(args):
    """Обрабатывает команду solve."""
    if args.a is None and args.b is None and args.c is None:
        try:
            a = int(input('Введите A: '))
            b = int(input('Введите B: '))
            c = int(input('Введите C: '))
        except ValueError:
            raise ValueError(
                'ОШИБКА: коэффициент не является целым числом'
            )

    elif args.a is not None and args.b is not None and args.c is not None:
        a, b, c = args.a, args.b, args.c

    else:
        raise ValueError('ОШИБКА: введен неверный набор параметров')

    kind, d, roots = equation.solve(a, b, c)

    if kind == 'квадратное':
        print('Уравнение квадратное')
        print(f'D = {d}')

        if len(roots) == 2:
            print(f'x1 = {roots[0]:.3f}, x2 = {roots[1]:.3f}')
        elif len(roots) == 1:
            print(f'x = {roots[0]:.3f}')
        else:
            print('Действительных корней нет')
    else:
        print('Уравнение линейное')
        print(f'x = {roots[0]:.3f}')

    return 0


def handle_stats(args):
    """Обрабатывает команду stats."""
    if args.input is not None:
        with open(args.input, encoding="utf-8-sig") as handle:
            lines = handle.readlines()
    else:
        lines = sys.stdin

    values = []

    for line in lines:
        for word in line.split():
            try:
                value = float(word)
            except ValueError:
                raise ValueError(f"ОШИБКА: {word} не является числом")

            values.append(value)

    if not values:
        raise ValueError("ОШИБКА: список чисел пуст")

    if len(values) > 20:
        raise ValueError("ОШИБКА: чисел больше 20")

    for value in values:
        if not math.isfinite(value):
            raise ValueError("ОШИБКА: число должно быть конечным")

        if abs(value) > 10_000:
            raise ValueError("ОШИБКА: число вне допустимого диапазона")

    report = [
        ("Количество", len, "d"),
        ("Сумма", stats.sum_values, ".3f"),
        ("Ср. арифм.", stats.mean, ".3f"),
        ("Сумма кв.", stats.sum_squares, ".3f"),
        ("Ср. кв.", stats.root_mean_square, ".3f"),
        ("Дисперсия", stats.variance, ".3f"),
        ("СКО", stats.standard_deviation_population, ".3f"),
        ("Станд. откл.", stats.standard_deviation, ".3f"),
        ("Наименьшее", stats.minimum, ".3f"),
        ("Наибольшее", stats.maximum, ".3f"),
        ("Положительных", stats.count_positive, "d"),
        ("Отрицательных", stats.count_negative, "d"),
    ]

    for label, function, form in report:
        value = function(values)

        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")

    return 0


def handle_series(args):
    """Обрабатывает команду series."""
    if args.terms is not None:
        series.check_terms(args.terms)
    else:
        series.check_eps(args.eps)

    term, formula = series.FORMULAS[args.func]
    print(formula)

    if args.terms is not None:
        result = series.sum_by_terms(term, args.terms)
        count = args.terms
    else:
        result, count = series.sum_by_eps(term, args.eps)

    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {result:.{series.DIGITS}f}")

    return 0


def handle_integrate(args):
    """Обрабатывает команду integrate."""
    function_data = integration.FORMULAS[args.func]

    integration.check_steps(args.steps)
    integration.check_limits(function_data, args.start, args.end)

    function, formula, _, _, _ = function_data
    print(formula)

    result = integration.integrate(
        function,
        args.start,
        args.end,
        args.steps,
    )

    print(f"Значение интеграла: {result:.4f}")

    return 0


def handle_fill(args):
    """Обрабатывает команду fill."""
    if not 1 <= args.count <= MAX_COUNT:
        raise ValueError(
            f"ОШИБКА: количество элементов вне диапазона 1..{MAX_COUNT}"
        )

    if not MIN_VALUE <= args.min <= MAX_VALUE:
        raise ValueError(
            f"ОШИБКА: минимальное значение должно быть "
            f"в диапазоне {MIN_VALUE}..{MAX_VALUE}"
        )

    if not MIN_VALUE <= args.max <= MAX_VALUE:
        raise ValueError(
            f"ОШИБКА: максимальное значение должно быть "
            f"в диапазоне {MIN_VALUE}..{MAX_VALUE}"
        )

    if args.min > args.max:
        raise ValueError(
            "ОШИБКА: минимальное значение больше максимального"
        )

    values = measure_time(
        "fill",
        generate_array,
        (args.count, args.min, args.max, args.seed),
    )

    if args.output is None:
        print(" ".join(str(value) for value in values))
    else:
        write_array(args.output, values)
        print(
            f"Записано элементов: {len(values)} в файл {args.output}"
        )

    return 0


def handle_sort(args):
    """Обрабатывает команду sort."""
    values = read_array(args.input)
    method = sorting.METHODS[args.method]
    descending = args.order == "desc"

    measure_time(
        f"sort ({args.method})",
        method,
        (values, descending),
    )

    if args.output is None:
        print(" ".join(str(value) for value in values))
    else:
        write_array(args.output, values)
        print(
            f"Записано элементов: {len(values)} в файл {args.output}"
        )

    print("Массив отсортирован.")

    return 0


def handle_search(args):
    """Обрабатывает команду search."""
    if abs(args.value) > MAX_SEARCH:
        raise ValueError(
            f"ОШИБКА: модуль искомого значения не должен превышать "
            f"{MAX_SEARCH}"
        )

    values = read_array(args.input)

    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            raise ValueError(
                "ОШИБКА: массив не упорядочен по возрастанию"
            )

    index = measure_time(
        "search",
        binary_search,
        (values, args.value),
    )

    if index is None:
        print(f"Значение {args.value} не найдено.")
        return 1

    print(
        f"Значение {args.value} имеет элемент с индексом {index + 1}."
    )

    return 0


def main(args=None):
    """Запускает приложение и обрабатывает команду пользователя."""
    parser = build_parser()
    args = parser.parse_args(args)

    if args.command is None:
        parser.print_help()
        return 0

    handlers = {
        'solve': handle_solve,
        'stats': handle_stats,
        'series': handle_series,
        'integrate': handle_integrate,
        'fill': handle_fill,
        'sort': handle_sort,
        'search': handle_search,
    }

    try:
        return handlers[args.command](args)
    except (ValueError, OSError) as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
