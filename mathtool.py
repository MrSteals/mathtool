import sys
from calc import equation
from cli import build_parser

# Разбор аргументов командной строки
parser = build_parser()
args = parser.parse_args(sys.argv[1:])

# Если команда не указана — вывод справки
if args.command is None:
    parser.print_help()
    sys.exit(0)

# Команда solve
if args.command != 'solve':
    print('заглушка')
    sys.exit(0)

# Проверка коэффициентов
if args.a is None and args.b is None and args.c is None:
    # Ввод коэффициентов с клавиатуры
    try:
        a = int(input('Введите A: '))
        b = int(input('Введите B: '))
        c = int(input('Введите C: '))
    except ValueError:
        print('ОШИБКА: коэффициент не является целым числом', file=sys.stderr)
        sys.exit(1)

elif args.a is not None and args.b is not None and args.c is not None:
    # Коэффициенты заданы в командной строке
    a = args.a
    b = args.b
    c = args.c

else:
    print('ОШИБКА: введен неверный набор параметров', file=sys.stderr)
    sys.exit(1)

# Решение уравнения с помощью модуля equation
try:
    kind, d, roots = equation.solve(a, b, c)

except ValueError as error:
    print(error, file=sys.stderr)
    sys.exit(1)

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
