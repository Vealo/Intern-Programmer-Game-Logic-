# Вопрос №1

# На языке Python написать алгоритм (функцию) определения четности целого числа, 
# который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. 
# Объяснить плюсы и минусы обеих реализаций. 
# Пример: 
# def isEven(value):
#       return value % 2 == 0
from math import floor
from time import perf_counter
from functools import wraps
from random import randint

#Используя битовое И мы можем выяснить равен ли последний бит (счет слева на право) равен "1" - признак нечотности.
def isEvenBin(value): 
      return value & 1 == 0

#Через округление. При округлении четное число не измениться.
def isEvenFloor(value):
      half = value / 2
      return half == floor(half)

# Пример: 
def isEven(value):
      return value % 2 == 0

#Проверяем массив чисел функций и возращаем результат
def checkAll(func, data):
     return [func(item) for item in data]

def resultTimeUse(func):
    @wraps(func)   
    def wrapper(data, *arg, **kwarg):
        start = perf_counter()
        result = checkAll(func, data)
        stop = perf_counter()
        print("-" * 20)
        print(f"Имя функции: {wrapper.__name__}")
        print(f"Заткраченое время: {stop - start}")
        print("-" * 20, "\n")
    
    return wrapper


data = [randint(0, 100_000_000_000) for _ in range(100_000)]

queue_1 = resultTimeUse(isEven)
queue_2 = resultTimeUse(isEvenBin)
queue_3 = resultTimeUse(isEvenFloor)

queue_1(data)
queue_2(data)
queue_3(data)

# Остаток от деление и битовое "И" дают примерно равные результаты для value < 100_000_000_000.
# Саммый медлиный способ округление (ожидаемо т.к. в нем больше операций).
# Реализация через "%" получает остаток от деления и сравнивает его с 0, должна замедляться с ростом чила.
# Реализация через "&" получает по маск езначение последнего бита и сравнивает с 0 в целом должна довать стабтльное малое время выполения.
# Реализацич через "floor" получает частное от деления и после обработки сравнивает первоначальное и округленое значения, самая емкая по скорости и памяти реализация.
