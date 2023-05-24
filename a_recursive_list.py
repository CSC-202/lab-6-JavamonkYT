class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
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


def initialize() -> List:
    return List()


def isEmpty(data: List) -> bool:
    if data.first is None:
        return True
    return False


def addAtIndex(data: List, index: int, value: int) -> List:
    if index == 0:
        newNode = Node(value, data.first)
        data.first = newNode #Update the first of this list
        return data
    else:
        tail = List() #Grab the tail
        tail.first = data.first.next
        newTail = addAtIndex(tail, index-1, value) #Change the tail without changing the original list
        data.first.next = newTail.first #Update the original list
        return data


def removeAtIndex(data: List, index: int) -> tuple[Node, List]:
    if index == 0:
        removedNode = Node(data.first.value, None)
        data.first = data.first.next #Update the first of this list to kill off that element
        return removedNode, data
    else:
        tail = List() #Grab the tail
        tail.first = data.first.next
        removedNode, newTail = removeAtIndex(tail, index-1) #Change the tail without changing the original list
        data.first.next = newTail.first #Update the original list
        return removedNode, data


def addToFront(data: List, value: int) -> List:
    newNode = Node(value, data.first)
    if isEmpty(data):
        data.last = newNode
    data.first = newNode
    return data


def addToBack(data: List, value: int) -> List:
    newNode = Node(value, None)
    if isEmpty(data):
        data.first = newNode
        data.last = newNode
    else:
        data.last.next = newNode
        data.last = data.last.next
    return data


def getElementAtIndex(data: List, index: int) -> Node:
    if index == 0:
        foundNode = Node(data.first.value, None)
        return foundNode
    else:
        tail = List() #Grab the tail
        tail.first = data.first.next
        if not isEmpty(tail):
            return getElementAtIndex(tail, index-1) #Dig deeper without changing the original list
        else:
            return Node(None, None)


def clear(data: List) -> List:
    return initialize()
