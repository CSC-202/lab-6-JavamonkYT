import a_recursive_list as List
import b_recursive_stack as Stack
import c_recursive_queue as Queue

l = List.initialize()

l = List.addToFront(l, 0)
l = Stack.push(l, 4)
l = List.addAtIndex(l, 1, 1)
l = List.addAtIndex(l, 1, 2)
l = List.addAtIndex(l, 2, 3)
print(l.toPythonList())

v, l = Stack.pop(l)
print(v.value)
print(l.toPythonList())
v, l = Queue.dequeue(l)
print(v.value)
print(l.toPythonList())


l = Queue.enqueue(l, 5)
l = List.addToBack(l, 1)
print(l.toPythonList())

print(List.getElementAtIndex(l, 4).value)