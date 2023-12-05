class Node:
    """Класс для узла очереди"""


    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None


class Queue:
    """Класс для очереди"""


    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None


    def __str__(self):
        """Магия str"""
        current = self.head
        queue_str = ""
        while current:
            queue_str += str(current.data) + "\n"
            current = current.next_node
        return queue_str.rstrip("\n")


    def __call__(self):
        """Магия вызова dequeue"""
        return self.dequeue()


    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if not self.head:
            # Если очередь пуста, устанавливаем
            # новый узел как начальный и конечный
            self.head = self.tail = new_node
        else:
            # Иначе добавляем новый узел в конец
            # очереди и обновляем указатель на конец
            self.tail.next_node = new_node
            self.tail = new_node


    def dequeue(self):
        """
        Метод для удаления элемента из очереди.
Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        else:
            removed_data = self.head.data
            self.head = self.head.next_node
            if self.head is None:
                self.tail = None
            return removed_data


