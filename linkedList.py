# Class for node for linked list
class Node:

    # Constructor for Node class
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    # Constructor for Linked List Class
    def __init__(self):
        self.head = None

    # Insert data into linked list
    def insert(self, data):
        node = Node(data)

        # Check if the head of linked list has data
        if self.head:
            current = self.head # Set current to head of Linked List
            while current.next: # While current has a next set it to its next
                current = current.next
            current.next = node # Set last node's next to new node
        else:
            self.head = node

    def printList(self):
        pList = [] # Array to hold data from linked list
        current = self.head # Set current to head of Linked ist
        
        # While current is not null 
        # add its data to the array
        # and set current to its next
        while current: 
            pList.append(current.data)
            current = current.next

        return pList

        
    
