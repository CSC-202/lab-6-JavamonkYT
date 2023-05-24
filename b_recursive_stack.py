class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result


def initialize() -> Stack:
    return Stack()


def isEmpty(data: Stack) -> bool:
    if data.first is None:
        return True
    return False


def push(data: Stack, value: int) -> Stack:
    newNode = Node(value, data.first)
    if isEmpty(data):
        data.last = newNode
    data.first = newNode
    return data


def pop(data: Stack) -> tuple[Node, Stack]:
    removedNode = Node(data.first.value, None)
    data.first = data.first.next
    return removedNode, data


def peek(data: Stack) -> Node:
    return Node(data.first.value, None)


def clear(data: Stack) -> Stack:
    return initialize()
