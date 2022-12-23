# eg: 10-->5-->16

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value, prev=self.tail)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value, next=self.head)
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)

        lead_node = self.traverse2index(index - 1)
        next_node = lead_node.next
        new_node = Node(value, next=next_node, prev=lead_node)
        lead_node.next = new_node
        next_node.prev = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise Exception()
        if index == 0:
            node_remove = self.head
            self.head = self.head.next
            self.head.prev = None
            del node_remove
            self.length -= 1
            return
        node_remove = self.traverse2index(index)
        lead_node = node_remove.prev
        next_node = node_remove.next
        lead_node.next = next_node
        next_node.prev = lead_node

        del node_remove
        self.length -= 1

    def traverse2index(self, index):
        if index >= self.length:
            raise Exception()

        current_node = self.head
        i = 0
        while i < index:
            current_node = current_node.next
            i += 1
        return current_node

    def print_list(self):
        array = []
        current_node = self.head
        array.append(current_node.value)
        while current_node.next is not None:
            current_node = current_node.next
            array.append(current_node.value)
        return array


ll = DoublyLinkedList(10)
print(ll.print_list())
ll.append(5)
print(ll.print_list())
ll.append(16)
print(ll.print_list())
ll.prepend(1)
print(ll.print_list())
ll.insert(2, 99)
print(ll.print_list())
ll.remove(2)
print(ll.print_list())
