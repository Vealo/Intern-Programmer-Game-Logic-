# Вопрос №2

# На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.
# Оценивается:
# 1.	Полнота и качество реализации
# 2.	Оформление кода
# 3.	Наличие сравнения и пояснения по быстродействию

class Queue(list):
    def __init__(self):
        self.first = None
        self.last = None

    def put(self, item):
        if self.empty():
            self.first = item
        self.last = item     
        self.append(item)

    def get(self):
        if self.full():
            temp = self.pop(0)
            self.first = self[0] 
            return temp
        self.first = None
        self.last = None
        return None
    
    def full(self):
        return self.__len__() > 0
    
    def empty(self):
        return self.__len__() == 0
    
    def __str__(self):
        return f"[{", ".join(str(item) for item in self)}]"
    
    def __repr__(self):
        return f"{__class__.__name__}"

    def clear(self):
        super().clear()
        self.first = None
        self.last = None

    def join(self, other):
        if isinstance(other, self.__class__):
            self.extend(other)
            return None
        return NotImplemented    

queue = Queue() 
addQueue = Queue()

for item in range(21, 31):
    addQueue.put(item)


print(f"Emty: {queue.empty()}, Full: {queue.full()}, First: {queue.first}, Last: {queue.last}")

for item in range(1, 21):
    queue.put(item)

print(f"Сгенерированная очередь: {queue}")
print(f"Emty: {queue.empty()}, Full: {queue.full()}, First: {queue.first}, Last: {queue.last}")
print(f"Продвигаем очередь на 1 элемент: {queue.get()}")
print(f"Получаем первый элемент очереди не изменяя очереди: {queue.first}")
print(f"Добавим к первой очереди вторую: {addQueue}")
queue.join(addQueue)
print(f"Итоговая очередь: {queue}")
print(f"Очистим очередь")
queue.clear()
print(f"Очередь: {queue}, Первый элемент: {queue.first}, Последний Элемент: {queue.last}")

# Очередь создана на базе встроего класса list. Сотвествено имеет все скоростные параметры данного класса. 
# По отношению к специализированным решениям реализованным на C++ как библиотеки python будет работать медленее на дополнительных функциях. 
