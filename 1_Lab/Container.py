from typing import List, Optional


class ContainerError(Exception):
    pass


class Container:
    def __init__(self, elements: Optional[List] = None):
        self._elements = elements or []

    @property
    def count(self):
        return len(self._elements)

    @property
    def is_empty(self):
        return len(self._elements) == 0

    def push(self, element):
        self._elements.append(element)

    def pop(self):
        raise NotImplemented('Container is base class')

    def peek(self):
        raise NotImplemented('Container is base class')


class Stack(Container):
    def pop(self):
        try:
            return self._elements.pop()
        except IndexError as e:
            raise ContainerError from e

    def peek(self):
        try:
            return self._elements[-1]
        except IndexError as e:
            raise ContainerError from e


class Queue(Container):
    def pop(self):
        try:
            return self._elements.pop(0)
        except IndexError as e:
            raise ContainerError from e

    def peek(self):
        try:
            return self._elements[0]
        except IndexError as e:
            raise ContainerError from e