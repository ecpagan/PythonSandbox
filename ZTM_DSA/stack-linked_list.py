#! python3

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        s = 'value:"{}", next:"{}"'.format(self.value, self.next)
        return s


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        node = Node(value)
        if self.is_empty():
            self.bottom = node
        else:
            node.next = self.top
        self.top = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return None
        if self.top == self.bottom:
            self.bottom = None
        node = self.top
        self.top = node.next
        self.length -= 1
        return node

    def is_empty(self):
        return self.length == 0


my_stack = Stack()
my_stack.push('Discord')
my_stack.push('Udemy')
my_stack.push('google')
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
