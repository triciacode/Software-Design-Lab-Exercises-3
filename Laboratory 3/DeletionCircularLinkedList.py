
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class circular_list:
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

            # Deletes node from end of the list

    def deleteEnd(self):
        # Checks whether list is empty
        if (self.head == None):
            return
        else:
            # Checks whether contain only one element
            if (self.head != self.tail):
                current = self.head
                # Loop will iterate till the second last element as current.next is pointing to tail
                while (current.next != self.tail):
                    current = current.next
                    # Second last element will be new tail
                self.tail = current
                # Tail will point to head as it is a circular linked list
                self.tail.next = self.head
                # If the list contains only one element
            # Then it will remove it and both head and tail will point to null
            else:
                self.head = self.tail = None

                # Displays all the nodes in the list

    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        else:
            # Prints each node by incrementing pointer.
            print(current.data),
            while (current.next != self.head):
                current = current.next;
                print(current.data),
            print("\n")

class CircularLinkedList:
    c_list = circular_list()
    # Adds data to the list
    c_list.add(5)
    c_list.add(4)
    c_list.add(3)
    c_list.add(2)

    # Printing original list
    print("Original List:")
    c_list.display();
    while (c_list.head != None):
        c_list.deleteEnd()
        # Printing updated list
        print("Updated List:")
        c_list.display()