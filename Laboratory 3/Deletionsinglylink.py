
#Deletion of Singly Linked list
# Node class
class Node:


    def __init__(self, data):
        self.data = data
        self.next = None


class singly_LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    # delete the first occurrence of key in linked list
    def deleteNode(self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return


        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if (temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.nexta

        temp = None

    # print list
    def displayList(self):
        temp = self.head
        while (temp):
            print(" %d" % (temp.data)),
            temp = temp.next


# Driver program
slist =singly_LinkedList()
slist.push(24)
slist.push(9)
slist.push(16)
slist.push(8)

print(" Singly Linked List: ")
slist.displayList()
slist.deleteNode(9)
print("\n Singly Linked List after Deletion of 9:")
slist.displayList()