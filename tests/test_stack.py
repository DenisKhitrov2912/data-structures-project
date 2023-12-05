"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


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


    def test_node_creation(self):
        """Тестирование создания экземпляров"""
        node = Node(5, Node(6, None))

        self.assertEqual(node.data, 5)
        self.assertEqual(node.next_node.data, 6)
        self.assertEqual(node.next_node.next_node, None)


if __name__ == '__main__':
    unittest.main()
