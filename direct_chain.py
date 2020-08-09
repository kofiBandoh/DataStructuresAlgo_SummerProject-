from linkedList import LinkedList


# Hashtable Class
# Handles collision with simple direct chain
class direct_chain:
    
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
        
        # If there is a linked list in that position
        # Add element to the linked list
        # Else create a new linked list at the position and add the element
        if self.table[position]:
            self.table[position].insert(element)
        else:
            self.table[position] = LinkedList()
            self.table[position].insert(element)

    def printTable(self):
        for i in range(self.size):
            if self.table[i]:
                print(i, "->" , self.table[i].printList())