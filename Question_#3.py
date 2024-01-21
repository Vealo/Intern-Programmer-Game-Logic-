# Вопрос №3

# На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. 
# Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). 
# Объяснить, почему вы считаете, что функция соответствует заданным критериям.

# Входные данные
from random import randint
data = [randint(0, 100) for _ in range(1, 10000)]

def swapSort(data): 
    target = len(data) - 1
    while target > 1:
        for i in range(target):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        target -= 1
    return data

def quickSort(data):

    if len(data) < 1:
        return data
    
    pivot = data[0]
    more = []
    target = []
    less = []
    
    for item in data:
        if item == pivot:
            target.append(item)
        elif pivot < item:
            more.append(item)
        else:
            less.append(item)

    return quickSort(less) + target + quickSort(more)

def dualSort(data):
    lenTarget = len(data) - 1

    if lenTarget < 1000:
        check = True
        for i in range(lenTarget):
            if data[i] > data[i + 1]:
                check = False
                break
        if check:
            return data
        return swapSort(data)
    
    return quickSort(data)


print(data)
print(dualSort(data))

# Сортировка реализована для сравнимых типов данных.
# Реализованны две вспомогательные функци сортировки "обменом значений" и "быстрая".
# На небольших массивах не имеет значения способ сортировки время их выполнения будет сравнимо мало.
# Для уменьшения затрат по памяти при количестве элементов до 1000 (имперически выбранное значения без доказательств):
#   Проверяем упорядоченость массива и если он упарядочен сразу возращаем.
#   Если не отсортирован запускаем сортировку обменом.
# При количестве элементов свыше 1000 происходит быстрая сортировка. 
# Как итог мы имеем три скорости:
#   на отсортированных массивах до 1000 - O(n)
#   на не отсортированных массивах до 1000 - O(n**2)
#   на массивах свыше 1000 - O(nlog(n))


