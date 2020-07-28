# Sources:
# https://realpython.com/linked-lists-python/
# https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
# https://stackoverflow.com/questions/6256983/how-are-deques-in-python-implemented-and-when-are-they-worse-than-lists

# This is an overview on what linked lists are and how to implement them on Python
# Basics:
# Each element of a linked list consists of "two blocks" called a node.
# One block in the node has the data; it contains the value that was stored in it
# The other block contains a reference to the next node that should be followed
# In Python, lists are dynamic arrays so the memory usage of linked lists and lists is similary.

# Use .insert() and .remove() to target specific elements in a list
# Use .append() and .pop() to insert/remove elements at the end of the list

# Linked lists have a time complexity of O(1) in queues (FIFO), which is faster than normal lists, but they perform similarly when implementing a stack (LIFO)
# In element lookups, lists are faster when you know which element you want to access (they are O(1)), but linked lists take O(n) because they have to traverse the whole list
# When searching for specific elements they perform the same, O(n) because they need to traverse every element one by one to find what they want

# In Python we can use collections.deque which stands for double-ended queue. It uses an implementation of a linked list that you can access, insert, or remove elements from the beginning or the end of the list with O(1) performance.
# deques are useful for append and pop things at the end/front but lists are better for random-access (O(1) speed) and fixed-length operations including slicing

# Linked lists can be used for queues, stacks, and graphs.
# For queues use FIFO (First In, First Out); That means that the first element inserted in the list is the first one to be retrieved

# For stacks use LIFO (Last In, First Out); that means that the last element that was inserted is the first one you would get

# For graphs you could use an adjacency list; each vertex of the graph is stored alongside a collection of connected vertices
graph = {
    1: [2, 3, None],
    2: [4, None],
    3: [None],
    4: [5, 6, None],
    5: [6, None],
    6: [None]
}

# To create a linked list using deque write the below. It will create an empty list. You may also populate it at creation (refer to source)
from collections import deque 
deque()

# Now we can manipulate the deque object by adding or removing elements
llist = deque("abcde")
print (llist)

llist.append("hola") # notice how since it's an append, it will be last in the list
print (llist)

llist.pop() # notice how you don't need to specify anything in pop because it automatically pops out hte last element in the list
print (llist)

llist.appendleft("adios") # use appendleft to specify you want it on the left side
print (llist)

llist.popleft() # use popleft to specify you want the leftmost element to be popped out
print (llist)