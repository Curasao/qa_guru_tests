import math, random

def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25

    output = f'Привет, {name}! Тебе {age} лет.'

# Проверяем результат

    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."

def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20


    perimeter = 2 * (a + b)

    assert perimeter == 60



    area = a * b


    assert area == 200

def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.

    """
    r = 23
    matdegree = 2

    area = math.pi * pow(r,matdegree)

    assert area == 1661.9025137490005


    length = 2 * math.pi * r

    assert length == 144.51326206513048

def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """


    # Создаем список из 10 случайных чисел от 1 до 100
    l = [random.randint(1, 100) for _ in range(10)]

    # Сортируем список по возрастанию
    l.sort()

    # Проверяем, что длина списка равна 10
    assert len(l) == 10, f"Длина списка не равна 10, а равна {len(l)}"

    # Проверяем, что список отсортирован по возрастанию
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1)), "Список не отсортирован по возрастанию"

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))

def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    l = list(set(l))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_dicts():
    """
    Создайте словарь из двух списков.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    d = dict(zip(first, second))

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second