INT_MAX = 4294967296
INT_MIN = -4294967296


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_bst(node):
    return is_bst_util(node, INT_MIN, INT_MAX)


def is_bst_util(node, minimum, maximum):
    if node is None:
        return True
    if node.data < minimum or node.data > maximum:
        return False
    return is_bst_util(node.left, minimum, node.data) and is_bst_util(node.right, node.data, maximum)

'''
root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(4)
'''

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if is_bst(root):
    print("The tree is BST")
else:
    print("The tree is not BST")

