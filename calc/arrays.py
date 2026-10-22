
"""Чтение, запись и генерация числовых массивов."""

import random
import sys

MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1_000_000
MAX_SEARCH = 1000


def read_array(path=None):
    """Читает и проверяет массив целых чисел из файла или stdin."""
    if path is not None:
        # Читаем файл целиком в кодировке UTF-8.
        with open(path, encoding="utf-8-sig") as file:
            text = file.read()
    else:
        # Читаем строки до пустой строки или конца ввода.
        lines = []
        print("Введите числа:", file=sys.stderr)

        while True:
            try:
                line = input()
            except EOFError:
                break

            if not line.strip():
                break

            lines.append(line)

        text = " ".join(lines)

    # Запятые и пробельные символы служат разделителями.
    text = text.replace(",", " ")
    words = text.split()

    values = []

    for word in words:
        try:
            value = int(word)
        except ValueError:
            raise ValueError(
                f"ОШИБКА: {word!r} не является целым числом"
            )

        values.append(value)

    # Проверяем количество элементов.
    if not values:
        raise ValueError("ОШИБКА: массив пуст")

    if len(values) > MAX_COUNT:
        raise ValueError(
            f"ОШИБКА: количество элементов превышает {MAX_COUNT}"
        )

    # Проверяем диапазон каждого элемента.
    for value in values:
        if not MIN_VALUE <= value <= MAX_VALUE:
            raise ValueError(
                f"ОШИБКА: число {value} вне диапазона "
                f"от {MIN_VALUE} до {MAX_VALUE}"
            )

    return values


def write_array(path, values):
    """Записывает массив целых чисел в файл одной строкой."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(" ".join(str(x) for x in values) + "\n")


def generate_array(count, low=MIN_VALUE, high=MAX_VALUE, seed=None):
    """Генерирует список случайных целых чисел."""
    random.seed(seed)

    values = []

    for _ in range(count):
        values.append(random.randint(low, high))

    return values
