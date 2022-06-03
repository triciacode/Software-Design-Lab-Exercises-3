# insertion
# node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# class Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Add new element at the start of the list
    def push(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    # display the content of the list
    def PrintList(self):
        temp = self.head
        if temp != None:
            print("The list contains:", end=" ")
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")


# test the code
dl = LinkedList()

# Add three elements at the start of the list.
dl.push(10)
dl.push(20)
dl.push(30)
dl.PrintList()