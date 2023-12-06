"""Здесь надо написать тесты с использованием
unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


class TestNode(unittest.TestCase):
    def test_init(self):
        """Тест конструктора узла"""
        node = Node()
        self.assertEqual(node.data, None)
        self.assertEqual(node.next_node, None)


class TestLinkedList(unittest.TestCase):
    def test_init(self):
        """Тест конструктора односвязного списка"""
        ll = LinkedList()
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)


    def test_insert_beginning(self):
        """Тест вставки в начало"""
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> None")


    def test_insert_at_end(self):
        """Тест вставки в конец"""
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        self.assertEqual(str(ll), "{'id': 2} -> {'id': 3} -> None")


    def test_str(self):
        """Тест магии str"""
        ll = LinkedList()
        self.assertEqual(str(ll), "None")
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        self.assertEqual(str(ll), "{'id': 1} -> {'id': 2} -> None")


if __name__ == '__main__':
    unittest.main()

