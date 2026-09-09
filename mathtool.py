import sys
import math

MAX_VALUE = 10_000
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
        A = int(input('Введите A: '))
        B = int(input('Введите B: '))
        C = int(input('Введите C: '))
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
            A = int(sys.argv[3])
            B = int(sys.argv[5])
            C = int(sys.argv[7])
        except ValueError:
            print('ОШИБКА: коэффициент не является целым числом', file=sys.stderr)
            sys.exit(1)

else:
    print('ОШИБКА: введен неверный набор параметров', file=sys.stderr)
    sys.exit(1)

# Проверка допустимого диапазона коэффициентов
if (abs(A) > MAX_VALUE) or (abs(B) > MAX_VALUE) or (abs(C) > MAX_VALUE):
    print('ОШИБКА: значение вне допустимого диапазона', file=sys.stderr)
    sys.exit(1)

# Решение уравнения
if A != 0:  # квадратное уравнение
    print('Уравнение квадратное')
    D = B * B - 4 * A * C
    print(f'D = {D}')

    if D > 0:
        x1 = (-B + math.sqrt(D)) / (2 * A)
        x2 = (-B - math.sqrt(D)) / (2 * A)
        print(f'x1 = {x1:.3f}, x2 = {x2:.3f}')
    elif D == 0:
        x = -B / (2 * A)
        print(f'x = {x:.3f}')
    else:
        print('Действительных корней нет')

elif B != 0:  # линейное уравнение
    print('Уравнение линейное')
    x = -C / B
    print(f'x = {x:.3f}')
else:
    print('ОШИБКА: это не уравнение, неизвестное отсутствует', file=sys.stderr)
    sys.exit(1)
