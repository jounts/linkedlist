from typing import Any


class Node:
    def __init__(self, value: Any, next_=None, prev=None):
        """
        Create new node for LinkedList
        :param value: Any
        :param next_: node class Node
        :param prev: node class Node
        """
        self._next = next_
        self._prev = prev
        self.value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_):
        if not isinstance(next_, (type(self), type(None))):
            raise TypeError('Need class Node')
        self._next = next_

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_):
        if not isinstance(prev_, (type(self), type(None))):
            raise TypeError('Need class Node')
        self._prev = prev_

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value}, {self.next.value}, {self.prev.value})'


class LinkedList:
    pass


if __name__ == '__main__':
    pass
