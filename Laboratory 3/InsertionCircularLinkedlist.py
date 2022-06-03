class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    if not head:
        return Node(data)
        # Assign the data into newNode.
    newNode = Node(data)
    newNode.next = head
    head = newNode
    return head


def circular(head):
    start = head
    while (head.next is not None):
        head = head.next  # to reach end of the list

    head.next = start  # Link the end of linked list to start
    return start


def displayList(node):
    start = node
    while (node.next is not start):
        print("{} ".format(node.data), end="")
        node = node.next
    # Display the last node of circular linked list.
    print("{} ".format(node.data), end="")


# Driver Code

if __name__ == '__main__':
    # Start with empty list
    head = None
    # Linked List 12 23 34 41 69
    head = push(head, 45)
    head = push(head, 36)
    head = push(head, 27)
    head = push(head, 18)
    head = push(head, 9)
    circular(head)
    print("The Nodes of the Circular Linked list:")
    displayList(head)