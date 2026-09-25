import sys
import math
from cli import build_parser
from calc import equation
from calc import stats
from calc import series
from calc import integration

def handle_solve(args):
    """Обрабатывает команду solve."""
    # Проверка коэффициентов
    if args.a is None and args.b is None and args.c is None:
        # Ввод коэффициентов с клавиатуры
        try:
            a = int(input('Введите A: '))
            b = int(input('Введите B: '))
            c = int(input('Введите C: '))
        except ValueError:
            raise ValueError('ОШИБКА: коэффициент не является целым числом')


    elif args.a is not None and args.b is not None and args.c is not None:
        # Коэффициенты заданы в командной строке
        a = args.a
        b = args.b
        c = args.c

    else:
        raise ValueError('ОШИБКА: введен неверный набор параметров')

    # Решение уравнения с помощью модуля equation
    kind, d, roots = equation.solve(a, b, c)

    # Вывод результата
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


# Получает и проверяет числа для команды stats
def handle_stats(args):
    """Обрабатывает команду stats."""
    # Выбираем источник данных
    if args.input is not None:
        with open(args.input, encoding="utf-8-sig") as handle:
            values = []

            for line in handle:
                for word in line.split():
                    try:
                        value = float(word)
                    except ValueError:
                        raise ValueError(
                            f"ОШИБКА: {word} не является числом"
                        )

                    values.append(value)
    else:
        values = []

        for line in sys.stdin:
            for word in line.split():
                try:
                    value = float(word)
                except ValueError:
                    raise ValueError(
                        f"ОШИБКА: {word} не является числом"
                    )

                values.append(value)

    # Проверяем полученный список
    if len(values) == 0:
        raise ValueError("ОШИБКА: список чисел пуст")

    if len(values) > 20:
        raise ValueError("ОШИБКА: чисел больше 20")

    for value in values:
        if not math.isfinite(value):
            raise ValueError("ОШИБКА: число должно быть конечным")

        if abs(value) > 10_000:
            raise ValueError(
                "ОШИБКА: число вне допустимого диапазона"
            )

    # Таблица статистических показателей
    REPORT = [
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

    # Вывод статистических показателей
    for label, function, form in REPORT:
        value = function(values)

        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")

    return 0

def handle_series(args):
    """Обрабатывает команду series."""
    # Проверяем заданный способ вычисления
    if args.terms is not None:
        series.check_terms(args.terms)
    else:
        series.check_eps(args.eps)

    # Выбираем формулу ряда
    term, formula = series.FORMULAS[args.func]

    print(formula)

    # Вычисляем сумму
    if args.terms is not None:
        result = series.sum_by_terms(term, args.terms)
        count = args.terms
    else:
        result, count = series.sum_by_eps(term, args.eps)

    # Выводим результат
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {result:.{series.DIGITS}f}")

    return 0

def handle_integrate(args):
    """Обрабатывает команду integrate."""
    # Выбираем функцию
    function_data = integration.FORMULAS[args.func]

    # Проверяем параметры
    integration.check_steps(args.steps)
    integration.check_limits(
        function_data,
        args.start,
        args.end
    )

    # Получаем функцию и формулу
    function, formula, _, _, _ = function_data

    print(formula)

    # Вычисляем интеграл
    result = integration.integrate(
        function,
        args.start,
        args.end,
        args.steps
    )

    print(f"Значение интеграла: {result:.4f}")

    return 0



def main(args=None):
    """Запускает приложение и обрабатывает команду пользователя."""
    # Разбор аргументов командной строки
    parser = build_parser()
    args = parser.parse_args(args)

    # Если команда не указана — вывод справки
    if args.command is None:
        parser.print_help()
        return 0

    # Таблица обработчиков команд
    handlers = {
        'solve': handle_solve,
        'stats': handle_stats,
        'series': handle_series,
        'integrate': handle_integrate,
    }

    # Вызов обработчика и обработка ошибок
    try:
        return handlers[args.command](args)

    except (ValueError, OSError) as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
