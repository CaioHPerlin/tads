from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._recursive_insert(self.root, new_node)

    def print_in_order(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            self.print_in_order(node.left)
        print(node.value, end=" ")
        if node.right:
            self.print_in_order(node.right)

    def print_pre_order(self, node = None):
        if node is None:
            node = self.root
        print(node.value, end=" ")
        if node.left:
            self.print_pre_order(node.left)
        if node.right:
            self.print_pre_order(node.right)

    def print_post_order(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            self.print_post_order(node.left)
        if node.right:
            self.print_post_order(node.right)
        print(node.value, end=" ")
    
    def remove(self, value):
        self.root = self._recursive_remove(self.root, value)

    def _recursive_insert(self, curr_node, new_node):
        if new_node.value < curr_node.value:
            if curr_node.left is None:
                curr_node.left = new_node
            else:
                self._recursive_insert(curr_node.left, new_node)
        
        else: 
            if curr_node.right is None:
                curr_node.right = new_node
            else:
                self._recursive_insert(curr_node.right, new_node)

    def _recursive_remove(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._recursive_remove(node.left, value)
        elif value > node.value:
            node.right = self._recursive_remove(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            heir = self._find_min(node.right)
            node.value = heir.value
            node.right = self._recursive_remove(node.right, heir.value)
        return node
    
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


bt = BinaryTree()

bt.insert(50)
bt.insert(27)
bt.insert(22)
bt.insert(10)
bt.insert(42)
bt.insert(31)
bt.insert(63)
bt.insert(70)
bt.insert(52)
bt.insert(54)
bt.insert(55)


print("In Order:")
bt.print_in_order()

print("\nPre Order:")
bt.print_pre_order()

print("\nPost Order:")
bt.print_post_order()

print()
