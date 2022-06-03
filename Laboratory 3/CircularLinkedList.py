#Node Class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CreateList:
    # Declaring head and tail pointer as null.
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

        # This function will add the new node at the end of the list.

    def add(self, data):
        newNode = Node(data)
        # Checks if the list is empty.
        if self.head.data is None:
            # If list is empty, both head and tail would point to new node.
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            # tail will point to new node.
            self.tail.next = newNode
            # New node will become new tail.
            self.tail = newNode
            # Since, it is circular linked list tail will point to head.
            self.tail.next = self.head

            # Displays all the nodes in the list

    def print(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        else:
            print("The nodes of the circular linked list: ")
            # Prints each node by incrementing pointer.
            print(current.data),
            while (current.next != self.head):
                current = current.next
                print(current.data)


class CircularLinkedList:
    c_l = CreateList()
    # Adds data to the list
    c_l.add("Software Design")
    c_l.add("Engineering economics")
    c_l.add(3)
    c_l.add(4)
    # Displays all the nodes present in the list
    c_l.print()