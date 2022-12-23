

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.first = node
        else:
            self.last.next = node
        self.last = node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return None
        temp_node = self.first
        if self.first == self.last:
            self.last = None
        self.first = temp_node.next
        self.length -= 1
        return temp_node

    def is_empty(self):
        return self.length == 0


my_queue = MyQueue()
my_queue.enqueue('Joy')
my_queue.enqueue('Matt')
my_queue.enqueue('Pavel')
my_queue.enqueue('Samir')

print(my_queue.peek().value)
print(my_queue.dequeue().value)
print(my_queue.dequeue().value)
print(my_queue.dequeue().value)
print(my_queue.dequeue().value)
print(my_queue.dequeue())
