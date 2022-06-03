class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


# A function to do inorder tree traversal
def printInorder(root):
    if root:

        printInorder(root.left)

        print(root.val),

        printInorder(root.right)


# A function to do postorder tree traversal
def printPostorder(root):
    if root:

        printPostorder(root.left)

        printPostorder(root.right)

        print(root.val),


# A function to do preorder tree traversal
def printPreorder(root):
    if root:

        print(root.val),

        printPreorder(root.left)

        printPreorder(root.right)


# Driver code
root = Node(14)
root.left = Node(23)
root.right = Node(24)
root.left.left = Node(31)
root.left.right = Node(52)
root.left.right = Node(56)
print("Preorder traversal of binary tree is")
printPreorder(root)

print("Inorder traversal of binary tree is")
printInorder(root)

print("Postorder traversal of binary tree is")
printPostorder(root)