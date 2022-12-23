#!python3

import json


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        else:
            cur_node = self.root
            while True:
                if value < cur_node.value:  # left
                    if cur_node.left is None:
                        cur_node.left = new_node
                        return
                    else:
                        cur_node = cur_node.left
                else:  # right
                    if cur_node.right is None:
                        cur_node.right = new_node
                        return
                    else:
                        cur_node = cur_node.right

    def lookup(self, value):
        if self.root is None:
            return None
        cur_node = self.root
        while cur_node:
            if value == cur_node.value:
                return cur_node
            if value < cur_node.value:  # left
                cur_node = cur_node.left
            elif value > cur_node.value:  # right
                cur_node = cur_node.right
            elif value == cur_node.value:
                return cur_node
        return None

    def remove(self, value):
        if self.root is None:
            return False
        current_node = self.root
        parent_node = None
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif current_node.value == value:
                # We have a match, get to work!

                # Option 1: No right child:
                if current_node.right is None:
                    if parent_node is None:
                        self.root = current_node.left
                    else:
                        # if parent > current value, make current left child a child of parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left

                        # if parent < current value, make left child a right child of parent
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.left

                # Option 2: Right child which doesn't have a left child
                elif current_node.right.left is None:
                    current_node.right.left = current_node.left
                    if parent_node is None:
                        self.root = current_node.right
                    else:
                        # if parent > current, make right child of the left the parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right

                        # if parent < current, make right child a right child of the parent
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right

                # Option 3: Right child that has a left child
                else:
                    # find the Right child's left most child
                    leftmost = current_node.right.left
                    leftmost_parent = current_node.right
                    while leftmost.left is not None:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left

                    # Parent's left subtree is now leftmost's right subtree
                    leftmost_parent.left = leftmost.right
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right

                    if parent_node is None:
                        self.root = leftmost
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = leftmost
                        elif current_node.value > parent_node.value:
                            parent_node.right = leftmost
                return True
        return False

    def breadth_first_search(self):
        current_node = self.root
        li = []
        queue = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.value)
            li.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return li

    def breadth_first_search_recursive(self, queue, li):
        if len(queue) == 0:
            return li
        current_node = queue.pop(0)
        print(current_node.value)
        li.append(current_node)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        return self.breadth_first_search_recursive(queue, li)

    def traverse_inorder(self, node, li):
        if node.left:
            self.traverse_inorder(node.left, li)
        li.append(node.value)
        if node.right:
            self.traverse_inorder(node.right, li)
        return li

    def traverse_preorder(self, node, li):
        li.append(node.value)
        if node.left:
            self.traverse_preorder(node.left, li)
        if node.right:
            self.traverse_preorder(node.right, li)
        return li

    def traverse_postorder(self, node, li):
        if node.left:
            self.traverse_postorder(node.left, li)
        if node.right:
            self.traverse_postorder(node.right, li)
        li.append(node.value)
        return li

    def dfs_inorder(self):
        return self.traverse_inorder(self.root, [])

    def dfs_postorder(self):
        return self.traverse_postorder(self.root, [])

    def dfs_preorder(self):
        return self.traverse_preorder(self.root, [])


def traverse(node):
    if node is None:
        return None
    tree = Node(node.value)

    if node.left is not None:
        tree.left = None if node.left is None else traverse(node.left)
    if node.right is not None:
        tree.right = None if node.right is None else traverse(node.right)
    return tree


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.__dict__
#tree.breadth_first_search()
#tree.breadth_first_search_recursive([tree.root], [])
print(tree.dfs_inorder())
print(tree.dfs_preorder())
print(tree.dfs_postorder())

traverse(tree.root)

node1 = tree.lookup(9)
node2 = tree.lookup(170)
node3 = tree.lookup(6)
node4 = tree.lookup(0)

print(tree.remove(0))
print(tree.remove(9))
print(tree.remove(20))

# JSON.stringify(traverse(tree.root))

#     9
#  4     20
# 1  6  15  170
