"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def test_push_pop(self):
        """Тестирование добавления и удаления элементов"""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), None)


    def test_str(self):
        """Тест магии str"""
        stack = Stack()
        self.assertEqual(stack.__str__(), "None")


if __name__ == '__main__':
    unittest.main()
