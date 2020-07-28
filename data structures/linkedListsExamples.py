# Make the two main elements of every single node, data and next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iteration__(self):
        node = self.head
        #if the below condition is true, it means we are at the end of the linked list
        while node is not None:
            yield node
            node = node.next
            
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)



    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

#Example of creating a linked list and assiging some values to it
llist = LinkedList()
print("1")
print (llist)

first_node = Node("a")
llist.head = first_node
print("2")
print (llist)

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print("3")
print (llist)

#traversing a linked list; traversing just means going through every single node through iteration
llist2 = LinkedList(["a", "b", "c", "d", "e"])
print("4")
print(llist2)
# for node in llist2:
#     print(node)

#Inserting new nodes at the beginning
llist3 = LinkedList()
print("5")
llist3.add_first(Node("a"))
print(llist3)

llist3.add_first(Node("0"))
print (llist3)

# inserting new nodes at the end
llist4 = LinkedList(["a", "b", "c", "d", "e"])
print("6")
print(llist4)
llist4.add_last(Node("f"))
print(llist4)
llist4.add_last(Node("g"))