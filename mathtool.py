import sys

reference_data = [

]

if (len(sys.argv) == 1) or sys.argv[1] == '--help':
    print(reference_data)
    sys.exit(0)

if (len(sys.argv) == 2) and sys.argv[1] != 'solve':
    print('ОШИБКА: команда не найдена')
    sys.exit(1)

if (len(sys.argv) == 2) and sys.argv[1] == 'solve':
    try:
        A = int(input('Введите A:'))
        B = int(input('Введите B:'))
        C = int(input('Введите C:'))

    except ValueError:
        print('ОШИБКА: коэффициент не является целым числом', file=sys.stderr)
        sys.exit(1)


elif (len(sys.argv) == 8) and sys.argv[1] == 'solve':
    if (sys.argv[2] != '-a') or (sys.argv[4] != '-b') or (sys.argv[6] != '-c'):
        print('ОШИБКА: введен неизвестный параметр')
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
    print('ОШИБКА: введен неверный набор параметров')
    sys.exit(1)

if (abs(A) > 10_000) or (abs(B) > 10_000) or (abs(C) > 10_000):
    print('ОШИБКА: значение вне допустимого диапазона', file=sys.stderr)
    sys.exit(1)

if A != 0: # квадратное уравнение
    print('Заглушка')
elif (A == 0) and (B != 0): # линейное уравнение
    print('Заглушка')
elif (A == 0) and (B == 0):
    print('ОШИБКА: уравнение не является алгебраическим', file=sys.stderr)
    sys.exit(1)
