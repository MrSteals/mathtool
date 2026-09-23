import sys
from calc import equation

REFERENCE_DATA = '''mathtool — решение уравнений вида A*x^2 + B*x + C = 0

Использование:
    python mathtool.py ................................ вывод справки
    python mathtool.py --help ......................... вывод справки
    python mathtool.py solve .......................... ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2 .......... решение с заданными коэффициентами

Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.
'''

# Вывод справки
if (len(sys.argv) == 1) or sys.argv[1] == '--help':
    print(REFERENCE_DATA)
    sys.exit(0)

# Проверка команды
if (len(sys.argv) == 2) and sys.argv[1] != 'solve':
    print('ОШИБКА: команда не найдена', file=sys.stderr)
    sys.exit(1)

# Ввод коэффициентов с клавиатуры
if (len(sys.argv) == 2) and sys.argv[1] == 'solve':
    try:
        a = int(input('Введите A: '))
        b = int(input('Введите B: '))
        c = int(input('Введите C: '))
    except ValueError:
        print('ОШИБКА: коэффициент не является целым числом', file=sys.stderr)
        sys.exit(1)

# Ввод коэффициентов из консоли
elif (len(sys.argv) == 8) and sys.argv[1] == 'solve':
    if (sys.argv[2] != '-a') or (sys.argv[4] != '-b') or (sys.argv[6] != '-c'):
        print('ОШИБКА: введен неизвестный параметр', file=sys.stderr)
        sys.exit(1)
    else:
        try:
            a = int(sys.argv[3])
            b = int(sys.argv[5])
            c = int(sys.argv[7])
        except ValueError:
            print('ОШИБКА: коэффициент не является целым числом', file=sys.stderr)
            sys.exit(1)

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
