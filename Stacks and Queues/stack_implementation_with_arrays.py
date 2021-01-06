class Stack:
    def __init__(self):
        self.stack_list = []
        self.top = None
        self.bottom = self.top
        self.length = len(self.stack_list)

    def push(self, value):

        if self.length == 0:
            self.bottom = self.stack_list.append(value)
            self.top = self.bottom
            self.length = 1
        else:
            self.top = self.stack_list.append(value)
            self.bottom = self.stack_list[0]
            self.length += 1

    def pop(self):
        if self.length is None:
            print('The stack is empty')
            return
        elif self.length == 1:
            print("The popped element is: ", self.stack_list[0])
            self.stack_list.remove(self.stack_list[0])
            self.length = 0
            self.top = None
            self.bottom = self.top
            return
        else:
            print("The popped element is: ", self.stack_list[len(self.stack_list) - 1])
            self.stack_list.remove(self.stack_list[len(self.stack_list) - 1])
            self.length -= 1
            self.top = self.stack_list[len(self.stack_list) - 1]
            self.bottom = self.stack_list[0]
            return

    def peek(self):

        if self.bottom is None:
            print('The stack is empty')
        elif self.length == 1:
            print("The topmost element is: ", self.stack_list[0])
        else:
            print("The topmost element is: ", self.stack_list[len(self.stack_list) - 1])

    def print_stack(self):

        if self.length == 0:
            print("stack is empty")
        else:
            print(self.stack_list)


my_stack = Stack()

my_stack.push(1)
print(my_stack.length)
my_stack.pop()
#my_stack.peek()
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
#my_stack.peek()
#my_stack.pop()

my_stack.print_stack()
print(my_stack.length)
