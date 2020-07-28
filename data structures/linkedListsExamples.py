class LinkedList:
    def __init__(self):
        self.head = None

# Make the two main elements of every single node, data and next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None