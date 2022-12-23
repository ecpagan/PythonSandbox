# leetcode.com
# 232. Implement Queue using Stacks, not the same but similar


class CrazyQueue:
    def __init__(self):
        self.first = []
        self.last = []

    def enqueue(self, value) -> None:
        length = len(self.first)
        for i in range(length):
            self.last.append(self.first.pop())
        self.last.append(value)
        return self

    def dequeue(self) -> int:
        length = len(self.last)
        for i in range(length):
            self.first.append(self.last.pop())
        temp = self.first.pop()
        return temp

    def peek(self):
        if self.empty():
            return None
        if len(self.last) > 0:
            return self.last[0]
        return self.first[-1]

    def empty(self) -> bool:
        return len(self.first) == 0 and len(self.last) == 0


queue = CrazyQueue()
print(queue.peek())
print(queue.enqueue('Joy'))
print(queue.enqueue('Matt'))
print(queue.enqueue('Pavel'))
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.peek())
