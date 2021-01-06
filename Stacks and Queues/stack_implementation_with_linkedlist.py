class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = self.top
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.bottom is None:
            self.bottom = new_node
            self.top = self.bottom
            self.length = 1
        else:
            self.top.next = new_node
            self.top = new_node
            self.length += 1

    def pop(self):
        if self.bottom is None:
            print('The stack is empty')
            return
        elif self.length == 1:
            print("The popped element is: ", self.top.data)
            self.top = None
            self.bottom = self.top
            self.length -= 1
            return
        else:
            current_node = self.bottom
            count = 1
            while count < self.length-1:
                current_node = current_node.next
                count += 1

            print("The popped element is: ", current_node.next.data)
            current_node.next = None
            self.length -= 1
            return

    def peek(self):
              
        if self.bottom is None:
            print('The stack is empty')
        elif self.length == 1:
            print("The topmost element is: ", self.bottom.data)
        else:
            '''
            This can be done as well, but a single line of code as
            shown should be sufficient. Just return/print the topmost
            element.
            
            current_node = self.bottom
            while current_node.next is not None:
                current_node = current_node.next
            print("The topmost element is: ", current_node.data)
            '''
            print("The topmost element is: ", self.top.data)

    def print_stack(self):

        if self.bottom is None:
            print("stack is empty")

        current_node = self.bottom
        all_stack_elements = []

        while current_node is not None:
            all_stack_elements.append(current_node.data)
            current_node = current_node.next

        print(all_stack_elements)


my_stack = Stack()


my_stack.push(1)
my_stack.pop()
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
my_stack.print_stack()
my_stack.peek()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.peek()
my_stack.print_stack()
print(my_stack.length)
