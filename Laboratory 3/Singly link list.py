#Creation of Singly Link List

#Node Class
class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singly_linked_list:
    def __init__(self):
        # Create an empty list
        self.tail = None
        self.head = None


    def append_item(self, data):
        # Append items on the list
        node = Node(data)
        if(self.head == None):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    def display(self):
        current = self.head

        if (self.head == None):
            print("List is empty")
            return
        print("Nodes of singly linked list: ")
        while (current != None):
            # Prints each node by incrementing pointer
            print(current.data),
            current = current.next

sL = singly_linked_list()

    # Append nodes to the list
sL.append_item('Takoyaki')
sL.append_item('Siomai')
sL.append_item('Samgyupsal')
sL.append_item('Sushi')

    # Displays the nodes present in the list
sL.display()

