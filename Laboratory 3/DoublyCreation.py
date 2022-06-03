class Node(object):
    # Doubly linked node
    def __init__(self, data=None): #function that initializes the node
        self.data = data
        self.next = None
        self.prev = None


class doubly_linked_list(object): #function that initializes the head
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data): #function to append an item at the e
        # Append an item
        new_item = Node(data)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item

        self.count += 1

    def print(self):
        for node in self.iter():
            print(node)

    def iter(self):
        # Iterate the list
        current = self.head
        while current:
            item_val = current.data
            current = current.next
            yield item_val


items = doubly_linked_list()
items.append('P')
items.append('A')
items.append('T')
items.append('R')
items.append('I')
items.append('C')
items.append('I')
items.append('A')
print("Items in the Doubly linked list: ")
items.print()