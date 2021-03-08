# DFS or Depth First Search is another traversal algorithm.
# In this, we traverse to the depths of the tree/graph until we can't go further, in which case, we go back up
# and repeat the process for the unvisited nodes
# DFS Traversals can be of 3 types - PreOrder, InOrder, and PostOrder.
# Again , to implement this, we'll need a BST which we have already coded. So we'll use that.

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.number_of_nodes += 1
            return
        else:
            current_node = self.root
            while (current_node.left != new_node) and (current_node.right != new_node):
                # Going left
                if new_node.data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
                # Going right
                elif new_node.data > current_node.data:
                    if current_node.right is None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right

            self.number_of_nodes += 1
            return

    def lookup(self, value):

        if self.root is None:
            return "The tree is empty"
        else:
            current_node = self.root
            while True:
                if current_node is None:
                    return "not found"
                elif current_node.data == value:
                    return "found"
                # go left
                elif current_node.data > value:
                    current_node = current_node.left
                # go right
                elif current_node.data < value:
                    current_node = current_node.right

    def lookup2(self, value):
        if self.root is None:
            return "Tree is empty"
        else:
            current_node = self.root
            while current_node is not None:
                if current_node.data > value:
                    current_node = current_node.left
                elif current_node.data < value:
                    current_node = current_node.right
                elif current_node.data == value:
                    return "found"

            return "not found"

    # Now we'll implement the three kinds of DFS Traversals.
    def inorder(self):
        return inorder_traversal(self.root, [])

    def preorder(self):
        return preorder_traversal(self.root, [])

    def postorder(self):
        return postorder_traversal(self.root, [])


def inorder_traversal(node, DFS_list):
    if node.left:
        inorder_traversal(node.left, DFS_list)
    DFS_list.append(node.data)
    if node.right:
        inorder_traversal(node.right, DFS_list)
    return DFS_list


def preorder_traversal(node, DFS_list):
    DFS_list.append(node.data)
    if node.left:
        preorder_traversal(node.left, DFS_list)
    if node.right:
        preorder_traversal(node.right, DFS_list)
    return DFS_list


def postorder_traversal(node, DFS_list):
    if node.left:
        postorder_traversal(node.left, DFS_list)
    if node.right:
        postorder_traversal(node.right, DFS_list)
    DFS_list.append(node.data)
    return DFS_list


myTree = BinarySearchTree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(6)
myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
myTree.insert(1)
print(myTree.lookup2(1))
print(myTree.lookup2(10))
print("InOrder DFS traversal ---> ", myTree.inorder())
print("PreOrder DFS traversal ---> ", myTree.preorder())
print("PostOrder DFS traversal ---> ", myTree.postorder())
