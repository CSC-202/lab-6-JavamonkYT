class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
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


def initialize() -> Queue:
    return Queue()


def isEmpty(data: Queue) -> bool:
    if data.first is None:
        return True
    return False


def enqueue(data: Queue, value: int) -> Queue:
    newNode = Node(value, None)
    if isEmpty(data):
        data.first = newNode
        data.last = newNode
    else:
        data.last.next = newNode
        data.last = data.last.next
    return data


def dequeue(data: Queue) -> tuple[Node, Queue]:
    removedNode = Node(data.first.value, None)
    data.first = data.first.next
    return removedNode, data


def peek(data: Queue) -> Node:
    return Node(data.first.value, None)


def clear(data: Queue) -> Queue:
    return initialize()
