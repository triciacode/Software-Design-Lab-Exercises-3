
#Node class
class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class singly_LinkedList:
   def __init__(self):
      self.head = None

   def listdisplay(self):
      display = self.head
      while display is not None:
         print (display.data)
         display = display.next

list = singly_LinkedList()
list.head = Node("Beef")
s2 = Node("Pork")
s3 = Node("chicken")

# Link first Node to second node
list.head.next = s2

# Link second Node to third node
s2.next = s3

list.listdisplay()