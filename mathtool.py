import sys
from calc import equation
from cli import build_parser

def handle_solve():
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



def handle_stats(args):
    print('заглушка')
    return 0

def handle_series(args):
    print('заглушка')
    return 0

def handle_integrate(args):
    print('заглушка')
    return 0



def main(args = None):
    # Разбор аргументов командной строки
    parser = build_parser()
    args = parser.parse_args(sys.argv[1:])

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




