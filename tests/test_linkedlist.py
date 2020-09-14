import unittest
from random import randint

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.l = LinkedList()

    def test_insert_emty_list(self):
        self.l.insert(0, 5)

        self.assertEqual(len(self.l), 1)
        self.assertEqual(self.l._LinkedList__head.value, 5)
        self.assertEqual(self.l._LinkedList__tail.value, 5)

    def test_insert_to_head(self):
        self.l.insert(10, 45)
        self.l.insert(100, 50)
        self.l.insert(0, 10)

        self.assertEqual(len(self.l), 3)
        self.assertEqual(self.l._LinkedList__head.value, 10)
        self.assertEqual(self.l._LinkedList__tail.value, 50)

    def test_insert_to_middle(self):
        values = [0, 1, 2]
        self.l.insert(0, values[0])
        self.l.insert(2, values[2])
        self.l.insert(1, values[1])
        self.assertEqual(self.l._LinkedList__head.value, 0)
        self.assertEqual(self.l._LinkedList__head.next.value, 1)
        self.assertEqual(self.l._LinkedList__tail.value, 2)
        self.assertEqual(self.l._LinkedList__tail.prev.value, 1)

    def test_iter(self):
        values = [1, 2, 3, 4, 5]
        for val in values:
            self.l.append(val)
        for ind, l_val in enumerate(self.l):
            self.assertEqual(values[ind], l_val)

    def test_append(self):
        values = [i for i in range(10)]
        for value in values:
            self.l.append(value)
        for ind, l_val in enumerate(self.l):
            self.assertEqual(values[ind], l_val)

    def test_push(self):
        values = [i for i in range(10)]
        for value in values:
            self.l.push(value)
        for ind, l_val in enumerate(self.l):
            self.assertEqual(values[len(values) - 1 - ind], l_val)

    def test_find(self):
        values = [i for i in range(15)]
        for value in values:
            self.l.append(value)
        self.l.insert(7, 'testvalue')
        self.assertEqual(self.l.find('testvalue'), 7)
        self.assertEqual(self.l.find(7), 8)

    def test_delete(self):
        values = [i for i in range(5)]
        del_ind = [4, 2, 0]
        for value in values:
            self.l.append(value)
        for ind in del_ind:
            self.l.delete(ind)
        self.assertEqual(self.l.find(1), 0)
        self.assertIsNone(self.l.find(2))

    def test_remove(self):
        values = [i for i in range(5)]
        del_val = [4, 2, 0]
        for value in values:
            self.l.append(value)
        for val in del_val:
            self.l.remove(val)
        self.assertEqual(self.l.find(1), 0)
        self.assertIsNone(self.l.find(2))

    def test_negative_index(self):
        for i in range(3):
            if i = 1:
                continue
            self.l.append(i)
        self.l.insert(-2, 1)
        self.assertEqual(self.l._LinkedList__head.value, 0)
        self.assertEqual(self.l._LinkedList__tail.value, 3)

    def test_clear(self):
        pass  # Узнать как протестировать это


if __name__ == '__main__':
    unittest.main()
