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

    def BFS(self):
        current_node = self.root
        BFS_result = [] # to store the result
        queue = [] # queue to track the children of each node
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            BFS_result.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return BFS_result

    def BFS_recursive(self, queue, BFS_list):
        if len(queue) == 0:
            return BFS_list
        current_node = queue.pop(0)
        BFS_list.append(current_node.data)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        return self.BFS_recursive(queue, BFS_list)


myTree = BinarySearchTree()
myTree.insert(5)
myTree.insert(3)
myTree.insert(7)
myTree.insert(1)
myTree.insert(13)
myTree.insert(65)
myTree.insert(0)
myTree.insert(10)
print(myTree.lookup2(1))
print(myTree.lookup2(10))

print(myTree.BFS())
print(myTree.BFS_recursive([myTree.root], []))
