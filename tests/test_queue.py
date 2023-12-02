"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        """Несколько элементов в очереди"""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(str(queue), "1\n2\n3")

    def test_enqueue_single_element(self):
        """Первый в очереди"""
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(str(queue), "1")

    def test_enqueue_empty_queue(self):
        """Пустая очередь"""
        queue = Queue()
        self.assertEqual(str(queue), "")

    def test_init(self):
        """Тест инициализации"""
        queue = Queue()
        self.assertEqual(queue.tail, None)
        self.assertEqual(queue.head, None)

    def test_str(self):
        """Тест магии str"""
        queue = Queue()
        self.assertEqual(queue.__str__(), "")


if __name__ == '__main__':
    unittest.main()
