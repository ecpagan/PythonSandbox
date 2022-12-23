# eg: 10-->5-->16

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)

        lead_node = self.traverse2index(index - 1)
        new_node = Node(value, lead_node.next)
        lead_node.next = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise Exception()
        if index == 0:
            node_remove = self.head
            self.head = self.head.next
            del node_remove
            self.length -= 1
            return

        lead_node = self.traverse2index(index - 1)
        node_remove = lead_node.next
        if node_remove == self.tail:
            self.tail = lead_node
            lead_node.next = None
        else:
            lead_node.next = node_remove.next
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

    def reverse(self):
        if self.length < 2:
            return self.head

        first_node = self.head
        self.tail = self.head
        second_node = first_node.next
        while second_node is not None:
            third_node = second_node.next
            second_node.next = first_node
            first_node = second_node
            second_node = third_node
        self.head.next = None
        self.head = first_node
        return self

    def reverse2(self):
        if self.length < 2:
            return self.head

        temp_ll = LinkedList(self.tail.value)
        self.remove(self.length - 1)
        while self.length > 0:
            temp_ll.append(self.tail.value)
            self.remove(self.length - 1)
        return temp_ll

    def print_list(self):
        array = []
        current_node = self.head
        array.append(current_node.value)
        while current_node.next is not None:
            current_node = current_node.next
            array.append(current_node.value)
        return array


ll = LinkedList(10)
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
ll = ll.reverse()
print(ll.print_list())
