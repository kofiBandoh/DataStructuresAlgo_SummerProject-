from binaryTree import BinaryTree


# Hashtable Class
# Handles collision with tree organised overflows
class tree_overflow:

    # Constructor for Hashtable
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Hashing function - Mid-Square Technique
    def hashing(self, key):
        key = key * key

        key = str(key)
        x = len(key)
        mid = x // 2
        key = key[mid-1:mid+1]

        return int(key)
    
    # Insert element into hashtable
    def insert(self, element):
        position = self.hashing(element) # Generate index for insertion
        
        # If there is a binary tree in that position
        # Add element to the binary tree
        # Else create a new binary tree at the position and add the element
        if self.table[position]:
            self.table[position].insert(element)
        else:
            self.table[position] = BinaryTree()
            self.table[position].insert(element)
            
    def printTree(self):
        for i in range(self.size):
            if self.table[i]:
                self.table[i].printTree()
                print(i, "->" ,self.table[i].get_pList())
                