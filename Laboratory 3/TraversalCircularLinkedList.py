
class Node:

    #Node Class
    def __init__(self, data):
        self.data = data
        self.next = None

class circular_LinkedList:

    # Create an empty list
    def __init__(self):
        self.head = None

    # Function to insert a node at the beginning of a Clist

    def push(self, data):
        ptr1 = Node(data)
        temp = self.head

        ptr1.next = self.head

        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr1

        else:
            ptr1.next = ptr1 # For the first node

        self.head = ptr1

    # Function to print nodes in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print (temp.data, end=" ")
                temp = temp.next
                if (temp == self.head):
                    break


# Driver program to test above function

# Initialize list as empty
cl_list = circular_LinkedList()

# Created linked list will be 11->2->56->12
cl_list.push(14)
cl_list.push(24)
cl_list.push(4)
cl_list.push(8)

print ("Nodes of circular Linked List")
cl_list.printList()