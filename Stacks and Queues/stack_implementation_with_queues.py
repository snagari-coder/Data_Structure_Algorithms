from queue import Queue


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.

        """
        self.q1 = Queue()
        self.q2 = Queue()
        self.current_size = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q1.put(x)
        self.current_size += 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        #print("size: ", self.q1.qsize())
        while self.q1.qsize() > 1:
            a = self.q1.get()
            self.q2.put(a)
            #print("size: ", self.q1.qsize())

        popped = self.q1.get()
        self.current_size -= 1
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q
        return popped

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q1.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.q1.empty():
            return True
        else:
            return False
# Time complexity - push --> O(1), pop --> O(n)

s = MyStack()
s.push(1)
s.push(2)
s.push(3)
print("Top is: ", s.top())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.empty())
