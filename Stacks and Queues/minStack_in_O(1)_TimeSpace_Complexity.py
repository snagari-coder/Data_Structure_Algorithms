# Implement a Stack in which you can get min element in O(1) time and O(1) space.

class Stack:
    def __init__(self):
        self.stack_list=[]
        self.min_stack = 0

    def push(self,value):
        print("Inserted element is: ", value)
        if len(self.stack_list) == 0:
            self.min_stack = value
            self.stack_list.append(value)
        else:
            if value < self.min_stack:
                calculated_element = 2 * value - self.min_stack
                self.stack_list.append(calculated_element)
                self.min_stack = value
            else:
                self.stack_list.append(value)

    def pop(self):
        if len(self.stack_list) == 0:
            print("Stack is empty")
            return
        else:
            popped = self.stack_list.pop()
            if popped < self.min_stack:
                print("popped element: ", self.min_stack)
                self.min_stack = 2 * self.min_stack - popped
                return
            else:
                print("popped element: ", popped)
                return

    def peek(self):
        if len(self.stack_list) == 0:
            print("Stack is empty")
            return
        else:
            top = self.stack_list[len(self.stack_list) - 1]
            if top < self.min_stack:
                print("Top element of stack is: ", self.min_stack)
                return
            else:
                print("Top element of stack is: ", top)
                return

    def getMin(self):
        print("Current minimum element of the stack: ", self.min_stack)
        return


stack = Stack()

stack.push(3)
stack.push(5)
stack.getMin()
stack.push(2)
stack.push(1)
stack.getMin()
stack.pop()
stack.getMin()
stack.pop()
stack.peek()

