#Insertion Singly List

#Node Class
class Node:
    def __init__(self, data):
        # Singly linked node
        self.data = data
        self.next = None
class singly_linkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def a (self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    def insert(self, prev, data):
        if not prev:
            print("Previous node is not in the list")
            return

        new_node = Node(data)
        new_node.next= prev.next
        prev.next = new_node


slist=  singly_linkedList()
slist.append('A')
slist.append('B')
slist.append('c')
slist.insert(slist.head.next, "E")
slist.print_list()