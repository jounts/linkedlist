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
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def __len__(self):
        return self.__len

    def insert(self, index: int, value: Any):
        if not isinstance(index, int):
            raise TypeError('index must be int')
        if index < 0:
            if self.__len >= abs(index):
                index = self.__len + index + 1
            else:
                index = 0
        insert_node = Node(value)
        if not self.__len:
            self.__head = insert_node
            self.__tail = self.__head
            self.__len += 1
        elif index < self.__len:
            if not index:
                insert_node.next = self.__head
                self.__head.prev = insert_node
                self.__head = insert_node
                self.__len += 1
            elif index > 0:
                current_node = self.__head
                for i in range(index - 1):
                    current_node = current_node.next
                insert_node.prev = current_node
                insert_node.next = current_node.next
                current_node.next.prev = insert_node
                current_node.next = insert_node
                self.__len += 1
        elif index >= self.__len:
            insert_node.prev = self.__tail
            self.__tail.next = insert_node
            self.__tail = insert_node
            self.__len += 1

    def append(self, value: Any):
        append_node = Node(value)
        if self.__head is None:
            self.__head = append_node
            self.__tail = self.__head
        else:
            append_node.prev = self.__tail
            self.__tail.next = append_node
            self.__tail = append_node
        self.__len += 1

    def push(self, value: Any):
        pushed_node = Node(value)
        if self.__head is None:
            self.__head = pushed_node
            self.__tail = self.__head
        else:
            pushed_node.next = self.__head
            self.__head.prev = pushed_node
            self.__head = pushed_node
        self.__len += 1

    def __iter__(self):
        current_node = self.__head
        for _ in range(self.__len):
            yield current_node.value
            current_node = current_node.next

    def find(self, value: Any):
        for index, list_value in enumerate(self):
            if list_value == value:
                return index

    def delete(self, index: int):
        if not isinstance(index, int):
            raise TypeError('index must be int')
        if index < 0:
            if self.__len >= abs(index):
                index = self.__len + index
            else:
                raise IndexError('index out of range')
        current_node = self.__head
        for i in range(self.__len):
            temp_node = current_node.next
            if i == index:
                if current_node.prev is not None and current_node.next is None:
                    current_node.prev.next = None
                    self.__tail = current_node.prev
                    current_node.prev = None
                    del current_node
                    self.__len -= 1
                elif current_node.prev is None and current_node.next is not None:
                    self.__head = current_node.next
                    current_node.next.prev = None
                    current_node.next = None
                    del current_node
                    self.__len -= 1
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    current_node.next = None
                    current_node.prev = None
                    del current_node
                    self.__len -= 1
            current_node = temp_node

    def remove(self, value: Any):
        current_node = self.__head
        for index, list_value in enumerate(self):
            temp_node = current_node.next
            if list_value == value:
                if current_node.next is None and current_node.prev is not None:
                    self.__tail = current_node.prev
                    del current_node
                    self.__len -= 1
                    break
                elif current_node.next is not None and current_node.prev is None:
                    self.__head = current_node.next
                    del current_node
                    self.__len -= 1
                    break
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    r_node = current_node
                    del r_node
                    self.__len -= 1
                    break
            current_node = temp_node

    def clear(self):
        current_node = self.__head
        for _ in range(self.__len):
            temp_node = current_node.next
            if current_node.next is not None:
                current_node.next = None
            elif current_node.prev is not None:
                current_node.prev = None
            del current_node.value
            del current_node
            current_node = temp_node
        self.__head = self.__tail = None
        self.__len = 0

    def __repr__(self):
        ans = []
        for i in self:
            ans.append(i)
        return f'{ans}'


if __name__ == '__main__':
    pass
