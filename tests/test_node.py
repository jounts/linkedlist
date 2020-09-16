import unittest

from linked_list import Node


class TestNode(unittest.TestCase):
    def setUp(self) -> None:
        self.node = Node(1)

    def test_init(self):
        node = Node(1)
        self.assertEqual(node.value, 1)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)

    def test_property_next(self):
        next_node = Node(2)
        node = Node(1, next_node)
        self.assertEqual(id(node.next), id(next_node))

    def test_property_setter_next(self):
        next_node = Node(2)
        node = Node(1)
        node.next = next_node
        self.assertEqual(id(node.next), id(next_node))
        with self.assertRaises(TypeError):
            node.next = 1

    def test_repr(self):
        node = Node(1, Node(2), Node(3))
        self.assertEqual(repr(node), 'Node(1, 2, 3)')


if __name__ == '__main__':
    unittest.main()
