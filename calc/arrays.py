import random
import sys

MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1_000_000
MAX_SEARCH = 1000


def read_array(path=None):
    """Читает массив целых чисел из файла или стандартного ввода."""
    if path is not None:
        with open(path, encoding="utf-8-sig") as file:
            text = file.read()
    else:
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

    if not values:
        raise ValueError("ОШИБКА: массив пуст")

    if len(values) > MAX_COUNT:
        raise ValueError(
            f"ОШИБКА: количество элементов превышает {MAX_COUNT}"
        )

    for value in values:
        if not MIN_VALUE <= value <= MAX_VALUE:
            raise ValueError(
                f"ОШИБКА: число {value} вне диапазона "
                f"от {MIN_VALUE} до {MAX_VALUE}"
            )

    return values


def write_array(path, values):
    """Записывает массив целых чисел в файл."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(" ".join(str(x) for x in values) + "\n")


def generate_array(count, low=MIN_VALUE, high=MAX_VALUE, seed=None):
    """Генерирует массив случайных целых чисел."""
    random.seed(seed)

    values = []

    for _ in range(count):
        values.append(random.randint(low, high))

    return values
