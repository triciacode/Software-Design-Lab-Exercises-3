class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class ReverseList:
    # Represent the head and tail of the doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None

        # addNode() will add a node to the list

    def addNode(self, data):
        # Create a new node
        newNode = Node(data)

        # If list is empty
        if self.head == None:
            # Both head and tail will point to newNode
            self.head = self.tail = newNode
            # head's previous will point to None
            self.head.previous = None
            # tail's next will point to None, as it is the last node of the list
            self.tail.next = None
        else:
            # newNode will be added after tail such that tail's next will point to newNode
            self.tail.next = newNode
            # newNode's previous will point to tail
            newNode.previous = self.tail
            # newNode will become new tail
            self.tail = newNode
            # As it is last node, tail's next will point to None
            self.tail.next = None

            # reverse() will reverse the doubly linked list

    def reverse(self):
        # Node current will point to head
        current = self.head

        # Swap the previous and next pointers of each node to reverse the direction of the list
        while (current != None):
            temp = current.next
            current.next = current.previous
            current.previous = temp
            current = current.previous
            # Swap the head and tail pointers.
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # display() will print out the elements of the list

    def display(self):
        # Node current will point to head
        current = self.head
        if (self.head == None):
            print("List is empty")
            return

        while (current != None):
            # Prints each node by incrementing pointer.
            print(current.data),
            current = current.next


dList = ReverseList()
# Add nodes to the list
dList.addNode(1)
dList.addNode(2)
dList.addNode(3)
dList.addNode(4)
dList.addNode(5)

print("Original List: ")
dList.display()
# Reverse the given list
dList.reverse()

# Displays the reversed list
print("\nReversed List: ")
dList.display()
