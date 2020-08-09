# Class for node for binary tree
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Class for Binary Tree
class BinaryTree:

    def __init__(self):
        self.root = None
        self.pList = []

    # Insert data into binary tree
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    # Recursive helper function
    # To insert data into binary tree
    def _insert(self, node, data):

        if data < node.data:
            if node.left is not None:
                self._insert(node.left, data)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._insert(node.right, data)
            else:
                node.right = Node(data)

    # Print data from binary tree
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    # Recursive helper function to print data from binary tree
    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            self.pList.append(node.data)
            self._printTree(node.right)
    
    def get_pList(self):
        return self.pList

