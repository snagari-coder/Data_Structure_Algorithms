class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)
        return

    def pop(self):
        if len(self.stack_list) == 0:
            print('The stack is empty')
            return
        else:
            print("The popped element is: ", self.stack_list.pop())
            return

    def peek(self):
        if len(self.stack_list) == 0:
            print('The stack is empty')
            return
        else:
            return self.stack_list[len(self.stack_list) - 1]

    # Stack follows LIFO, so when we print, we should print in LIFO fashion.
    # O(n) time complexity as we traverse through the array
    def print_stack(self):

        if len(self.stack_list) == 0:
            print("stack is empty")
        else:
            for i in range(len(self.stack_list)-1, -1, -1):
                print(self.stack_list[i])
            return


my_stack = Stack()

my_stack.push(1)
my_stack.pop()
my_stack.peek()
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
# my_stack.peek()
# my_stack.pop()
my_stack.print_stack(
