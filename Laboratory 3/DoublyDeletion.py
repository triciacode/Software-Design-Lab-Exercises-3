


#  Define class of linked list Node
class LinkNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #  Insert new node at end position
    def append(self, value):
        #  Create a new node
        node = LinkNode(value)
        if (self.head == None):
            #  Add first node
            self.head = node
            self.tail = node
            return

        #  Add node at last position
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

        #  Delete a linked list by given node value

    def pop(self, value):
        if (self.head == None):
            #  When linked list is empty
            print("Empty linked list")

        if (self.head.data == value):
            #  When remove head
            self.head = self.head.next
            if (self.head != None):
                self.head.prev = None
            else:
                #  When linked list empty after delete
                self.tail = None

        elif (self.tail.data == value):
            #  When remove last node
            self.tail = self.tail.prev
            if (self.tail != None):
                self.tail.next = None
            else:
                #  Remove all nodes
                self.head = None

        else:
            #  When need to find deleted node
            temp = self.head
            #  Get remove node
            while (temp != None and temp.data != value):
                temp = temp.next

            if (temp == None):
                #  Node key not exist
                print("Deleted node are not found")
            else:
                #  Separating deleted node
                #  And combine next and previous node
                temp.prev.next = temp.next
                if (temp.next != None):
                    #  When deleted intermediate nodes
                    temp.next.prev = temp.prev

    #  Display node element of doubly linked list
    def display(self):
        if (self.head == None):
            print("Empty Linked List")
        else:
            print("Linked List Head to Tail ", end=" :")
            #  Get first node of linked list
            temp = self.head
            #  iterate linked list
            while (temp != None):
                #  Display node value
                print("", temp.data, end=" ")
                #  Visit to next node
                temp = temp.next

dll = DoublyLinkedList()
value = 8
    #  Insert following linked list nodes
dll.append(14)
dll.append(24)
dll.append(1)
dll.append(4)
dll.append(8)
dll.append(7)
dll.append(2)
print("Before delete node value ", value)
dll.display()

print("\nAfter delete node value ", value)
dll.pop(value)
    # display all node
dll.display()