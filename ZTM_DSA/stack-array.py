#! python3

class Stack:
    def __init__(self):
        self.array = []

    def peek(self):
        if self.is_empty():
            return None
        return self.array[-1]

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if self.is_empty():
            return None
        value = self.array.pop()
        return value

    def is_empty(self):
        return len(self.array) == 0


my_stack = Stack()
my_stack.push('Discord')
my_stack.push('Udemy')
my_stack.push('google')
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
